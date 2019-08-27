#!/usr/bin/python3
""" Search API """
from sys import argv
import requests


if __name__ == "__main__":
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})
        j = response.json()
        if j:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
