#!/usr/bin/python3
"""
Module: 5-json_api.py
"""
import requests
import sys

def search_user(letter):
    """
    Sends a POST request to the specified URL with the letter as a parameter and processes the response
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, data=payload)
    
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)
