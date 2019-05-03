#!/usr/bin/python3
if __name__ == '__main__':
        from sys import *
        args = len(argv)
        if args == 1:
                print("{:d} arguments.".format(args - 1))
        elif args == 2:
                print("{:d} argument:".format(args - 1))
                print("{:d}: {:s}".format(args - 1, argv[1]))
        else:
                print("{:d} arguments:".format(args - 1))
                for i in range(1, args):
                        print("{:d}: {:s}".format(i, argv[i]))
