prompt = "Enter To-Do : "
# todos = []
todos = ["cook", "clean", "shop"]

while True:
    user_action = input("Type '(a)dd', '(s)how', '(e)dit', (c)omplete, or '(q)uit': ").strip().lower()

    match user_action:
        case 'add' | 'a':
            todo = input(prompt)
            todos.append(todo)
        case 'show' | 's':
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo.title()}")
        case 'edit' | 'e':
            index = int(input("Enter ToDo to edit : "))
            if index - 1 < 0 or index - 1 >= len(todos):
                print("Index out-of-range. Please try again.")
            else:
                todo = input(prompt)
                todos[index - 1] = todo
                print(f"Todo #{index} updated.")
        case 'complete' | 'c':
            index = int(input("Enter ToDo to complete : "))
            if index - 1 < 0 or index - 1 >= len(todos):
                print("Index out-of-range. Please try again.")
            else:
                todos.remove(todos[index - 1])
                print(f"Todo #{index} complete.")
        case 'quit' | 'q':
            break
        case _:
            print("Invalid input. Please try again.")

print("Goodbye!")


