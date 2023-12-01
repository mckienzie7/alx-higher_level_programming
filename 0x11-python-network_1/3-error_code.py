#!/usr/bin/python3
"""REquesthttp"""
import sys
from urllib.error import HTTPError
import urllib.parse
from urllib.request import urlopen, Request


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        req = Request(url)
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
