#!/usr/bin/python3
if __name__ == '__main__':
        from sys import argv
        from add_0 import add

        args = len(argv)
        sum = 0

        if args == 1:
                print("{:d}".format(sum))
        else:
                print("{:d} arguments:".format(args -1))
                for i in range(1, args):
                        sum += int(argv[i])
                        print("{:d}".format(sum))
