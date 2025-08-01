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
                    print(f"\n{result}\n")
                except ValueError as e:
                    print(f"Error: {e}")
            case 'show' | 's':
                result = fn.get_todos(todos)
                print(f"\n{result}\n")
            case 'edit' | 'e':
                result = fn.edit(tokens, todos)
                print(f"\n{result}\n")
            case 'insert' | 'i':
                result = fn.insert(tokens, todos)
                print(f"\n{result}\n")
            case 'complete' | 'c':
                fn.complete(tokens, todos)
            case 'help' | 'h':
                print(fn.display_help())
            case 'quit' | 'q':
                print("\nGoodbye!\n")
                exit(0)
            case _:
                print("\nInvalid command. Please try again.\n")


if __name__ == "__main__":
    main()
