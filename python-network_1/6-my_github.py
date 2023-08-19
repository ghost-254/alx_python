#!/usr/bin/python3
"""
Module: 6-my_github.py
"""
import requests
import sys

def get_github_id(username, token):
    """
    Uses GitHub API with Basic Authentication to display the user's id
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        user_data = response.json()
        print("GitHub user ID:", user_data['id'])
    else:
        print("Failed to fetch GitHub data. Status code:", response.status_code)

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)
