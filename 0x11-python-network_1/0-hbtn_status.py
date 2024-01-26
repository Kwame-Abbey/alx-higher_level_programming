#!/usr/bin/python3
"""Uses the package urllib to fetch a url"""

if __name__ == '__main__':
    from urllib.request import urlopen

    endpoint = 'https://alx-intranet.hbtn.io/status'
    with urlopen(endpoint) as response:
        body = response.read()

    print(f"Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
