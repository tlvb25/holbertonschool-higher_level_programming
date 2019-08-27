#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
            auth=(argv[1], argv[2]))
    if response.status_code == 200:
        j = response.json()
        print(j.get('id'))
    else:
        print('None')
