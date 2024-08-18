#!/usr/bin/python3
"""Returns Employee Information from an API service"""

import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    api_url_UserName = f'https://jsonplaceholder.typicode.com/users/{id}'
    UserName_res = requests.get(api_url_UserName).json()

    api_todosURL = f'{api_url_UserName}/todos'
    
    user_todo = requests.get(api_todosURL).json()

    empName = UserName_res.get('name')
    Total_task = 0
    completed = 0

    for val in user_todo:
        Total_task += 1
        if val.get('completed'):
            completed += 1

    print(
            f'Employee {empName} is done with tasks({completed}/{Total_task}):')
    [print(f"\t {val.get('title')}") for val in user_todo]
