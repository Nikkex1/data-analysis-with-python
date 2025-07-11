#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    idx = df.loc[:,"Air temperature (degC)"] < 0
    df = df[idx]
    return df.describe().loc["count","Air temperature (degC)"]

def main():
    print(f"Number of days below zero: {int(below_zero())}")
    
if __name__ == "__main__":
    main()
