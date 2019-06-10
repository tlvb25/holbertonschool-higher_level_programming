#!/usr/bin/python3
'''
    contains method number_of_lines
'''

def number_of_lines(filename=""):
    '''
        returns num of lines in textfile
    '''
    with open(filename, mode='r', encoding='utf-8') as a_file:
        line_num = 0
        for l in a_file:
            line_num +=1
        return (line_num)
