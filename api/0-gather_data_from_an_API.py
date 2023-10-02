#!/usr/bin/env python3
"""
Gathering data from the API
"""

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
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task.get('completed'))

        print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')
        
        for task in todos_data:
            if task.get('completed'):
                print(f'\t{task.get("title")} \n')

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 0-gather_data_from_an_API.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
