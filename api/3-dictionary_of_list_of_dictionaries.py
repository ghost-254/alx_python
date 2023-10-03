#!/usr/bin/env python3
"""
Gathering data from the API and exporting to JSON
"""

import json
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

        employee_name = user_data.get('username')
        
        # Creating a dictionary to store tasks for the user
        user_tasks = {
            "username": employee_name,
            "tasks": []
        }
        
        for task in todos_data:
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            user_tasks["tasks"].append(task_dict)

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

if __name__ == '__main__':
    all_employee_tasks = {}

    for employee_id in range(1, 11):  # Assuming there are 10 employees, you can adjust this range accordingly
        result = get_employee_todo_progress(employee_id)
        if result:
            employee_id, user_tasks = result
            all_employee_tasks[str(employee_id)] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employee_tasks, json_file)
