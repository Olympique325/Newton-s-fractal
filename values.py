"""Assign all values to be used in all the scripts"""
from complex import Complex
from math import sqrt

WINDOW_HEIGHT = 4320
WINDOW_WIDTH = 7680

SCALE_X = 2.5
SCALE_Y = 2.5

def f(z : Complex) -> Complex:
    a,b = z.a, z.b
    f_a = pow(a,5) - 10*pow(a,3)*pow(b,2) + 5*a*pow(b,4) - 1
    f_b = 5*pow(a,4)*b - 10*pow(a,2)*pow(b,3) + pow(b,5)
    return Complex(f_a,f_b)

def fder(z : Complex) -> Complex:
    a, b = z.a, z.b
    fder_a = 5*pow(a,4) - 30*pow(a,2)*pow(b,2) + pow(b,4)
    fder_b = 20*pow(a,3)*b - 20*a*pow(b,3)
    return Complex(fder_a, fder_b)

roots = [
    Complex(1,0),
    Complex(-.5,sqrt(3)/2),
    Complex(-.5,-sqrt(3)/2)
]

colours = [
    (252,127,3),
    (52,153,55),
    (79,38,150)
]