import bpy
from ..node_math.functions import *
from .vector_functions import *
def __add_instance_method(method):
    setattr(bpy.types.NodeSocketVector, method.__name__, method)
def	__add__(self, other):
    if type(other)!=bpy.types.NodeSocketVector:
        raise TypeError(f"異なる型同士の演算は'{add.__name__}()'または'{vadd.__name__}()'を利用してください。")
    return vadd(self,other)
def	__sub__(self, other):
    if type(other)!=bpy.types.NodeSocketVector:
        raise TypeError(f"異なる型同士の演算は'{sub.__name__}()'または'{vsub.__name__}()'を利用してください。")
    return vsub(self,other)
def	__mul__(self, other):
    if type(other)!=bpy.types.NodeSocketVector:
        raise TypeError(f"異なる型同士の演算は'{mul.__name__}()'または'{vmul.__name__}()'を利用してください。")
    return vmul(self,other)
def	__truediv__(self, other):
    if type(other)!=bpy.types.NodeSocketVector:
        raise TypeError(f"異なる型同士の演算は'{div.__name__}()'または'{vdiv.__name__}()'を利用してください。")
    return vdiv(self,other)
def	__floordiv__(self, other):
    if type(other)!=bpy.types.NodeSocketVector:
        raise TypeError(f"異なる型同士の演算は'{floordiv.__name__}()'または'{vfloordiv.__name__}()'を利用してください。")
    return vfloordiv(self,other)
def	__mod__(self, other):
    if type(other)!=bpy.types.NodeSocketVector:
        raise TypeError(f"異なる型同士の演算は'{mod.__name__}()'または'{vmod.__name__}()'を利用してください。")
    return vmod(self,other)
def	__radd__(self, other):
    return vadd(other,self)
def	__rsub__(self, other):
    return vsub(other,self)
def	__rmul__(self, other):
    return vmul(other,self)
def	__rtruediv__(self, other):
    return vdiv(other,self)
def	__rfloordiv__(self, other):
    return vfloor(div(other,self))
def	__rmod__(self, other):
    return vmod(other,self)
def __iadd__(self, other):
    return __add__(self,other)
def __isub__(self,other):
    return __sub__(self,other)
def __imul__(self,other):
    return __mul__(self,other)
def __itruediv__(self,other):
    return __truediv__(self,other)
def __ifloordiv__(self,other):
    return __floordiv__(self,other)
def __imod__(self,other):
    return __mod__(self,other)
def __neg__(self):
    return vmul(self,-1)
def x(self:bpy.types.NodeSocketVector)->bpy.types.NodeSocketFloat:
    return __separateXYZ(self).outputs[0]
def y(self:bpy.types.NodeSocketVector)->bpy.types.NodeSocketFloat:
    return __separateXYZ(self).outputs[1]
def z(self:bpy.types.NodeSocketVector)->bpy.types.NodeSocketFloat:
    return __separateXYZ(self).outputs[2]
def __separateXYZ(socket):
    link_list=[link for link in socket.links if type(link.to_node)==bpy.types.ShaderNodeSeparateXYZ]
    if len(link_list)==0:
        current_node = get_node_tree().nodes.new(type="ShaderNodeSeparateXYZ")
    else:
        current_node = link_list[0].to_node
    links = get_node_tree().links
    links.new(socket,current_node.inputs[0])
    return current_node
__add_instance_method(__add__)
__add_instance_method(__sub__)
__add_instance_method(__mul__)
__add_instance_method(__truediv__)
__add_instance_method(__floordiv__)
__add_instance_method(__mod__)
__add_instance_method(__radd__)
__add_instance_method(__rsub__)
__add_instance_method(__rmul__)
__add_instance_method(__rtruediv__)
__add_instance_method(__rfloordiv__)
__add_instance_method(__rmod__)
__add_instance_method(__iadd__)
__add_instance_method(__isub__)
__add_instance_method(__imul__)
__add_instance_method(__itruediv__)
__add_instance_method(__ifloordiv__)
__add_instance_method(__imod__)
__add_instance_method(__neg__)
__add_instance_method(x)
__add_instance_method(y)
__add_instance_method(z)
setattr(bpy.types.NodeSocketVector, "x", property(x))
setattr(bpy.types.NodeSocketVector, "y", property(y))
setattr(bpy.types.NodeSocketVector, "z", property(z))