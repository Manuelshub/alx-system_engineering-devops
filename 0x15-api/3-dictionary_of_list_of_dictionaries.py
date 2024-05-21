#!/usr/bin/python3
"""
This Script fetches data from an API and exports to a json file
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    todos = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(url).json()

    dixt = {}
    for user in users:
        dixt[user.get("id")] = []
        for todo in requests.get(todos).json():
            if todo.get("userId") == user.get("id"):
                dixt[user.get("id")].append({
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(dixt, jsonfile)
