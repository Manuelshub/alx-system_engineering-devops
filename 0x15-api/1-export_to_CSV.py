#!/usr/bin/python3
"""
This Script fetches data from an API and exports to a csv file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employeeID = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employeeID}"
    todos = f"https://jsonplaceholder.typicode.com/users/{employeeID}/todos"
    user = requests.get(url).json()
    username = user.get("name")
    tasks = requests.get(todos).json()

    with open(f"{employeeID}.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in tasks:
            writer.writerow(
                [todo.get("userId"),
                 user.get("username"), todo.get("completed"),
                 todo.get("title")])
