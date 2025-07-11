#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    pub_sum = df.groupby("Publisher").sum().sort_values(by="WoC",ascending=False)
    max_pub = pub_sum.index[0]

    return df[df["Publisher"] == max_pub]

def main():
    df = best_record_company()
    print(df)
    

if __name__ == "__main__":
    main()
