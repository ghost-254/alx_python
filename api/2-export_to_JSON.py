#!/usr/bin/env python3
"""
Export tasks data to JSON format
"""

import json
import requests
import sys

def export_employee_tasks_to_json(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Sending requests to get user and tasks data
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        # Checking response status codes
        if user_response.status_code != 200 or todos_response.status_code != 200:
            print(f'Error: Failed to retrieve data for employee {employee_id}')
            sys.exit(1)

        user_data = user_response.json()
        todos_data = todos_response.json()

        # Extracting user information
        employee_id= user_data.get('id')
        username = user_data.get('username')

        # Preparing data for JSON export
        json_data = {
            str(employee_id): [
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": username
                }
                for task in todos_data
            ]
        }

        # Writing JSON data to file
        json_file_name = f"{employee_id}.json"
        with open(json_file_name, mode='w') as json_file:
            json.dump(json_data, json_file)

        print(f'Data exported to {json_file_name}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 2-export_to_JSON.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_employee_tasks_to_json(employee_id)
    except ValueError:
        print('Error: Invalid employee ID. Please provide a valid integer.')
        sys.exit(1)
