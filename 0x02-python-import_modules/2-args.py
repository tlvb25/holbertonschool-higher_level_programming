#!/usr/bin/python3
if __name__ == '__main__':
        import sys

        args = len(sys.argv)

        if args == 1:
                print("0 arguments.")
        elif args > 1:
                print("{:d} arguments:".format(args))
                for i in range(args):
                        print("{:d} {:s}".format(i, args[i]))
