#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
import numpy as np

def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv",sep="\t")
    model = linear_model.LinearRegression(fit_intercept=True)
    x = df.loc[:,"X1":"X5"]
    y = df.loc[:,"Y"]
    model.fit(x,y)

    r2_list = []
    r2_all = model.score(x,y)
    r2_list.append(r2_all)

    for i in range(1,6):
        c = f"X{i}"
        x = df.loc[:,c]
        # convert x to np array, does not work otherwise in this case
        x = np.array(x)[:,np.newaxis]
        model.fit(x,y)
        r2 = model.score(x,y)
        r2_list.append(r2)

    return r2_list
    
def main():
    r2s = coefficient_of_determination()
    for i, r in enumerate(r2s):
        if i == 0:
            print(f"R-score with feature(s) X: {r}")
        else:
            print(f"R-score with feature(s) X{i}: {r}")

if __name__ == "__main__":
    main()
