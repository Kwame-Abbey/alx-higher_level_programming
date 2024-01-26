#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the
body of the response
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    payload = {'email': argv[2]}
    endpoint = argv[1]

    res = requests.post(endpoint, data=payload)
    res.raise_for_status()
    print(res.text)
