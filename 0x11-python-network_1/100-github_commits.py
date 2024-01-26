#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge"""

if __name__ == '__main__':
    import requests
    from sys import argv

    endpoint = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"

    res = requests.get(endpoint)
    data = res.json()
    try:
        for i in range(10):
            print(f"{data[i].get('sha')}: "
                  f"{data[i].get('commit').get('author').get('name')}")
    except IndexError:
        pass
