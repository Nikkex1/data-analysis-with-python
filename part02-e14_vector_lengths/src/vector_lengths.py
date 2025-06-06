#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    # sqrt(sum(x1-n**2))
    return np.sqrt(np.sum(a**2,axis=1))

def main():
    np.random.seed(9)
    array = np.random.randint(0,10,(3,4))
    print(vector_lengths(array))

if __name__ == "__main__":
    main()
