#!/usr/bin/python3
"""
This Script fetches data from an API and exports to a json file
"""
import json
import requests
import sys


if __name__ == "__main__":
    employeeID = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employeeID}"
    todos = f"https://jsonplaceholder.typicode.com/users/{employeeID}/todos"
    user = requests.get(url).json()
    username = user.get("name")
    tasks = requests.get(todos).json()

    with open(f"{employeeID}.json", 'w') as jsonfile:
        json.dump({employeeID: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in tasks]}, jsonfile)
