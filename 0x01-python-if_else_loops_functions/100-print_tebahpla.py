#!/usr/bin/python3
for alpha in range(ord('z'), ord('`'), -1):
        if alpha % 2 == 1:
                print("{}".format(chr(alpha - 32)), end='')
        else:
                print("{}".format(chr(alpha)), end='')
