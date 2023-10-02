#!/usr/bin/env python3
"""
Exports data to CSV
"""

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        employee_name = user_data.get('name')
        user_id = user_data.get('id')

        # Defining the CSV file name based on the user ID
        csv_file_name = f'{user_id}.csv'

        # Creating and opening the CSV file for writing
        with open(csv_file_name, 'w', newline='') as csvfile:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Writing the header row
            writer.writeheader()

            for task in todos_data:
                # Checking if the task is completed
                task_completed = 'True' if task.get('completed') else 'False'

                # Writing task data to the CSV file
                writer.writerow({
                    'USER_ID': user_id,
                    'USERNAME': employee_name,
                    'TASK_COMPLETED_STATUS': task_completed,
                    'TASK_TITLE': task.get('title')
                })

        print(f'Data exported to {csv_file_name}')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 1-export_to_CSV.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
