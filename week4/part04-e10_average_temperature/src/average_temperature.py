#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    idx = df.loc[:,"m"] == 7
    summary = df[idx].describe()
    return summary.loc["mean","Air temperature (degC)"]

def main():
    print(f"Average temperature in July: {average_temperature():.1f}")

if __name__ == "__main__":
    main()
