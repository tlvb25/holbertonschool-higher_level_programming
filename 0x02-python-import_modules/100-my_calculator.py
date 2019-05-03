#!/usr/bin/python3
if __name__ == '__main__':
    from sys import *
    from calculator_1 import *
    args = len(argv)
    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]
    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if c == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif c == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif c == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif c == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)