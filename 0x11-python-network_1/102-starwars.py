#!/usr/bin/python3
""" Star Wars API #2 """
from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get('https://swapi.co/api/people/?search={}'
                            .format(argv[1]))
    j = response.json()
    l = j.get('results')
    print('Number of results:', j.get('count'))
    while j.get('next') is not None:
        response = requests.get(j.get('next'))
        j = response.json()
        l += j.get('results')
    for i in l:
        print(i.get('name'))
        for a in i.get('films'):
            film = requests.get(a)
            print('\t{}'.format(film.json().get('title')))
