#!/usr/bin/python3

import numpy as np

def meeting_lines(a1, b1, a2, b2):
    coeffs = np.array([[a1,-1],[a2,-1]])
    dependent = np.array([-b1,-b2])
    return np.linalg.solve(coeffs,dependent)

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
