import json
import os
from enum import Enum

filepath = "todo.json"
class UserAction(Enum):
    ADD = "add"
    SHOW = "show"
    EDIT = "edit"
    COMPLETE = "complete"
    QUIT = "quit"


def initialize():
    todos = []
    # if file does not exist, create a new empty file
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            json.dump(todos, f)
    # file exist so load it
    else:
        with open(filepath, 'r') as f:
            todos = json.load(f)
    return todos

def save_todos(todos):
    with open(filepath, 'w') as f:
        json.dump(todos, f)

def check_range(index, length):
    if index < 0 or index >= length:
        print("Index out-of-range. Please try again.")
        return False
    else:
        return True

def main():
    todos = initialize()

    while True:
        user_action = input("Enter command or 'help': ").strip().lower()
        if 'add' in user_action:
                todos.append(user_action[4:])
                save_todos(todos)
                print(f"\"{user_action[4:].title()}\" added to the ToDo list.")
        elif 'show' in user_action:
                for index, todo in enumerate(todos):
                    print(f"{index + 1}. {todo.title()}")
        elif 'edit' in user_action:
                user_action = user_action[5:]
                tokens = user_action.split()
                index = int(tokens[0])
                todo = " ".join(tokens[1:])
                if check_range(index - 1, len(todos)):
                    old_todo = todos[index - 1]
                    todos[index - 1] = todo
                    save_todos(todos)
                    print(f"Todo #{index} changed from {old_todo.title()} to {todos[index - 1].title()}.")
        elif 'complete' in user_action:
                index = int(input("Enter ToDo to complete : "))
                if check_range(index - 1, len(todos)):
                    todos.pop(index - 1)
                    save_todos(todos)
                    print(f"Todo #{index} complete.")
        elif 'quit' in user_action:
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
