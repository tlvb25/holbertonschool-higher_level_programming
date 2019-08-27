#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
        print(response)
