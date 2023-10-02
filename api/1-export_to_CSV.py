#!/usr/bin/python3
"""
This script retrieves TODO list data for a given employee ID using the JSONPlaceholder REST API
and exports it to a CSV file.
"""

import csv
import requests
import sys

def export_employee_todo_to_csv(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        employee_name = user_data.get('name')

        # Creating a CSV file with the user's ID as the filename
        csv_file_name = f'{employee_id}.csv'
        with open(csv_file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

            for task in todos_data:
                task_completed_status = 'Yes' if task.get('completed') else 'No'
                csv_writer.writerow([employee_id, employee_name, task_completed_status, task.get('title')])

        print(f'Data has been exported to {csv_file_name}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 1-export_to_CSV.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_employee_todo_to_csv(employee_id)
