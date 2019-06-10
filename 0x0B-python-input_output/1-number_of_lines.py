#!/usr/bin/python3
'''
    contains method number_of_lines
'''


def number_of_lines(filename=""):
    '''
        returns num of lines in textfile
    '''
    line_num = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            line_num += 1
        return(line_num)
