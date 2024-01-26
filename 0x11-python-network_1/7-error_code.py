#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the
body of the response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    res = requests.get(argv[1])

    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
