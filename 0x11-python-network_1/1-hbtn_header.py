#!/usr/bin/python3
"""Sends a request and displays the value of X-Request-Id
variable found in the header of the response"""

if __name__ == '__main__':
    from sys import argv
    from urllib.request import urlopen

    with urlopen(argv[1]) as response:
        pass

    print(response.headers.get('X-Request-Id'))
