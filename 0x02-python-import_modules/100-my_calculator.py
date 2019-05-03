#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, div, mul

    args = len(argv)

    operan = {add: '+', sub: '-', mul: '*', div: '/'}

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] in operan:
        a = int(argv[1])
        b = int(argv[3])
        evaluation = operan[argv[2]]
        result = evaluation(a, b)
        print("{} {} {} = {}".format(a, argv[2], b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
