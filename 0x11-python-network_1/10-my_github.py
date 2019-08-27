#!/usr/bin/python3
""" My Github! """
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
                                auth=(argv[1], argv[2]))
    if response.status_code == 200:
        j = response.json()
        print(j.get('id'))
    else:
        print('None')
