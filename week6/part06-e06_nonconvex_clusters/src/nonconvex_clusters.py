#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def nonconvex_clusters():
    # read the data
    df = pd.read_csv("src/data.tsv",sep="\t")
    X = df.loc[:,"X1":"X2"]
    y = df.loc[:,"y"]

    # cluster the data using DBSCAN
    results = np.zeros((4,4))
    eps_r = np.arange(0.05, 0.2, 0.05)
    for i, eps_i in enumerate(eps_r):
        # eps value for each clustering
        results[i,0] = eps_i
        # model
        model = DBSCAN(eps=eps_i)
        model.fit(X)
        # number of clusters
        n_clusters = len(set(model.labels_)) - (1 if -1 in model.labels_ else 0)
        results[i,2] = n_clusters
        # score for each clustering
        if n_clusters == len(y.unique()):
            idx = model.labels_ == -1
            acc = accuracy_score(y[~idx],model.labels_[~idx])
            results[i,1] = acc
        else:
            results[i,1] = np.nan
        # outliers
        n_outliers = list(model.labels_).count(-1)
        results[i,3] = n_outliers

    final = pd.DataFrame(results,columns=["eps","Score","Clusters","Outliers"])
    return final

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
