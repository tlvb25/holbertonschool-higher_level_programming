#!/usr/bin/python3
if __name__ == '__main__':
        from calculator_1 import *
        from sys import *

        args = len(argv)
        a = argv[1]
        c = argv[2]
        b = argv[3]

        if args < 3 or args > 3:
                print("Usage: ./100-my_calculator.py <a> <operator> <b>")
                exit(1)
        if c != "+" or c != "/" or c != "*" or c != "-":
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
        if c == "+":
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif c == "-":
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif c == "*":
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        else:
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
