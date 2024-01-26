#!/usr/bin/python3
"""Uses the requests package to fetch a url"""

if __name__ == '__main__':
    import requests

    response = requests.get("https://alx-intranet.hbtn.io/status")
    response.raise_for_status()

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
