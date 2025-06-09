#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    sepal_length = data[:,0]
    petal_length = data[:,2]
    return scipy.stats.pearsonr(sepal_length,petal_length)[0]

def correlations():
    return np.corrcoef(load(),rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
