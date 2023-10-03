#!/usr/bin/env python3
"""
Exporting tasks data to CSV
"""

import csv
import requests
import sys

def export_employee_tasks_to_csv(employee_id):
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
        user_id = user_data.get('id')
        username = user_data.get('username')

        # Defining the CSV file name based on the user ID
        csv_file_name = f'{user_id}.csv'

        # Preparing CSV data
        csv_data = []
        for task in todos_data:
            task_completed = task['completed']
            task_title = task['title']
            csv_data.append([user_id, username, str(task_completed), task_title])

        # Writing CSV data to file
        with open(csv_file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

        print(f'Data exported to {csv_file_name}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 export_to_CSV.py <employee_id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_employee_tasks_to_csv(employee_id)
    except ValueError:
        print('Error: Invalid employee ID. Please provide a valid integer.')
        sys.exit(1)
