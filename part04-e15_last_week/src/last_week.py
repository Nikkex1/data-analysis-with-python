#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df["WoC"] -= 1
    df = df[~df["LW"].isin(["New", "Re"])]
    df["LW"] = df["LW"].astype(int)

    mask1 = df["Peak Pos"] == df["Pos"]
    mask2 = df["Pos"] < df["LW"]
    df.loc[mask1 & mask2, "Peak Pos"] = np.nan
    
    df = df.sort_values("LW")
    df.index = df["LW"]
    df = df.reindex(range(1, 41))
    df["Pos"] = df.index
    df["LW"] = np.nan

    return df

def main():
    if True:
        df = last_week()
        print("Shape: {}, {}".format(*df.shape))
        print("dtypes:", df.dtypes)
        print(df)
    else:
        print(last_week())


if __name__ == "__main__":
    main()
