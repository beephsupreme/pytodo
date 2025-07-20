prompt = "Enter To-Do : "
todos = []

while True:
    user_action = input("Type 'add', 'show', or 'quit': ").strip().lower()

    match user_action:
        case 'add':
            todo = input(prompt)
            todos.append(todo)
        case 'show':
            for index, todo in enumerate(todos):
                print(f"{index + 1}. {todo}")
        case 'quit':
            exit(0)
        case _:
            print("Invalid input. Please try again.")
