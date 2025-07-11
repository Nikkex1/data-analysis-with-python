#!/usr/bin/env python3

import pandas as pd

def cities():
    idx = ["Helsinki","Espoo","Tampere","Vantaa","Oulu"]
    column_names = ["Population","Total area"]
    data = [[643272,715.48],
           [279044,528.03],
           [231853,689.59],
           [223027,240.35],
           [201810,3817.52]]

    df = pd.DataFrame(data,index=idx,columns=column_names)
    return df
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
