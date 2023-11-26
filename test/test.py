import bpy
from ..NodeScript import *
function_list = [add,
    sub,
    mul,
    div,
    mul_add,
    pow,
    log,
    sqrt,
    inv_sqrt,
    abs,
    exp,
    min,
    max,
    less_than,
    greater_than,
    sign,
    compare,
    smooth_min,
    smooth_max,
    round,
    floor,
    ceil,
    trunc,
    fract,
    mod,
    floored_mod,
    wrap,
    snap,
    pingpong,
    sin,
    cos,
    tan,
    asin,
    acos,
    atan,
    atan2,
    sinh,
    cosh,
    tanh,
    deg2rad,
    rad2deg,
    floordiv]
vector_function_list = [vadd,
    vsub,
    vmul,
    vdiv,
    vmul_add,
    vcross,
    vproject,
    vreflect,
    vrefract,
    vfaceforward,
    vdot,
    vdistance,
    vlength,
    vscale,
    vnormalize,
    vabs,
    vmin,
    vmax,
    vfloor,
    vceil,
    vfraction,
    vmod,
    vwrap,
    vsnap,
    vsin,
    vcos,
    vtan,
    vfloordiv]
def check_func(funcsion_list):
    for func in funcsion_list:
        sf = value(1,'sf1')
        sv = vector3(1,1,1)
        f_v = 0.1
        i_v = 1
        paramList = [sf,sv,f_v,i_v]
        argnum = func.__code__.co_argcount
        for i in range(4**argnum):
            args=[]
            tmp_num = i
            for j in range(argnum):
                args.append(paramList[tmp_num % 4])
                tmp_num //=4
            
            func(*(args[:argnum]))
            print(f"{func.__name__} checked!")
def error_check(func,a,b):
    try:
        func(a,b)
        raise RuntimeError(f"エラーを出力すべきポイントでエラーを出力していません。\n{func.__name__}")
    except TypeError as e:
        print(func.__name__)
        print(e)
        print(type(e))
def check_operator():
    sf = value(1,'sf1')
    sv = vector3(1,1,1)
    f_v = 0.1
    i_v = 1
    # NodeSocketFloat-NodeSocketFloat
    sf+sf
    sf-sf
    sf*sf
    sf/sf
    sf//sf
    sf%sf
    # NodeSocketFloat-float
    sf+f_v
    sf-f_v
    sf*f_v
    sf/f_v
    sf//f_v
    sf%f_v
    # NodeSocketFloat-int
    sf+i_v
    sf-i_v
    sf*i_v
    sf/i_v
    sf//i_v
    sf%i_v
    # NodeSocketFloat-NodeSocketVector
    error_check(bpy.types.NodeSocketFloat.__add__,sf,sv)
    error_check(bpy.types.NodeSocketFloat.__sub__,sf,sv)
    error_check(bpy.types.NodeSocketFloat.__mul__,sf,sv)
    error_check(bpy.types.NodeSocketFloat.__truediv__,sf,sv)
    error_check(bpy.types.NodeSocketFloat.__floordiv__,sf,sv)
    error_check(bpy.types.NodeSocketFloat.__mod__,sf,sv)
    # NodeSocketVector-NodeSocketVector
    sv+sv
    sv-sv
    sv*sv
    sv/sv
    sv//sv
    sv%sv
    # NodeSocketVector-float
    error_check(bpy.types.NodeSocketVector.__add__,sv,f_v)
    error_check(bpy.types.NodeSocketVector.__sub__,sv,f_v)
    error_check(bpy.types.NodeSocketVector.__mul__,sv,f_v)
    error_check(bpy.types.NodeSocketVector.__truediv__,sv,f_v)
    error_check(bpy.types.NodeSocketVector.__floordiv__,sv,f_v)
    error_check(bpy.types.NodeSocketVector.__mod__,sv,f_v)
    # NodeSocketVector-int
    error_check(bpy.types.NodeSocketVector.__add__,sv,i_v)
    error_check(bpy.types.NodeSocketVector.__sub__,sv,i_v)
    error_check(bpy.types.NodeSocketVector.__mul__,sv,i_v)
    error_check(bpy.types.NodeSocketVector.__truediv__,sv,i_v)
    error_check(bpy.types.NodeSocketVector.__floordiv__,sv,i_v)
    error_check(bpy.types.NodeSocketVector.__mod__,sv,i_v)
    # NodeSocketVector-NodeSocketFloat
    error_check(bpy.types.NodeSocketVector.__add__,sv,sf)
    error_check(bpy.types.NodeSocketVector.__sub__,sv,sf)
    error_check(bpy.types.NodeSocketVector.__mul__,sv,sf)
    error_check(bpy.types.NodeSocketVector.__truediv__,sv,sf)
    error_check(bpy.types.NodeSocketVector.__floordiv__,sv,sf)
    error_check(bpy.types.NodeSocketVector.__mod__,sv,sf)
def check_group():
    val1 = value(5,"a")
    vec1 = vector3(1,1,1,"b")
    val2 = value(5,"c")
    vec2 = vector3(1,1,1,"d")
    node_input = add(mul(val1,vec1),vmul(val2,vec2))
    make_group(node_input)
if __name__ == "__main__":
    check_func(function_list)
    check_func(vector_function_list)
    check_operator()
    check_group()