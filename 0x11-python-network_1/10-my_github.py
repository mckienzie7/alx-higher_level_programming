#!/usr/bin/python3
"""Using requests module"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    passwd = sys.argv[2]
    request = requests.get(url, auth=(username, passwd))
    my_id = request.json().get('id')
    print(my_id)
