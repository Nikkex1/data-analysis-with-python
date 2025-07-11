#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    nominator = np.sum(X*Y,axis=1)
    denominator = np.sqrt(np.sum(X**2,axis=1)) * np.sqrt(np.sum(Y**2,axis=1))
    
    angle = np.clip(nominator / denominator,-1.0,1.0)
    radians = np.arccos(angle)
    degrees = np.degrees(radians)
    return degrees



def main():
    np.random.seed(9)
    array1 = np.random.randint(0,10,(3,4))
    array2 = np.random.randint(0,10,(3,4))
    print(vector_angles(array1,array2))

if __name__ == "__main__":
    main()
