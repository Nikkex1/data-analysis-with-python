#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    return [row for row in np.array(a)]

def get_columns(a):
    return [column for column in np.array(a).T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
