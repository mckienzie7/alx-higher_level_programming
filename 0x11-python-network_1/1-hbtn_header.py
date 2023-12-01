#!/usr/bin/python3
"""request a url"""
import sys
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    with urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
