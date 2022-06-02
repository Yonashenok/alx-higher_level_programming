#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *
    arg = argv[1:]
    if len(arg) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif arg[1] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(arg[0])
        b = int(arg[2])
        if arg[1] == "+":
            print("{} + {} = {}".format(arg[0],  arg[2], add(a, b)))
        elif arg[1] == "-":
            print("{} - {} = {}".format(arg[0], arg[2], sub(a, b)))
        elif arg[1] == "*":
            print("{} * {} = {}".format(arg[0], arg[2], mul(a, b)))
        elif arg[1] == "/":
            print("{} / {} = {}".format(arg[0], arg[2], div(a, b)))
