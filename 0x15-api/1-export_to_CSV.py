#!/usr/bin/python3
""" Requests and displays todos of a user """
from requests import get
from sys import argv
from csv import writer, QUOTE_ALL

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
        return list(map(lambda item: [
            str(user_id),
            name,
            str(item.get('completed')),
            item.get('title')
        ], user_todos))

    try:
        with open(f'{user_id}.csv', 'w', newline='') as file:
            csv_file = writer(file, quoting=QUOTE_ALL)
            csv_file.writerows(get_todo(user_id))
    except Exception:
        pass

    get_todo(user_id)
