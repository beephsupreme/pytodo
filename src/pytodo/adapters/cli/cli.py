from src.pytodo.core import functions as fn

def main():
    print("\nWelcome to the PyTodo 1.0!")

    while True:
        user_action = input("Enter command or 'help': ").strip().lower()
        tokens = user_action.split()
        command = tokens[0]
        match command:
            case 'add' | 'a':
                try:
                    result = fn.add(tokens)
                except ValueError as e:
                    result = f"Error: {e}"
            case 'show' | 's':
                todos = fn.load_store()
                if len(todos) == 0:
                    result = "The todo list is empty."
                else:
                    enumerated_todos = [f"{i + 1}. {item}" for i, item in enumerate(todos)]
                    result = "\n".join(enumerated_todos)
            case 'edit' | 'e':
                try:
                    result = fn.edit(tokens)
                except ValueError as e:
                    result = f"Error: {e}"
            case 'insert' | 'i':
                try:
                    result = fn.insert(tokens)
                except ValueError as e:
                    result = f"Error: {e}"
            case 'complete' | 'c':
                try:
                    result = fn.complete(tokens)
                except ValueError as e:
                    result = f"Error: {e}"
            case 'help' | 'h':
                todo_help = fn.display_help()
                enumerated_help = [f"{i + 1}. {item}" for i, item in enumerate(todo_help)]
                result = "Available commands:\n" + "\n".join(enumerated_help)
            case 'quit' | 'q':
                result = "Goodbye!"
                exit(0)
            case _:
                result = "Invalid command. Please try again."
        print(f"\n{result}\n")

if __name__ == "__main__":
    main()
