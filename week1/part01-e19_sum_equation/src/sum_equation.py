#!/usr/bin/env python3

def sum_equation(L):
    if len(L) > 0:
        str_list = [str(int) for int in L]
        string = ""
        string = " + ".join(str_list)
        string = f"{string} = {sum(L)}"
        return string
    else:
        return "0 = 0"

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
