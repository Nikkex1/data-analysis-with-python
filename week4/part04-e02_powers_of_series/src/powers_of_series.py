#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    column_names = [i for i in range(1,k+1)]
    new_s = {}
    for column in column_names:
        new_s[column] = s ** column
    df = pd.DataFrame(new_s)
    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
