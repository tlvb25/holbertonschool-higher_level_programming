#!/usr/bin/python3
""" Response header value #1 """
from sys import argv
import request


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
