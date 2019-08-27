#!/usr/bin/python3
""" Error code #1 """
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print('Error code:', response.status_code)
