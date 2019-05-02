#!/usr/bin/python3
def uppercase(str):
        upper_str = ''
        for c in str:
                if ord(c) >= 65:
                        upper_str += chr(ord(c) - 32)
                else:
                        upper_str = c
        print("{:c}".format(upper_str), end="")
        print('')
