#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    fine_token = argv[2]
    github_endpoint = 'https://api.github.com/user'
    username = argv[1]

    res = requests.get(github_endpoint, auth=(username, fine_token))
    data = res.json()
    print(data.get('id'))
