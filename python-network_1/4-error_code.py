#!/usr/bin/python3
"""
Module: 4-error_code.py
"""
import requests
import sys

def fetch_and_display(url):
    """
    Fetches and displays the response body and handles error codes if >= 400
    """
    response = requests.get(url)
    print(response.text)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display(url)
