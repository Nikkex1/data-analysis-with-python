#!/usr/bin/env python3

def main():
    # [expression for element in iterable lc-clauses]
    for line in ([f"({a},{b})" for a in range(1,7)
                        for b in range(1,7)
                        if a + b == 5]):
        print(line)

if __name__ == "__main__":
    main()
