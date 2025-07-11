#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv",sep="\t")

    # presidents
    df["President"][2:].replace({
        "Bush, George": "George Bush",
        "Clinton, Bill": "Bill Clinton"},inplace=True)
    
    # start
    df["Start"].replace("2017 Jan", 2017,inplace=True)

    # seasons
    df["Seasons"].replace("two",2,inplace=True)

    # vice-president
    df["Vice-president"].replace({
        "Mike pence": "Mike Pence",
        "joe Biden": "Joe Biden",
        "Cheney, dick": "Dick Cheney",
        "gore, Al": "Al Gore"},inplace=True)

    # convert datatypes
    df["Last"] = pd.to_numeric(df["Last"],errors="coerce")
    df = df.astype({
        "Start":int,
        "Seasons":int
    })

    return df

def main():
    df = cleaning_data()
    print(df)
    print(df.dtypes)

if __name__ == "__main__":
    main()
