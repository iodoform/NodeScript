import bpy
def new_node(nodeType:str,operation:str,*inputs:bpy.types.NodeSocket|int|float|None)->bpy.types.NodeSocket:
    links = get_node_tree().links
    current_node = get_node_tree().nodes.new(type=nodeType)
    current_node.operation = operation
    for i in range(len(current_node.inputs)):
        load_socket(inputs[i],links,current_node.inputs[i])
    output=[output for output in current_node.outputs if output.enabled==True][0]
    return output
def load_socket(load:bpy.types.NodeSocket|float|int|None, links:bpy.types.NodeLinks, input:bpy.types.NodeSocket)->None:
    if load == None:
        return
    if issubclass(type(load),bpy.types.NodeSocket): 
        links.new(load,input)
    elif type(load)==float or type(load)==int: 
        if type(input.default_value)==bpy.types.bpy_prop_array:
            for i in range(len(input.default_value)):
                input.default_value[i]=load
        else:
            input.default_value = load
    else: 
        raise TypeError("bpy.types.NodeSocket、float、またはintを入力してください")
def make_group(input0:bpy.types.NodeSocket,name:str|None=None) ->bpy.types.NodeSocket:
    override_context = get_node_editor_context()
    with bpy.context.temp_override(**override_context):
        select_all_linked_from(input0.node)
        for node in bpy.context.selected_nodes:
            if type(node)==bpy.types.ShaderNodeValue:
                node.select=False
            if type(node)==bpy.types.ShaderNodeCombineXYZ and not any([input.is_linked for input in node.inputs]):
                node.select = False
        node_tree=get_node_tree()
        dummy_node = node_tree.nodes.new(type="ShaderNodeMath")
        node_tree.links.new(dummy_node.inputs[0],input0)
        dummy_node.select=False
        # groupNodeのノードツリーに入る
        bpy.ops.node.group_make()
        groupNode:bpy.types.ShaderNodeGroup = node_tree.nodes[-1]
        bpy.ops.node.tree_path_parent()
        # groupNodeのノードツリーを抜ける
        deleteNode(dummy_node)
        for i,input in enumerate(groupNode.inputs):
            link:bpy.types.NodeLink=input.links[0]
            if type(link.to_socket)==bpy.types.NodeSocketFloat:
                if type(link.from_socket)==bpy.types.NodeSocketFloat:
                    link.to_socket.default_value=link.from_socket.default_value
                    groupNode.node_tree.interface.items_tree[i+1].name="Value" if link.from_node.label=='' else link.from_node.label
                else:
                    groupNode.node_tree.interface.items_tree[i+1].socket_type="NodeSocketVector"
                    groupNode.node_tree.interface.items_tree[i+1].name="Vector" if link.from_node.label=='' else link.from_node.label
                    for j in range(len(link.to_socket.default_value)):
                        link.to_socket.default_value[j]=link.from_node.inputs[j].default_value
            else:
                if type(link.from_socket)==bpy.types.NodeSocketFloat:
                    groupNode.node_tree.interface.items_tree[i+1].socket_type="NodeSocketFloat"
                    groupNode.node_tree.interface.items_tree[i+1].name="Value" if link.from_node.label=='' else link.from_node.label
                    link.to_socket.default_value=link.from_socket.default_value
                else:
                    for j in range(len(link.to_socket.default_value)):
                        link.to_socket.default_value[j]=link.from_node.inputs[j].default_value
                    groupNode.node_tree.interface.items_tree[i+1].name="Vector" if link.from_node.label=='' else link.from_node.label
            deleteNode(link.from_node)
        if name!=None:
            groupNode.node_tree.name=name
            groupNode.label=name
    return groupNode.outputs[0]

def deleteNode(node:bpy.types.Node)->None:
    selected_nodes= bpy.context.selected_nodes
    bpy.ops.node.select(deselect_all=True)
    node.select=True
    bpy.ops.node.delete()
    for tmp_node in selected_nodes:
        tmp_node.select=True

def get_node_editor_context()->bpy.types.Context:
    override_context = None
    for area in bpy.context.screen.areas:
        if area.type == 'NODE_EDITOR':
            override_context = bpy.context.copy()
            override_context["space_data"] = area.spaces[0]
            override_context["area"] = area
            for rgn in area.regions:
                if rgn.type == 'WINDOW':
                    override_context['region'] = rgn
            break
    if override_context==None:
        raise RuntimeError("ノードエディタを起動してから実行してください。")
    return override_context

def select_all_linked_from(node:bpy.types.Node)->None:
    bpy.ops.node.select(deselect_all=True)
    node.select=True
    nodeNum=len(bpy.context.selected_nodes)
    bpy.ops.node.select_linked_from()
    while len(bpy.context.selected_nodes)>nodeNum:
        nodeNum=len(bpy.context.selected_nodes)
        bpy.ops.node.select_linked_from()
def get_node_tree()->bpy.types.NodeTree:
    override_context=get_node_editor_context()
    with bpy.context.temp_override(**override_context):
        return bpy.context.space_data.edit_tree