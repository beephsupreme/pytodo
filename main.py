import json
import os

filepath = "todo.json"

def initialize():
    todos = []
    # if file does not exist, create a new empty file
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            json.dump(todos, f)
    # file exists so load it
    else:
        with open(filepath, 'r') as f:
            todos = json.load(f)
    return todos

def save_todos(todos):
    with open(filepath, 'w') as f:
        json.dump(todos, f)

def check_range(index, length):
    if index < 0 or index >= length:
        print("\nIndex out-of-range. Please try again.\n")
        return False
    else:
        return True

def main():
    todos = initialize()
    print("\nWelcome to the TodosModos 1.0!\n")
    while True:
        user_action = input("Enter command or 'help': ").strip().lower()
        tokens = user_action.split()
        command = tokens[0]

        match command:
            case 'add' | 'a':
                if len(tokens) < 2:
                    print("\nUsage: (a)dd todo#\n")
                    continue
                todo = " ".join(tokens[1:])
                todos.append(todo)
                save_todos(todos)
                print(f"\n\"{todo.title()}\" added to the todo list.\n")
            case 'show' | 's':
                if len(todos) == 0:
                    print("\nThe todo list is empty.\n")
                    continue
                print()
                for index, todo in enumerate(todos):
                    print(f"{index + 1}. {todo.title()}")
                print()
            case 'edit' | 'e':
                if len(tokens) < 3:
                    print("\nUsage: (e)dit todo# new_todo\n")
                    continue
                try:
                    index = int(tokens[1])
                except ValueError:
                    print("\nUsage: (e)dit todo# new_todo\n")
                    continue
                todo = " ".join(tokens[2:])
                if check_range(index - 1, len(todos)):
                    old_todo = todos[index - 1]
                    todos[index - 1] = todo
                    save_todos(todos)
                    print(f"\nTodo #{index} changed from \"{old_todo.title()}\" to \"{todos[index - 1].title()}\".\n")
            case 'insert' | 'i':
                if len(tokens) < 3:
                    print("\nUsage: (i)nsert after_todo# new_todo\n")
                    continue
                try:
                    index = int(tokens[1])
                except ValueError:
                    print("\nUsage: (i)nsert after_todo# new_todo\n")
                    continue
                todo = " ".join(tokens[2:])
                if check_range(index - 1, len(todos) - 1):
                    previous_todo = todos[index - 1]
                    next_todo = todos[index]
                    todos.insert(index, todo)
                    save_todos(todos)
                    print(f"\n\"{todo}\" inserted between \"{previous_todo.title()}\" and \"{next_todo.title()}\".\n")
            case 'complete' | 'c':
                if len(tokens) < 2:
                    print("\nUsage: (c)omplete todo#\n")
                    continue
                try:
                    index = int(tokens[1])
                except ValueError:
                    print("\nUsage: (c)omplete todo#\n")
                    continue
                if check_range(index - 1, len(todos)):
                    todo = todos[index - 1]
                    todos.pop(index - 1)
                    save_todos(todos)
                    print(f"\n\"#{index}. {todo.title()}\" has been removed from the ToDo list.\n")
            case 'help' | 'h':
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
            case 'quit' | 'q':
                break
            case _:
                print("\nInvalid command. Please try again.\n")

    print("\nGoodbye!\n")

if __name__ == "__main__":
    main()
