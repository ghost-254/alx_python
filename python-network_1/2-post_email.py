#!/usr/bin/python3
"""
Module: 2-post_email.py
"""
import requests
import sys

def post_email(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter and displays the response body
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
