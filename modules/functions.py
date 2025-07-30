import json
import os

filepath = "../todo.json"

def initialize():
    """ if data file exists, load todos, if not create a new empty file """
    todos = []
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            json.dump(todos, f)
    else:
        with open(filepath, 'r') as f:
            todos = json.load(f)
    return todos

def save_todos(todos):
    """ save todos in 'todo.json' """
    with open(filepath, 'w') as f:
        json.dump(todos, f)

def check_range(index, length):
    """ check if index is between 0 and length """
    if index < 0 or index >= length:
        print("\nIndex out-of-range. Please try again.\n")
        return False
    else:
        return True

def add(tokens, todos):
    """ add todos """
    if len(tokens) < 2:
        print("\nUsage: (a)dd todo#\n")
        return
    todo = " ".join(tokens[1:])
    todos.append(todo)
    save_todos(todos)
    print(f"\n\"{todo.title()}\" added to the todo list.\n")

def edit(tokens, todos):
    """ edit todos """
    if len(tokens) < 3:
        print("\nUsage: (e)dit todo# new_todo\n")
        return
    try:
        index = int(tokens[1])
    except ValueError:
        print("\nUsage: (e)dit todo# new_todo\n")
        return
    todo = " ".join(tokens[2:])
    if check_range(index - 1, len(todos)):
        old_todo = todos[index - 1]
        todos[index - 1] = todo
        save_todos(todos)
        print(f"\nTodo #{index} changed from \"{old_todo.title()}\" to \"{todos[index - 1].title()}\".\n")

def insert(tokens, todos):
    """ insert new todo """
    if len(tokens) < 3:
        print("\nUsage: (i)nsert after_todo# new_todo\n")
        return
    try:
        index = int(tokens[1])
    except ValueError:
        print("\nUsage: (i)nsert after_todo# new_todo\n")
        return
    todo = " ".join(tokens[2:])
    if check_range(index - 1, len(todos) - 1):
        previous_todo = todos[index - 1]
        next_todo = todos[index]
        todos.insert(index, todo)
        save_todos(todos)
        print(f"\n\"{todo}\" inserted between \"{previous_todo.title()}\" and \"{next_todo.title()}\".\n")

def complete(tokens, todos):
    """ complete todos """
    if len(tokens) < 2:
        print("\nUsage: (c)omplete todo#\n")
        return
    try:
        index = int(tokens[1])
    except ValueError:
        print("\nUsage: (c)omplete todo#\n")
        return
    if check_range(index - 1, len(todos)):
        todo = todos[index - 1]
        todos.pop(index - 1)
        save_todos(todos)
        print(f"\n\"#{index}. {todo.title()}\" has been removed from the ToDo list.\n")

def display_todos(todos):
    """ display todos """
    if len(todos) == 0:
        print("\nThe todo list is empty.\n")
        return
    print()
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo.title()}")
    print()

def display_help():
    """ display help """
    print(
        """
Available commands:
(a)dd todo
(c)omplete todo_number
(e)dit todo_number new_todo
(h)elp: show this menu
(i)nsert after_todo new_todo
(q)uit: end this program
(s)how: show all todo's
        """)
