#!/usr/bin/python3
import json

def load_from_json_file(filename=""):
    '''
        contains function that creates an Object from a “JSON file”
    '''
    with open(filename, mode='r', encoding='utf-8') as f:
        json.load(f)
