#!/usr/bin/python3
"""
This Script gathers data from an API.
"""
import requests
import sys


if __name__ == "__main__":
    employeeID = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employeeID}"
    todos = f"https://jsonplaceholder.typicode.com/users/{employeeID}/todos"
    user = requests.get(url).json()
    username = user.get("name")
    tasks = requests.get(todos).json()
    completed = [todo.get("title") for todo in tasks if todo.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        username, len(completed), len(tasks)))
    for task in completed:
        print(f"\t {task}")
