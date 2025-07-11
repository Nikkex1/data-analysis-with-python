#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    l = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            parts = re.findall("\S+",line)
            if parts[0] == "!":
                continue
            l.append(f"{parts[0]}\t{parts[1]}\t{parts[2]}\t{' '.join(parts[3::])}")

    return l

def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
