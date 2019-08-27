#!/usr/bin/python3
"""Star Wars API #1"""
from sys import argv
import requests


if __name__ == "__main__":
    respnse = requests.get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    j = respnse.json()
    l = j.get('results')
    print('Number of results:', j.get('count'))
    while j.get('next') is not None:
        r = requests.get(j.get('next'))
        j = r.json()
        l += j.get('results')
    for i in l:
        print(i.get('name'))
