#!/usr/bin/python3
for i in range(97, 123):
        if ord(str(i)) == "q" or ord(str(i)) == "e":
                continue
        print("{}".format(chr(i)), end="")
