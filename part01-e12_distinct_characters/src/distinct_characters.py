#!/usr/bin/env python3

def distinct_characters(L):
    dict = {}
    for item in L:
        temp_string = set(item)
        if item not in dict:
            dict[item] = len(temp_string)

    return dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
