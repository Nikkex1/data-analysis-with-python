#!/usr/bin/env python3

def interleave(*lists):
    new = []
    for items in zip(*lists):
        new.extend(items)

    return new

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
