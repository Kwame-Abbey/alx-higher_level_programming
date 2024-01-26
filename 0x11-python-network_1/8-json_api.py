#!/usr/bin/python3
"""Defines a json"""


if __name__ == '__main__':
    import requests
    from sys import argv

    val = argv[1] if len(argv) > 1 else ""
    payload = {'q': val}
    endpoint = 'http://0.0.0.0:5000/search_user'

    try:
        res = requests.post(endpoint, data=payload)
        data = res.json()
        if 'id' in data and 'name' in data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
