import bpy
from .functions import *
from ..node_vector_math.vector_functions import *
def __add_instance_method(method):
    setattr(bpy.types.NodeSocket, method.__name__, method)
def	__add__(self, other):
    if type(other)!=bpy.types.NodeSocketFloat and type(other)!=int and type(other)!=float:
        raise TypeError(f"異なる型同士の演算は'{add.__name__}()'または'{vadd.__name__}()'を利用してください。")
    return add(self,other)
def	__sub__(self, other):
    if type(other)!=bpy.types.NodeSocketFloat and type(other)!=int and type(other)!=float:
        raise TypeError(f"異なる型同士の演算は'{sub.__name__}()'または'{vsub.__name__}()'を利用してください。")
    return sub(self,other)
def	__mul__(self, other):
    if type(other)!=bpy.types.NodeSocketFloat and type(other)!=int and type(other)!=float:
        raise TypeError(f"異なる型同士の演算は'{mul.__name__}()'または'{vmul.__name__}()'を利用してください。")
    return mul(self,other)
def	__truediv__(self, other):
    if type(other)!=bpy.types.NodeSocketFloat and type(other)!=int and type(other)!=float:
        raise TypeError(f"異なる型同士の演算は'{div.__name__}()'または'{vdiv.__name__}()'を利用してください。")
    return div(self,other)
def	__floordiv__(self, other):
    if type(other)!=bpy.types.NodeSocketFloat and type(other)!=int and type(other)!=float:
        raise TypeError(f"異なる型同士の演算は'{floordiv.__name__}()'または'{vfloordiv.__name__}()'を利用してください。")
    return floordiv(self,other)
def	__mod__(self, other):
    if type(other)!=bpy.types.NodeSocketFloat and type(other)!=int and type(other)!=float:
        raise TypeError(f"異なる型同士の演算は'{mod.__name__}()'または'{vmod.__name__}()'を利用してください。")
    return mod(self,other)
def	__pow__(self, other):
    return pow(self,other)
def	__radd__(self, other):
    return add(other,self)
def	__rsub__(self, other):
    return sub(other,self)
def	__rmul__(self, other):
    return mul(other,self)
def	__rtruediv__(self, other):
    return div(other,self)
def	__rfloordiv__(self, other):
    return floor(div(other,self))
def	__rmod__(self, other):
    return mod(other,self)
def	__rpow__(self, other):
    return pow(other,self)
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
def __ipow__(self,other):
    return __pow__(self,other)
def __neg__(self):
    return mul(self,-1)

__add_instance_method(__add__)
__add_instance_method(__sub__)
__add_instance_method(__mul__)
__add_instance_method(__truediv__)
__add_instance_method(__floordiv__)
__add_instance_method(__mod__)
__add_instance_method(__pow__)
__add_instance_method(__radd__)
__add_instance_method(__rsub__)
__add_instance_method(__rmul__)
__add_instance_method(__rtruediv__)
__add_instance_method(__rfloordiv__)
__add_instance_method(__rmod__)
__add_instance_method(__rpow__)
__add_instance_method(__iadd__)
__add_instance_method(__isub__)
__add_instance_method(__imul__)
__add_instance_method(__itruediv__)
__add_instance_method(__ifloordiv__)
__add_instance_method(__imod__)
__add_instance_method(__ipow__)
__add_instance_method(__neg__)