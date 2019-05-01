#!/usr/bin/python3
for i in range(97, 123):
        if ord(chr(i)) == ord("q") or ord(chr(i)) == ord("e"):
                continue
        print("{}".format(chr(i)), end="")