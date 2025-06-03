#!/usr/bin/env python3
def triple(number: int):
        return number*3

def square(number: int):
    return number**2

def main():
    for i in range(1,11):
        ti = triple(i)
        si = square(i)
        if si > ti:
             break
        print(f"triple({i})=={ti} square({i})=={si}")

if __name__ == "__main__":
    main()
