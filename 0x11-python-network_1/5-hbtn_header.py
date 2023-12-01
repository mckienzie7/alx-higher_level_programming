#!/usr/bin/python3
"""Using requests module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    header = request.headers.get('X-Request-Id')
    print(header)
