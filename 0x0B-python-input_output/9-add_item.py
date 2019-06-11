#!/usr/bin/python3

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

def add_item(args="", filename=""):
    try:
        all_args = load_from_json_file(filename)
    except:
        all_args = []

    for arguments in args:
        all_args.append(arguments)
    save_to_json_file(all_args, filename)

    if __name__ == "__main__":
        args = sys.argv[1:]
        filename = "add_item.json"
        add_item(args, filename)
