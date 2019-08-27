#!/usr/bin/python3
""" Response header value #1 """
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
