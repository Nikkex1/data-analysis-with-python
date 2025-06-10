#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    data = pd.read_csv("src/municipal.tsv",sep="\t",index_col="Region 2018")
    # subset from Akaa to Äänekoski
    data = data["Akaa":"Äänekoski"]
    # swedish speaking people and foreigners > 5%
    swedish = data["Share of Swedish-speakers of the population, %"]
    foreign = data["Share of foreign citizens of the population, %"]
    data = data[swedish > 5]
    data = data[foreign > 5]

    # return population, swedish, foreigners
    idx = ["Population","Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]
    return data[idx]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
