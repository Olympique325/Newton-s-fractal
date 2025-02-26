"""Houses the complex class, which represents complex numbers"""
from math import sqrt

class Complex:
    def __init__(self,a,b):
        self.a: float = a
        self.b: float = b

    def __add__(self, other):
        return Complex(self.a + other.a,self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b*other.b, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        return Complex((self.a*other.a + self.b*other.b)/(other.a * other.a + other.b * other.b)
                       ,(self.b*other.a - self.a*other.b)/(other.a * other.a + other.b * other.b))

    def __abs__(self):
        return sqrt(self.a * self.a + self.b * self.b)

    def __str__(self):
        return str(self.a) + " + i" + str(self.b)