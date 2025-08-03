from src.pytodo.core import functions as fn

HELP_TEXT = ["(a)dd todo", "(c)omplete todo_number", "(e)dit todo_number new_todo", "(h)elp: show this menu",
             "(i)nsert after_todo new_todo", "(q)uit: end this program", "(s)how: show all todo's"]

def display_result(msg):
    print(f"\n{msg}\n")


def main():
    print("\nWelcome to the PyTodo 1.0!")

    while True:
        user_action = input("Enter command or 'help': ").strip().lower()
        tokens = user_action.split()
        command = tokens[0]
        match command:
            case 'add' | 'a':
                if len(tokens) < 2:
                    display_result("(a)dd failed: not enough arguments")
                else:
                    if fn.add(" ".join(tokens[1:])):
                        display_result("task added...")
                    else:
                        print("An error occurred - check error.log for details")
            case 'show' | 's':
                todos = fn.load_store()
                if len(todos) == 0:
                    display_result("The todo list is empty.")
                else:
                    enumerated_todos = [f"{i + 1}. {item}" for i, item in enumerate(todos)]
                    temp = "\n".join(enumerated_todos)
                    display_result(temp)
            case 'edit' | 'e':
                if len(tokens) < 3:
                    display_result("(e)dit failed: not enough arguments")
                else:
                    try:
                        index = int(tokens[1])
                        task = " ".join(tokens[2:])
                        if fn.edit(index, task):
                            display_result("task edited...")
                        else:
                            display_result("An error occurred - check error.log for details")
                    except ValueError:
                        display_result("(e)dit failed: invalid argument")
            case 'insert' | 'i':
                if len(tokens) < 3:
                    display_result("(i)insert failed: not enough arguments")
                else:
                    try:
                        index = int(tokens[1])
                        task = " ".join(tokens[2:])
                        if fn.insert(index, task):
                            display_result("task inserted...")
                        else:
                            display_result("An error occurred - check error.log for details")
                    except ValueError:
                        display_result("(i)insert failed: invalid argument")
            case 'complete' | 'c':
                if len(tokens) < 2:
                    display_result("(c)omplete failed: not enough arguments")
                else:
                    try:
                        index = int(tokens[1])
                        if fn.complete(index):
                            display_result("task completed...")
                        else:
                            display_result("An error occurred - check error.log for details")
                    except ValueError:
                        display_result("(c)omplete failed: invalid argument")
            case 'help' | 'h':
                enumerated_help = [f"{i + 1}. {item}" for i, item in enumerate(HELP_TEXT)]
                display_result("Available commands:\n" + "\n".join(enumerated_help))
            case 'quit' | 'q':
                display_result("Goodbye!")
                exit(0)
            case _:
                display_result("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
