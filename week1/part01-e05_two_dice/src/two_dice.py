#!/usr/bin/env python3

def main():
    diceroll = range(1,7)
    for i in diceroll:
        for j in diceroll:
            if i + j == 5:
                print(f"({i},{j})")

if __name__ == "__main__":
    main()
