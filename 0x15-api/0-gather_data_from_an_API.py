#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""

import requests
from sys import argv


def gather_from_api():
    """
    This gets the info about the todo progress
    """
    employeeId = int(argv[1])
    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        employeeId)
    userUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employeeId)
    res = requests.get(userUrl)
    if res.status_code == 200:
        users = res.json()
        userName = users['name']

    # todoUrl = f'{url}/?userId={employeeId}'
    res = requests.get(url)
    if res.status_code == 200:
        todo = list(res.json())
        no_of_tasks = len(todo)
        completed_task = [x for x in todo if x.get('completed')]
        done_task = len(completed_task)
        print(
            "Employee {} is done with tasks({}/{}):".format(
                userName,
                done_task,
                no_of_tasks
            )
        )
        for x in completed_task:
            print("\t {}".format(x.get('title')))

if __name__ == '__main__':
    gather_from_api()
