#!/usr/bin/python3
""" POST an email #1 """

if __name__ == "__main__":
    
    import requests
    import sys

    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
