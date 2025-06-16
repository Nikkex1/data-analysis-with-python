#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    center_y, center_x = a.shape[:2]
    center_y = (center_y - 1) / 2
    center_x = (center_x - 1) / 2
    return (center_y,center_x)   # note the order: (center_y, center_x)

def radial_distance(a):
    center_y, center_x = center(a)
    y_idx, x_idx = np.indices(a.shape[:2])
    d = np.sqrt((x_idx-center_x)**2 + (y_idx-center_y)**2)
    return d

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.interp(a,(a.min(),a.max()),(tmin,tmax))

def radial_mask(a):
    return scale(1-radial_distance(a))

def radial_fade(a):
    return a * radial_mask(a)[:,:,np.newaxis]

def main():
    img = plt.imread("src/painting.png")
    f,ax = plt.subplots(3,1)
    ax[0].imshow(img)
    ax[1].imshow(radial_mask(img))
    ax[2].imshow(radial_fade(img))
    plt.show()

if __name__ == "__main__":
    main()
