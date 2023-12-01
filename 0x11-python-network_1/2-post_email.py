#!/usr/bin/python3
"""REquesthttp"""
import sys
import urllib.parse
from urllib.request import urlopen, Request


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        value = {"email": sys.argv[2]}
        data = urllib.parse.urlencode(value)
        data = data.encode('ascii')
        req = Request(url, data)
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except IndexError:
        pass
