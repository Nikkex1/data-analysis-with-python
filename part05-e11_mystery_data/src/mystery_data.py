#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv",sep="\t")
    model = LinearRegression(fit_intercept=False)
    # remember : to include all rows!
    x = df.loc[:,"X1":"X5"]
    y = df.loc[:,"Y"]
    model.fit(x,y)
    coeffs = model.coef_
    return coeffs

def main():
    coefficients = mystery_data()
    for i, c in enumerate(coefficients):
        print(f"Coefficient of X{i+1} is {c}")
    
if __name__ == "__main__":
    main()
