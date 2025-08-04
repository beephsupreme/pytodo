import src.pytodo.core.functions as fn
import FreeSimpleGUI as sg

def main():
    label = sg.Text("Enter a task")
    input_box = sg.InputText(key="user_input")
    todo_list = sg.Listbox(values=fn.load_store(), key="todo_list", enable_events=True, size=(45, 10))
    add_button = sg.Button("Add")
    edit_button = sg.Button("Edit")
    insert_button = sg.Button("Insert")
    complete_button = sg.Button("Complete")
    quit_button = sg.Button("Quit")

    layout = [ [label],
               [input_box],
               [todo_list],
               [add_button, edit_button, insert_button, complete_button, quit_button]
             ]

    window = sg.Window("PyTodo",
                       layout = layout,
                       font = ("Helvetica", 20))

    while True:
        event, values = window.read()
        match event:
            case "Add":
                fn.add(values["user_input"])
                input_box.update('')
                todo_list.update(fn.load_store())
            case "Edit":
                index = todo_list.get_indexes()[0]
                fn.edit(index, values["user_input"])
                todo_list.update(fn.load_store())
                input_box.update('')
            case "Insert":
                index = todo_list.get_indexes()[0]
                fn.insert(index, values["user_input"])
                todo_list.update(fn.load_store())
                input_box.update('')
            case "Complete":
                index = todo_list.get_indexes()[0]
                fn.complete(index)
                todo_list.update(fn.load_store())
            case "Quit":
                break
            case sg.WINDOW_CLOSED:
                break

    window.close()


if __name__ == "__main__":
    main()


