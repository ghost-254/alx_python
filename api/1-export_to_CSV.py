#!/usr/bin/python3
"""
This script retrieves TODO list data for a given employee ID using the JSONPlaceholder REST API
and exports it to a CSV file.
"""

import csv
import requests
import sys

def gather_data(employee_id):
    """
    Retrieve TODO list data for the given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetchich employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Fetching TODO list for the employee
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_list = todo_response.json()

    # Exporting TODO list data to a CSV file
    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in todo_list:
            csv_writer.writerow([user_id, username, task.get("completed"), task.get("title")])

    print(f"Data has been exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)
