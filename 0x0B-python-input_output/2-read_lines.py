#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, mode='r', encoding='utf-8') as a_file:
        if (nb_lines <= 0):
            print(a_file.read(), end="")
        else:
            for line in a_file:
                print(line, end="")
                nb_lines -= 1
