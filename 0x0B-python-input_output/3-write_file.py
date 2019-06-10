#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as a_file:
        char_count = a_file.write(text)
        return char_count
