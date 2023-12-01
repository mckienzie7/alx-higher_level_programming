#!/usr/bin/python3
"""Using requests module"""
import requests
import sys


if __name__ == "__main__":
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    request = requests.get(url)
    commits = request.json()
    try:
        for i in range(0, 10):
            sha = commits[i].get('sha')
            name = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {name}")
    except (IndexError, KeyError):
        pass
