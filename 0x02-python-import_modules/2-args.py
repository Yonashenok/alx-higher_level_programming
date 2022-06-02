#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)

    if x - 1  == 0:
        print(f"{x-1} {'arguments.'}")
    elif x - 1  == 1:
        print(f"{x-1} {'argument:'}")
        print(f"{x-1} {argv[1]}")
    else:
        print(f"{x-1} {'arguments:'}")
        for i in range(len(argv)):
            if i > 0:
                print(f"{i}: {argv[i]}")
