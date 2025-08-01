from src.pytodo.core import functions as fn
import time

def main():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("\nWelcome to the TodosModos 1.0!")
    print(f"{now}\n")
    todos = fn.initialize()

    while True:
        user_action = input("Enter command or 'help': ").strip().lower()
        tokens = user_action.split()
        command = tokens[0]
        match command:
            case 'add' | 'a':
                try:
                    result = fn.add(tokens, todos)
                except ValueError as e:
                    result = f"Error: {e}"
            case 'show' | 's':
                td = fn.get_todos(todos)
                if len(td) == 0:
                    result = "The todo list is empty."
                else:
                    temp = []
                    for index, todo in enumerate(td):
                        temp.append(f"{index + 1}. {todo.title()}")
                    result = "\n".join(temp)
            case 'edit' | 'e':
                try:
                    result = fn.edit(tokens, todos)
                except ValueError as e:
                    result = f"Error: {e}"
            case 'insert' | 'i':
                try:
                    result = fn.insert(tokens, todos)
                except ValueError as e:
                    result = f"Error: {e}"
            case 'complete' | 'c':
                try:
                    result = fn.complete(tokens, todos)
                except ValueError as e:
                    result = f"Error: {e}"
            case 'help' | 'h':
                result = "\n".join(fn.display_help())
            case 'quit' | 'q':
                result = "Goodbye!"
                exit(0)
            case _:
                result = "Invalid command. Please try again."
        print(f"\n{result}\n")

if __name__ == "__main__":
    main()
