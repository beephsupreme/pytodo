import cli_functions as cli

def main():
    print("\nWelcome to the PyTodo 1.0!")
    while True:
        user_action = input("Enter command or 'help': ").strip().lower()
        tokens = user_action.split()
        command = tokens[0]
        match command:
            case 'add' | 'a':
                cli.add(tokens)
            case 'show' | 's':
               cli.show()
            case 'edit' | 'e':
              cli.edit(tokens)
            case 'insert' | 'i':
               cli.insert(tokens)
            case 'complete' | 'c':
               cli.complete(tokens)
            case 'help' | 'h':
                cli.display_help()
            case 'quit' | 'q':
                cli.display_result("Goodbye!")
                exit(0)
            case _:
                cli.display_result("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
