# Enter you module contents here
"""
A module for calculating the length of a hypotenuse and the area of
a right-angled triangle. Both functions take the lengths of the sides
as arguments.
"""

from math import sqrt

__version__ = "1.0"
__author__ = "Nikkex"

def hypotenuse(x,y):
    """
    Calculate the length of the hypotenuse of a right-angled triangle.
    """
    return sqrt(x**2 + y**2)

def area(x,y):
    """
    Calculate the area of a right-angled triangle.
    """
    return (x * y) / 2

if __name__ == "__main__":
    print(hypotenuse(5,8))
    print(area(5,5))