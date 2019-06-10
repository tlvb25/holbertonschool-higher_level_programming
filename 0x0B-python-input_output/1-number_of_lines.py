#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        line_num = 0
        for l in f:
            line_num +=1
        return line_num
