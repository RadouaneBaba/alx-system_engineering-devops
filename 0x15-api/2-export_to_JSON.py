#!/usr/bin/python3
""" export data in the Json format """
import json
import requests
import sys

if __name__ == '__main__':
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    res2 = requests.get('https://jsonplaceholder.typicode.com/users')
    users = res2.json()
    todos = res.json()
    name = None

    for user in users:
        if user.get('id') == int(sys.argv[1]):
            name = user.get('username')
            break

    with open(f"{sys.argv[1]}.json", mode="w") as outfile:
        todo_list = []
        for todo in todos:
            if todo.get('userId') == int(sys.argv[1]):
                todo_dict = {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": name
                    }
                todo_list.append(todo_dict)
        json.dump({sys.argv[1]: todo_list}, outfile)
