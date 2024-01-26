#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    res = requests.get(argv[1])
    res.raise_for_status()

    print(res.headers.get('X-Request-Id'))
