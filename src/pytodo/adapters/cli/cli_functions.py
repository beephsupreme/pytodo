from src.pytodo.core import functions as fn

HELP_TEXT = ["(a)dd todo", "(c)omplete todo_number", "(e)dit todo_number new_todo", "(h)elp: show this menu",
             "(i)nsert before_todo_number new_todo", "(q)uit: end this program", "(s)how: show all todo's"]

def display_result(msg):
    print(f"\n{msg}\n")

def add(tokens):
    if len(tokens) < 2:
        display_result("(a)dd failed: not enough arguments")
    else:
        if fn.add(" ".join(tokens[1:])):
            display_result("task added...")
        else:
            print("An error occurred - check error.log for details")

def show():
    todos = fn.load_store()
    if len(todos) == 0:
        display_result("The todo list is empty.")
    else:
        enumerated_todos = [f"{i + 1}. {item}" for i, item in enumerate(todos)]
        temp = "\n".join(enumerated_todos)
        display_result(temp)

def edit(tokens):
    if len(tokens) < 3:
        display_result("(e)dit failed: not enough arguments")
    else:
        try:
            index = int(tokens[1]) - 1
            task = " ".join(tokens[2:])
            if fn.edit(index, task):
                display_result("task edited...")
            else:
                display_result("An error occurred - check error.log for details")
        except ValueError:
            display_result("(e)dit failed: invalid argument")

def insert(tokens):
    if len(tokens) < 3:
        display_result("(i)insert failed: not enough arguments")
    else:
        try:
            index = int(tokens[1]) - 1
            task = " ".join(tokens[2:])
            if fn.insert(index, task):
                display_result("task inserted...")
            else:
                display_result("An error occurred - check error.log for details")
        except ValueError:
            display_result("(i)insert failed: invalid argument")

def complete(tokens):
    if len(tokens) < 2:
        display_result("(c)omplete failed: not enough arguments")
    else:
        try:
            index = int(tokens[1]) - 1
            if fn.complete(index):
                display_result("task completed...")
            else:
                display_result("An error occurred - check error.log for details")
        except ValueError:
            display_result("(c)omplete failed: invalid argument")

def display_help():
    enumerated_help = [f"{i + 1}. {item}" for i, item in enumerate(HELP_TEXT)]
    display_result("Available commands:\n" + "\n".join(enumerated_help))
