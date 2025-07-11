#!/usr/bin/env python3

def merge(L1, L2):
    temp = L1 + L2
    L = []
    for i in range(len(temp)):
        smallest = min(temp)
        L.append(smallest)
        temp.remove(smallest)

    return L

def main():
    L1 = [1,2,3,4,5]
    L2 = [2,4,6,8,10]
    print(merge(L1,L2))

if __name__ == "__main__":
    main()
