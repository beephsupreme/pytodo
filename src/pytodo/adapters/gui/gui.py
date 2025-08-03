# import src.pytodo.core.functions as fn

import FreeSimpleGUI as sg

def main():
    label = sg.Text("Enter a task")
    text_box = sg.InputText()
    add_button = sg.Button("Add Task", key="add_task")

    layout = [[label],[text_box, add_button]]
    window = sg.Window("PyTodo", layout)

    window.read()
    window.close()


if __name__ == "__main__":
    main()


