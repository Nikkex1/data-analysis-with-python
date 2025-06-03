#!/usr/bin/env python3

def find_matching(L, pattern):
    new = []
    for i, x in enumerate(L):
        if pattern in x:
            new.append(i)

    return new

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
