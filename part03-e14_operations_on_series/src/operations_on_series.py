#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    i = ["a","b","c"]
    s1 = pd.Series(L1,i)
    s2 = pd.Series(L2,i)
    return (s1, s2)
    
def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del s2["b"]
    return (s1, s2)
    
def main():
    l1 = [1,2,3]
    l2 = [4,5,6]
    s1, s2 = create_series(l1,l2)
    print(create_series(l1,l2))
    print(modify_series(s1,s2))
    s3 = s1 + s2
    print(s3)
    
if __name__ == "__main__":
    main()
