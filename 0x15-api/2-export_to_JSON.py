#!/usr/bin/python3
""" Requests and displays todos of a user """
from requests import get
from sys import argv
from json import dump

if __name__ == "__main__":
    user_id = int(argv[1])

    def get_user(id):
        """ Gets th username """
        res = get(f'https://jsonplaceholder.typicode.com/users/{id}')
        return res.json().get('username')

    def get_todo(id):
        """ Returns data from todo response """
        res = get('https://jsonplaceholder.typicode.com/todos')
        user_todos = list(filter(lambda todo: todo.get('userId') == id,
                                 res.json()))
        name = get_user(user_id)
        return {user_id: list(map(lambda item: {
            'task': item.get('title'),
            'completed': item.get('completed'),
            'username': get_user(user_id)
        }, user_todos))}

    try:
        with open(f'{user_id}.json', 'w') as file:
            dump(get_todo(user_id), file)
    except Exception:
        pass
    get_todo(user_id)
