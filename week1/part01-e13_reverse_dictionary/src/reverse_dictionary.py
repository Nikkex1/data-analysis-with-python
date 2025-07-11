#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse = {}
    for key, value in d.items():
        for finnish_word in value:
            if finnish_word not in reverse:
                reverse[finnish_word] = []
            reverse[finnish_word].append(key)

    return reverse

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
