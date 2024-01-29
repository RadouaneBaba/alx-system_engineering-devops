#!/usr/bin/python3
""" export data in the CSV form """
import csv
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

    with open(f"{sys.argv[1]}.csv", mode="w") as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            if todo.get('userId') == int(sys.argv[1]):
                row = [sys.argv[1],
                       name,
                       todo.get('completed'),
                       todo.get('title')]
                writer.writerow(row)
