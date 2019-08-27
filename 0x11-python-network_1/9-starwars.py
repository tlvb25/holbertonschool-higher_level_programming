#!/usr/bin/python3
""" Star Wars API #0 """
from sys import argv
import requests


if __name__ == "__main__":

    import requests
    import sys

    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    response = requests.get(url)
    data = response.json()
    if data:
        print("Number of results: {}".format(data.get('count')))
        for dic in data.get('results'):
            print(dic.get('name'))
