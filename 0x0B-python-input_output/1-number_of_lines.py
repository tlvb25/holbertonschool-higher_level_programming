#!/usr/bin/python3
'''
    contains method number_of_lines
'''


def number_of_lines(filename=""):
    '''
        returns num of lines in textfile
    '''
    lineNum = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            lineNum += 1
        return(lineNum)
