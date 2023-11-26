import bpy
from ..node_utils.util_functions import *
def math_node(operation:str,input0:bpy.types.NodeSocket|int|float = 0\
                        ,input1:bpy.types.NodeSocket|int|float = 0\
                        ,input2:bpy.types.NodeSocket|int|float = 0)->bpy.types.NodeSocketFloat:
    return new_node("ShaderNodeMath",operation,input0,input1,input2)

def add(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("ADD",input0,input1)
def sub(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("SUBTRACT",input0,input1)
def mul(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("MULTIPLY",input0,input1)
def div(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("DIVIDE",input0,input1)
def mul_add(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("MULTIPLY_ADD",input0,input1,input2)
def pow(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("POWER",input0,input1)
def log(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("LOGARITHM",input0,input1)
def sqrt(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("SQRT",input0)
def inv_sqrt(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("INVERSE_SQRT",input0)
def abs(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("ABSOLUTE",input0)
def exp(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("EXPONENT",input0)
def min(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("MINIMUM",input0,input1)
def max(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("MAXIMUM",input0,input1)
def less_than(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("LESS_THAN",input0,input1)
def greater_than(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("GREATER_THAN",input0,input1)
def sign(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("SIGN",input0)
def compare(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("COMPARE",input0,input1,input2)
def smooth_min(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("SMOOTH_MIN",input0,input1,input2)
def smooth_max(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("SMOOTH_MAX",input0,input1,input2)
def round(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("ROUND",input0)
def floor(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("FLOOR",input0)
def ceil(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("CEIL",input0)
def trunc(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("TRUNC",input0)
def fract(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("FRACT",input0)
def mod(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("MODULO",input0,input1)
def floored_mod(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("FLOORED_MODULO",input0,input1)
def wrap(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float,input2:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("WRAP",input0,input1,input2)
def snap(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("SNAP",input0,input1)
def pingpong(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("PINGPONG",input0,input1)
def sin(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("SINE",input0)
def cos(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("COSINE",input0)
def tan(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("TANGENT",input0)
def asin(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("ARCSINE",input0)
def acos(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("ARCCOSINE",input0)
def atan(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("ARCTANGENT",input0)
def atan2(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("ARCTAN2",input0,input1)
def sinh(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("SINH",input0)
def cosh(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("COSH",input0)
def tanh(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("TANH",input0)
def deg2rad(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("RADIANS",input0)
def rad2deg(input0:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return math_node("DEGREES",input0)
def value(val:float|int,label:str='')->bpy.types.NodeSocketFloat:
    node = get_node_tree().nodes.new(type="ShaderNodeValue")
    if type(val) == float or type(val) == int:
        node.outputs[0].default_value = val
        node.label=label
        return node.outputs[0]
    else: raise TypeError("float、またはintを入力してください")
def floordiv(input0:bpy.types.NodeSocket|int|float,input1:bpy.types.NodeSocket|int|float)->bpy.types.NodeSocketFloat:
    return floor(div(input0,input1))