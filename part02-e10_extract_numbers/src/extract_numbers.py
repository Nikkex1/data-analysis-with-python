#!/usr/bin/env python3

def extract_numbers(s):
    l = []
    split_string = s.split()
    for item in split_string:
        try:
            l.append(int(item))
        except ValueError:
            try:
                l.append(float(item))
            except ValueError:
                pass

    return l

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
