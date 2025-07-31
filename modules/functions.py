import json
import os
import sys

filepath = "daata/todos_modos.json"

def initialize(fp = filepath):
    """ if data file exists, load todos, if not create a new empty file """
    todos = []
    if not os.path.exists(fp):
       write_todos(todos)
    else:
       todos = read_todos(fp)
    return todos

def write_todos(todos, fp = filepath):
    """ save todos in 'todos_modos.json' """
    try:
        with open(filepath, 'w') as f:
            json.dump(todos, f)
    except FileNotFoundError:
        print(f"Error: {fp} was not found.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access {fp}.", file=sys.stderr)
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: {fp} points to a directory, not a file.", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"An unexpected OS error occurred: {e}", file=sys.stderr)
        sys.exit(1)

def read_todos(fp = filepath) -> list:
    try:
        with open(filepath, 'r') as f:
            todos = json.load(f)
    except FileNotFoundError:
            print(f"Error: {fp} was not found.", file=sys.stderr)
            sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access {fp}.", file=sys.stderr)
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: {fp} points to a directory, not a file.", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"An unexpected OS error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    return todos

def check_range(index, length) -> bool:
    """ check if index is between 0 and length """
    if index < 0 or index >= length:
        return False
    else:
        return True

def add(tokens, todos) -> bool:
    """ add todos - throws ValueError if adding fails """
    if len(tokens) < 2:
        raise ValueError("Usage: (a)dd <todo>")
    todo = " ".join(tokens[1:])
    todos.append(todo)
    write_todos(todos)
    return True

def edit(tokens, todos) -> str:
    """ edit todos """
    usage = "Usage: (e)dit <todo #> <new todo>"
    if len(tokens) < 3:
        raise ValueError(usage)
    try:
        index = int(tokens[1])
    except ValueError:
        raise ValueError(usage)
    todo = " ".join(tokens[2:])
    if check_range(index - 1, len(todos)):
        old_todo = todos[index - 1]
        todos[index - 1] = todo
        write_todos(todos)
        return f"Todo #{index} changed from \"{old_todo.title()}\" to \"{todos[index - 1].title()}\"."
    else:
        raise ValueError(f"Todo #{index} not found.")

def insert(tokens, todos) -> str:
    """ insert new todo """
    usage = "Usage: (i)nsert <after todo #> <new todo>"
    if len(tokens) < 3:
        raise ValueError(usage)
    try:
        index = int(tokens[1])
    except ValueError:
        raise ValueError(usage)
    todo = " ".join(tokens[2:])
    if check_range(index - 1, len(todos) - 1):
        previous_todo = todos[index - 1]
        next_todo = todos[index]
        todos.insert(index, todo)
        write_todos(todos)
        return f"\"{todo}\" inserted between \"{previous_todo.title()}\" and \"{next_todo.title()}\"."
    else:
        raise ValueError(f"Todo #{index} not found.")

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
        write_todos(todos)
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

def display_help() -> str:
    """ display help """
    return  """
Available commands:
(a)dd todo
(c)omplete todo_number
(e)dit todo_number new_todo
(h)elp: show this menu
(i)nsert after_todo new_todo
(q)uit: end this program
(s)how: show all todo's
            """
