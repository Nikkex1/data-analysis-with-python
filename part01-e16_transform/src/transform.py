#!/usr/bin/env python3

def transform(s1, s2):
    return list(map(lambda x : int(x[0]) * int(x[1]) ,list(zip(s1.split(),s2.split()))))

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
