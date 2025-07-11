#!/usr/bin/env python3
import pandas as pd
import numpy as np

def read_series():
    # index, value
    series = pd.Series()
    while True:
        line = input("idx value: ")
        if line == "":
            break
        line = line.split()
        series[line[0]] = line[1]
    
    return series

def main():
    print(read_series())

if __name__ == "__main__":
    main()
