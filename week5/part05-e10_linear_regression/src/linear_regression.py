#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    # requires 2d array (not 1d), done with [:,np.newaxis]
    model.fit(x[:,np.newaxis],y)

    intercept = model.intercept_
    slope = model.coef_[0]

    return slope, intercept

def main():
    # textual
    x = np.array([1,2,3,4,5,6,7,8,9,10])
    y = np.array([2,4,7,9,11,12,15,16,17,19])
    slope, intercept = fit_line(x,y)
    print(f"Slope: {slope}\nIntercept: {intercept}")

    # plot original data points
    plt.scatter(x,y, color="black")
    # plot linear regression y = b + ax (b: intercept, a: slope)
    plt.plot(intercept + slope * x)
    plt.show()

if __name__ == "__main__":
    main()
