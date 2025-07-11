#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    # size, month, day, hour, minute, filename
    l = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            p = re.findall("\S+",line)
            h, m = int(p[7].split(":")[0]),int(p[7].split(":")[1])
            line_tuple = (int(p[4]),p[5],int(p[6]),h,m,p[8])
            l.append(line_tuple)

    return l

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
