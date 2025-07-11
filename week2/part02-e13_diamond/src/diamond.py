#!/usr/bin/env python3

import numpy as np

def diamond(n):
    s = np.eye(n,dtype=int)
    s_r = s[::-1]

    upper = np.concatenate((s_r,s[:,1:]),axis=1)
    lower = upper[::-1]

    return np.concatenate((upper, lower[1:,:]))

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
