#!/usr/bin/python3
""" Response header value #0 """

if __name__ == "__main__":

    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as r:
        print(dict(r.info()).get('X-Request-Id'))
