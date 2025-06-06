#!/usr/bin/env python3

import sys
from math import sqrt

def summary(filename):
    # sum, average, standard deviation
    l = []
    with open(filename) as file:
        for line in file:
            try:
                l.append(float(line.strip()))
            except ValueError:
                continue

    sum_l = sum(l)
    avg_l = sum_l / len(l)
    std_l = 0
    for number in l:
        std_l += (number - avg_l)**2
    std_l = sqrt(std_l/(len(l)-1))

    return (sum_l,avg_l,std_l)

def main():
    for filename in sys.argv[1:]:
        params = summary(filename)
        print(f"File: {filename} Sum: {params[0]:.6f} Average: {params[1]:.6f} Stddev: {params[2]:.6f}")

if __name__ == "__main__":
    main()
