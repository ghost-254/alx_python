#!/usr/bin/python3
"""
Module: 0-gather_data_from_an_API
"""
import requests

def fetch_status():
    """
    Fetches and displays the status from https://alu-intranet.hbtn.io/status
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

if __name__ == "__main__":
    fetch_status()
