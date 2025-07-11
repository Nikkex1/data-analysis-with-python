#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    # choose column
    data = df["Population change from the previous year, %"] > 0
    return data.mean()

def main():
    df = pd.read_csv("src/municipal.tsv",sep="\t",index_col="Region 2018")
    df = df["Akaa":"Äänekoski"]
    proportion = growing_municipalities(df)
    print(f"Proportion of growing municipalities: {100* proportion:.1f}%")

if __name__ == "__main__":
    main()
