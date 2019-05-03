#!/usr/bin/python3
if __name__ == '__main__':
	from calculator_1 import *
	from sys import *

	args = len(argv)
	a = int(argv[1])
	c = argv[2]
	b = int(argv[3])

	if args != 4:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)
	if c == "+":
		print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
	elif c == "-":
		print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
	elif c == "*":
		print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
	elif c == "/":
		print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
	else:
		print("Unknown operator. Available operators: +, -, * and /")
		exit(1)
