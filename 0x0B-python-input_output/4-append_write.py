#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        appened_file = f.write(text)
        return appened_file
