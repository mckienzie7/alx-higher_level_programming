#!/usr/bin/python3
"""Using requests module"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    status_code = request.status_code
    if int(status_code) >= 400:
        print(f"Error code: {status_code}")
    else:
        print(request.text)
