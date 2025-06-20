#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    df.loc[:,"LW"] = df.loc[:,"LW"].replace(["New","Re"],np.nan)
    df.loc[:,"LW"] = pd.to_numeric(df.loc[:,"LW"])
    return df[df.loc[:,"Pos"] > df.loc[:,"LW"]]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
