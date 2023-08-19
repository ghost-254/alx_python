#!/usr/bin/python3
"""
Module: 1-hbtn_header.py
"""
import requests
import sys

def get_request_id(url):
    """
    Sends a request to the given URL and displays the value of X-Request-Id header
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)

if __name__ == "__main__":
    url = sys.argv[1]
    get_request_id(url)
