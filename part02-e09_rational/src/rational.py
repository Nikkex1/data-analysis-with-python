#!/usr/bin/env python3

class Rational(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        numerator = self.a * other.b + other.a * self.b
        denominator = self.b * other.b
        return Rational(numerator,denominator)

    def __sub__(self, other):
        numerator = self.a * other.b - other.a * self.b
        denominator = self.b * other.b
        return Rational(numerator,denominator)

    def __mul__(self, other):
        numerator = self.a * other.a
        denominator = self.b * other.b
        return Rational(numerator,denominator)

    def __truediv__(self, other):
        numerator = self.a * other.b
        denominator = self.b * other.a
        return Rational(numerator,denominator)

    def __lt__(self, other):
        return (self.a / self.b) < (other.a / other.b)

    def __gt__(self, other):
        return (self.a / self.b) > (other.a / other.b)

    def __eq__(self, other):
        return (self.a / self.b) == (other.a / other.b)
    
    def __str__(self):
        return f"{self.a},{self.b}"

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
