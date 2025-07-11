#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    while True:
        cmd = input("Choose a shape (triangle, rectangle, circle): ")
        if cmd == "triangle":
            b = int(input("Give base of the triangle: "))
            h = int(input("Give height of the triangle: "))
            print(f"The area is {b*h/2:.6f}")
        elif cmd == "rectangle":
            w = int(input("Give width of the rectangle: "))
            h = int(input("Give height of the rectangle: "))
            print(f"The area is {w*h:.6f}")
        elif cmd == "circle":
            r = int(input("Give radius of the circle: "))
            print(f"The area is {math.pi*r**2:.6f}")
        elif cmd == "":
            break
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
