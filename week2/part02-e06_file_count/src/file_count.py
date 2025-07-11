#!/usr/bin/env python3

import sys

def file_count(filename):
    # lines, words and characters
    l = []
    with open(filename) as file:
        lines = file.readlines()
        line_c = len(lines)
        word_c = sum(len(line.split()) for line in lines)
        char_c = sum(len(line) for line in lines)

    return (line_c,word_c,char_c)

def main():
    if True:
        for filename in sys.argv[1:]:
            params = file_count(filename)
            print(f"{params[0]}\t{params[1]}\t{params[2]}\t{filename}")
    else:
        print(file_count("src/test.txt"))

if __name__ == "__main__":
    main()
