#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # fetches todo list data
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    # Displays the result
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks, total_tasks
        )
    )
    for task in todo_data:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
