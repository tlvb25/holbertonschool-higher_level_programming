#!/usr/bin/python3
""" Error code #0 """
import urllib.requests
import urllib.parse
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except urllib.error.HTTPError as error:
        print('Error code:', error.code)
