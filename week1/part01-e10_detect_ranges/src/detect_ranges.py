#!/usr/bin/env python3

def detect_ranges(L):
    new = sorted(L)
    final_list = []
    start_value, end_value = 0,0
    skip_condition = False
    for i in range(len(new)):
        # last item
        if i == len(new) - 1:
            if new[i] - 1 == new[i-1]:
                end_value = new[i] + 1
                final_list.append((start_value,end_value))
                break
            else:
                final_list.append(new[i])
                break
        # determine start point
        if new[i] + 1 == new[i+1] and new[i] - 1 != new[i-1]:
            start_value = new[i]
            skip_condition = True
            continue
        # determine end point
        if new[i] - 1 == new[i-1] and new[i] + 1 != new[i+1]:
            end_value = new[i] + 1
            skip_condition = False
            final_list.append((start_value,end_value))
            continue

        if skip_condition:
            continue
        final_list.append(new[i])

    return final_list
        

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13, 14, 16, 19]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()