#!/usr/bin/python3
""" state of todolist for x employee """
import requests
import sys

if __name__ == '__main__':
    res = requests.get('https://jsonplaceholder.typicode.com/todos')
    res2 = requests.get('https://jsonplaceholder.typicode.com/users')
    users = res2.json()
    todos = res.json()
    total = 0
    completed = 0
    name = ''

    for user in users:
        if user.get('id') == int(sys.argv[1]):
            name = user.get('name')
    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]):
            total += 1
            if todo.get('completed'):
                completed += 1

    print(f'Employee {name} is done with tasks({completed}/{total}):')

    for todo in todos:
        if todo.get('userId') == int(sys.argv[1]) and todo.get('completed'):
            print(f"\t {todo.get('title')}")
