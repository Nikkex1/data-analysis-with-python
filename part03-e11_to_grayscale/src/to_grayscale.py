#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    gray = np.array([0.2126, 0.7152, 0.0722])
    image = img @ gray
    return image

def to_red(img):
    image = img
    image[:,:,(1,2)] = 0
    return image

def to_green(img):
    image = img
    image[:,:,(0,2)] = 0
    return image

def to_blue(img):
    image = img
    image[:,:,(0,1)] = 0
    return image

def main():
    img = plt.imread("src/painting.png")
    plt.gray()
    plt.imshow(to_grayscale(img))
    fig, ax = plt.subplots(3)
    ax[0].imshow(to_red(img))
    ax[1].imshow(to_green(img))
    ax[2].imshow(to_blue(img))
    plt.show()

if __name__ == "__main__":
    main()
