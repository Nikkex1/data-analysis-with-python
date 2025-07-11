#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    c1 = a[:,0]
    c2 = a[:,1]
    c = a[:,2]
    s = a[:,3]
    plt.subplot(1,2,1)
    plt.plot(c1,c2)
    plt.subplot(1,2,2)
    plt.scatter(c1,c2,c=c,s=s)
    plt.show()

def main():
    array = np.array([[1,2,3,4],
                      [4,5,6,7]])
    print(subfigures(array))

if __name__ == "__main__":
    main()
