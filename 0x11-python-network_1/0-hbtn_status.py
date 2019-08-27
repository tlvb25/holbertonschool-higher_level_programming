#!/usr/bin/python3
import urllib.request
"""urlib.request usage"""

if __name__ == "__main__":
    with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('t- content: {}'.format(html))
        print('t- utf8 content'.format(html.decode(utf-8)))
