#!/usr/bin/python3
""" Requests and displays todos of a user """
from requests import get
from json import dump

if __name__ == "__main__":
    def get_users():
        """ Gets th username """
        res = get(f'https://jsonplaceholder.typicode.com/users')
        return res.json()

    def get_todo():
        """ Returns data from todo response """
        res = get('https://jsonplaceholder.typicode.com/todos')
        all_todo = {}
        for user in get_users():
            user_todos = list(filter(
                lambda todo: todo.get('userId') == user.get('id'),
                res.json()))

            all_todo[user.get('id')] = list(map(lambda item: {
                'task': item.get('title'),
                'completed': item.get('completed'),
                'username': user.get('username')
            }, user_todos))

        return all_todo

    try:
        with open('todo_all_employees.json', 'w') as file:
            dump(get_todo(), file)
    except Exception:
        pass
    get_todo()
