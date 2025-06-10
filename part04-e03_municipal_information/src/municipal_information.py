#!/usr/bin/env python3

import pandas as pd

def main():
    # dataframe
    data = pd.read_csv("src/municipal.tsv",sep="\t")
    print(f"Shape: {data.shape[0]},{data.shape[1]}")
    print("Columns:")
    for column in data.columns:
        print(column)

if __name__ == "__main__":
    main()
