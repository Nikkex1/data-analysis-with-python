#!/usr/bin/env python3
import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

def explained_variance():
    # read the data
    df = pd.read_csv("src/data.tsv",sep="\t")

    # variance
    var = df.var(axis=0)
    # fit PCA to the data
    pca = PCA(random_state=0)
    pca.fit(df)

    # return variances (all/PCA)
    return var, pca.explained_variance_

def main():
    if True:
        v, ev = explained_variance()
        print(sum(v), sum(ev))
        var_l = " ".join([f"{var:.3f}" for var in v])
        ev_l = " ".join([f"{ev:.3f}" for ev in ev])
        print(f"The variances are: {var_l}")
        print(f"The explained variances after PCA are: {ev_l}")
        #plot cumulative explained variances
        cum_sum = np.cumsum(ev)
        plt.plot(np.arange(1,len(cum_sum)+1),cum_sum)
        plt.show()
    else:
        print(explained_variance())

if __name__ == "__main__":
    main()
