#!/usr/bin/python3
if __name__ == '__main__':
        import sys

        args = len(sys.argv)

        if args == 1:
                print("{:d} arguments.".format(args - 1))
        elif args == 2:
                print("{:d} argument:".format(args - 1))
                print("{:d}: {:s}".format(args - 1, sys.argv[2]))
        else:
                print("{:d} arguments:".format(args))
                for i in range(1, args):
                        print("{:d} {:s}".format(i, sys.argv[i]))
