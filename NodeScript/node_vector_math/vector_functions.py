import bpy
from ..node_utils.util_functions import *
def vector_math_node(operation:str,input0:bpy.types.NodeSocket|int|float|None = None\
                        ,input1:bpy.types.NodeSocket|int|float|None = None\
                        ,input2:bpy.types.NodeSocket|int|float|None = None\
                        ,input3:bpy.types.NodeSocket|int|float|None = None)\
                            ->bpy.types.NodeSocketVector|bpy.types.NodeSocketFloat:
    return new_node("ShaderNodeVectorMath",operation,input0,input1,input2,input3)
def vfloordiv(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vfloor(vdiv(input0,input1))
def vector3(x:bpy.types.NodeSocket|int|float,y:bpy.types.NodeSocket|int|float,z:bpy.types.NodeSocket|int|float,label:str='')->bpy.types.NodeSocketVector:
    node:bpy.types.ShaderNodeCombineXYZ = get_node_tree().nodes.new(type="ShaderNodeCombineXYZ")
    load_socket(x,get_node_tree().links,node.inputs[0])
    load_socket(y,get_node_tree().links,node.inputs[1])
    load_socket(z,get_node_tree().links,node.inputs[2])
    node.label=label
    return node.outputs[0]
def vadd(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("ADD",input0 = input0,input1 = input1)
def vsub(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("SUBTRACT",input0 = input0,input1 = input1)
def vmul(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("MULTIPLY",input0 = input0,input1 = input1)
def vdiv(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("DIVIDE",input0 = input0,input1 = input1)
def vmul_add(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("MULTIPLY_ADD",input0 = input0,input1 = input1,input2 = input2)
def vcross(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("CROSS_PRODUCT",input0 = input0,input1 = input1)
def vproject(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("PROJECT",input0 = input0,input1 = input1)
def vreflect(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("REFLECT",input0 = input0,input1 = input1)
def vrefract(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("REFRACT",input0 = input0,input1 = input1,input3 = input2)
def vfaceforward(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("FACEFORWARD",input0 = input0,input1 = input1,input2 = input2)
def vdot(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return vector_math_node("DOT_PRODUCT",input0 = input0,input1 = input1)
def vdistance(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return vector_math_node("DISTANCE",input0 = input0,input1 = input1)
def vlength(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return vector_math_node("LENGTH",input0 = input0)
def vscale(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("SCALE",input0 = input0,input3 = input1)
def vnormalize(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("NORMALIZE",input0 = input0)
def vabs(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("ABSOLUTE",input0 = input0)
def vmin(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("MINIMUM",input0 = input0,input1 = input1)
def vmax(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("MAXIMUM",input0 = input0,input1 = input1)
def vfloor(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("FLOOR",input0 = input0)
def vceil(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("CEIL",input0 = input0)
def vfraction(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("FRACTION",input0 = input0)
def vmod(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("MODULO",input0 = input0,input1 = input1)
def vwrap(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("WRAP",input0 = input0,input1 = input1,input2 = input2)
def vsnap(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("SNAP",input0 = input0,input1 = input1)
def vsin(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("SINE",input0 = input0)
def vcos(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("COSINE",input0 = input0)
def vtan(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketVector:
    return vector_math_node("TANGENT",input0 = input0)
