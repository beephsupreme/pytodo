import json
import os

filepath = "todo.json"

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
        tokens = user_action.split()
        command = tokens[0]

        match command:
            case 'add' | 'a':
                if len(tokens) < 2:
                    print("Usage: (a)dd todo#")
                    continue
                todo = " ".join(tokens[1:])
                todos.append(todo)
                save_todos(todos)
                print(f"\"{todo.title()}\" added to the ToDo list.")
            case 'show' | 's':
                if len(todos) == 0:
                    print("The ToDo list is empty.")
                    continue
                print()
                for index, todo in enumerate(todos):
                    print(f"{index + 1}. {todo.title()}")
                print()
            case 'edit' | 'e':
                if len(tokens) < 3:
                    print("Usage: (e)dit todo# new_todo")
                    continue
                try:
                    index = int(tokens[1])
                except ValueError:
                    print("Usage: (e)dit todo# new_todo")
                    continue
                todo = " ".join(tokens[2:])
                if check_range(index - 1, len(todos)):
                    old_todo = todos[index - 1]
                    todos[index - 1] = todo
                    save_todos(todos)
                    print(f"Todo #{index} changed from \"{old_todo.title()}\" to \"{todos[index - 1].title()}\".")
            case 'complete' | 'c':
                if len(tokens) < 2:
                    print("Usage: (c)omplete todo#")
                    continue
                try:
                    index = int(tokens[1])
                except ValueError:
                    print("Usage: (c)omplete todo#")
                    continue
                if check_range(index - 1, len(todos)):
                    todo = todos[index - 1]
                    todos.pop(index - 1)
                    save_todos(todos)
                    print(f"\"#{index}. {todo.title()}\" has been removed from the ToDo list.")
            case 'help' | 'h':
                print(
                """
                Available commands:
                (a)dd todo
                (s)how
                (e)dit todo_number new_todo
                (c)omplete todo_number
                (h)elp: show this menu
                (q)uit: end this program
                """)
            case 'quit' | 'q':
                break
            case _:
                print("Invalid command. Please try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
