#!/usr/bin/python3
""" Requests and displays todos of a user """
from requests import get
from sys import argv

user_id = int(argv[1])


def get_user(id):
    """ Gets th username """
    res = get(f'https://jsonplaceholder.typicode.com/users/{id}')
    return res.json().get('name')


def get_todo(id):
    """ Returns data from todo response """
    res = get('https://jsonplaceholder.typicode.com/todos')
    user_todos = list(filter(lambda todo: todo['userId'] == id, res.json()))
    completed = list(filter(lambda todo: todo['completed'] is True,
                            user_todos))
    return {
        'len_comp': len(completed),
        'completed': completed,
        'len_all': len(user_todos)
    }


print(f"Employee {get_user(user_id)} is done with \
({get_todo(user_id)['len_comp']}/{get_todo(user_id)['len_all']}):")

for todo in get_todo(user_id)['completed']:
    print(f"\t {todo['title']}")
