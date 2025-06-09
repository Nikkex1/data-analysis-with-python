#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    # shape[0] 
    center_y, center_x = a.shape[:2]
    center_y = (center_y - 1) / 2
    center_x = (center_x - 1) / 2
    return (center_y,center_x)   # note the order: (center_y, center_x)

def radial_distance(a):
    pass

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.array([[]])

def radial_mask(a):
    return np.array([[]])

def radial_fade(a):
    return np.array([[]])

def main():
    print(center(np.zeros((10, 11, 3))))
    print(radial_distance(np.zeros((10, 11, 3))))

if __name__ == "__main__":
    main()
