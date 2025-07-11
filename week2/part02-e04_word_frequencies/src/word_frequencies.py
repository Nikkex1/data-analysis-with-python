#!/usr/bin/env python3

def word_frequencies(filename):
    word_count = {}
    with open(filename) as file:
        parts = [line.split() for line in file]
        for item in parts:
            for line in item:
                word = line.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1

    return word_count

def main():
    print(word_frequencies("src/alice.txt"))

if __name__ == "__main__":
    main()
