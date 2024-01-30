#!/usr/bin/python3
""" export data to json """
import json
import requests

if __name__ == '__main__':
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    res2 = requests.get('https://jsonplaceholder.typicode.com/users')
    users = res2.json()
    todos = res.json()
    j_dict = {}

    for user in users:
        j_dict[user.get('id')] = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                todo_dict = {
                        "username": user.get('username'),
                        "task": todo.get('title'),
                        "completed": todo.get('completed')
                        }
                j_dict[user.get('id')].append(todo_dict)

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(j_dict, outfile)
