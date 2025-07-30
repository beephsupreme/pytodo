from modules import functions as fn


def main():
    todos = fn.initialize()
    print("\nWelcome to the TodosModos 1.0!\n")
    while True:
        user_action = input("Enter command or 'help': ").strip().lower()
        tokens = user_action.split()
        command = tokens[0]

        match command:
            case 'add' | 'a':
                fn.add(tokens, todos)
            case 'show' | 's':
                fn.display_todos(todos)
            case 'edit' | 'e':
                fn.edit(tokens, todos)
            case 'insert' | 'i':
                fn.insert(tokens, todos)
            case 'complete' | 'c':
                fn.complete(tokens, todos)
            case 'help' | 'h':
                fn.display_help()
            case 'quit' | 'q':
                print("\nGoodbye!\n")
                exit(0)
            case _:
                print("\nInvalid command. Please try again.\n")


if __name__ == "__main__":
    main()
