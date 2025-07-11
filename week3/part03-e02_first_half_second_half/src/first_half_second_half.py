#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    first_half = a[:,:a.shape[1]//2]
    second_half = a[:,a.shape[1]//2:]
    # axis=1 vertical comparison
    comparison = np.sum(first_half,axis=1) > np.sum(second_half,axis=1)
    return a[comparison]

def main():
    a = np.array(
        [[1, 3, 4, 2],
        [2, 2, 1, 2]]
        )
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
