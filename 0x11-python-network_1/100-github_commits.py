#!/usr/bin/python3
""" Time for an interview!  """

if __name__ == "__main__":

    import requests
    import sys

    response = requests.get("https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]))
    if response.status_code != 200:
        print("None")
    else:
        data = response.json()
        for t in data[0:10]:
            print("{}: {}".format(t.get('sha'),
                                  t.get('commit').get('author').get('name')))
