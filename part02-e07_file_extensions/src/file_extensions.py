#!/usr/bin/env python3

def file_extensions(filename):
    with open(filename) as file:
        l = []
        d = {}
        for line in file:
            line = line.strip()
            parts = line.split(".")
            if len(parts) == 1:
                l.append(parts[0])
            else:
                if parts[-1] not in d:
                    d[parts[-1]] = []
                d[parts[-1]].append(line)
    return (l, d)

def main():
    if True:
        test = file_extensions("src/filenames.txt")
        print(f"{len(test[0])} files with no extension")
        for key, value in sorted(test[1].items()):
            print(key, len(value))
    else:
        print(file_extensions("src/filenames.txt"))

if __name__ == "__main__":
    main()
