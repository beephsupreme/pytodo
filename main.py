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
    f.close()
    return todos

def save_todos(todos):
    with open(filepath, 'w') as f:
        json.dump(todos, f)
    f.close()

def check_range(index, length):
    if index < 0 or index >= length:
        print("Index out-of-range. Please try again.")
        return False
    else:
        return True

def main():
    todos = initialize()

    while True:
        user_action = input("Type '(a)dd', '(s)how', '(e)dit', (c)omplete, or '(q)uit': ").strip().lower()

        match user_action:
            case 'add' | 'a':
                todo = input("Enter Todo : ")
                todos.append(todo)
                save_todos(todos)
                print("ToDo added successfully")
            case 'show' | 's':
                for index, todo in enumerate(todos):
                    print(f"{index + 1}. {todo.title()}")
            case 'edit' | 'e':
                index = int(input("Which ToDo do you want to edit? "))
                if check_range(index - 1, len(todos)):
                    todo = input("Enter Todo : ")
                    todos[index - 1] = todo
                    save_todos(todos)
                    print(f"Todo #{index} updated.")
            case 'complete' | 'c':
                index = int(input("Enter ToDo to complete : "))
                if check_range(index - 1, len(todos)):
                    todos.pop(index - 1)
                    save_todos(todos)
                    print(f"Todo #{index} complete.")
            case 'quit' | 'q':
                break
            case _:
                print("Invalid input. Please try again.")
    print("Goodbye!")

if __name__ == "__main__":
    main()
