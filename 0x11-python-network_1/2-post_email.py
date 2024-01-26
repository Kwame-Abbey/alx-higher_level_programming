#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

if __name__ == '__main__':
    from sys import argv
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode

    email = {"email": argv[2]}
    data = urlencode(email)
    post_data = data.encode('utf-8')
    req = Request(argv[1], data=post_data)

    with urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
