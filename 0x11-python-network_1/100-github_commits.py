#!/usr/bin/python3
"""Time for an interview!"""
from sys import argv
import requests


if __name__ == "__main__":
    resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    l = resp.json()
    try:
        for i in range(10):
            print(l[i].get('sha'), l[i].get('commit')
                  .get('author').get('name'), sep=": ")
    except:
        pass
