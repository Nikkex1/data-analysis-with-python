#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    if n == 0:
        return np.eye(len(a))
    if n > 0:
        return reduce(lambda x,y : x@y, (a for i in range(n)))
    if n < 0:
        inv = np.linalg.inv(a)
        return reduce(lambda x,y : x@y, (inv for i in range(abs(n))))

def main():
    np.random.seed(0)
    array = np.random.randint(0,10,(4,4))
    print(np.linalg.matrix_power(array,3))
    print(matrix_power(array,3))

if __name__ == "__main__":
    main()
