import json, os, tempfile
from pathlib import Path
from platformdirs import user_data_dir

APP_NAME = "pytodo"
APP_AUTHOR = "rowsey.org"

def get_store_path(filename: str = "store.json") -> Path:
    base = Path(user_data_dir(APP_NAME, APP_AUTHOR))
    base.mkdir(parents=True, exist_ok=True)
    return base / filename

FILEPATH = get_store_path()
HELP_TEXT = ["(a)dd todo", "(c)omplete todo_number", "(e)dit todo_number new_todo", "(h)elp: show this menu",
             "(i)nsert after_todo new_todo", "(q)uit: end this program", "(s)how: show all todo's"]

def load_store(path: Path):
    """ if path doesn't exist, return empty list, else load store """
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_store(path: Path, data: list):
    """ write store to FILEPATH and save a backup """
    tmp_fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=path.name, text=True)
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as tmp:
            json.dump(data, tmp, ensure_ascii=False, indent=2)
            tmp.flush()
            os.fsync(tmp.fileno())
        # optional one-file backup
        if path.exists():
            backup = path.with_suffix(path.suffix + ".bak")
            try: os.replace(path, backup)
            except OSError: pass
        os.replace(tmp_name, path)  # atomic on same filesystem
    finally:
        try: os.unlink(tmp_name)
        except FileNotFoundError: pass

def initialize():
    """ get store and if empty, save as new file """
    todos = load_store(FILEPATH)
    if todos == []:
        save_store(FILEPATH, todos)
    return todos

def check_range(index, length) -> bool:
    """ check if index is between 0 and length """
    if index < 0 or index >= length:
        return False
    else:
        return True

def add(tokens, todos) -> str:
    """ add todos - throws ValueError if adding fails """
    usage = "Usage: (a)dd <todo>"
    if len(tokens) < 2:
        raise ValueError(usage)
    todo = " ".join(tokens[1:])
    todos.append(todo)
    save_store(FILEPATH, todos)
    return f"\"{todo.capitalize()}\" added to the Todo list"

def edit(tokens, todos) -> str:
    """ edit todos """
    usage = "Usage: (e)dit <todo #> <new todo>"
    if len(tokens) < 3:
        raise ValueError(usage)
    try:
        index = int(tokens[1])
    except ValueError:
        raise ValueError(usage)
    todo = " ".join(tokens[2:])
    if check_range(index - 1, len(todos)):
        old_todo = todos[index - 1]
        todos[index - 1] = todo
        save_store(FILEPATH, todos)
        return f"Todo #{index} changed from \"{old_todo.title()}\" to \"{todos[index - 1].title()}\"."
    else:
        raise ValueError(f"Todo #{index} not found.")

def insert(tokens, todos) -> str:
    """ insert new todo """
    usage = "Usage: (i)nsert <after todo #> <new todo>"
    if len(tokens) < 3:
        raise ValueError(usage)
    try:
        index = int(tokens[1])
    except ValueError:
        raise ValueError(usage)
    todo = " ".join(tokens[2:])
    if check_range(index - 1, len(todos) - 1):
        previous_todo = todos[index - 1]
        next_todo = todos[index]
        todos.insert(index, todo)
        save_store(FILEPATH, todos)
        return f"\"{todo}\" inserted between \"{previous_todo.title()}\" and \"{next_todo.title()}\"."
    else:
        raise ValueError(f"Todo #{index} not found.")

def complete(tokens, todos) -> str:
    """ complete todos """
    usage = "Usage: (c)omplete <todo #>"
    if len(tokens) < 2:
        raise ValueError(usage)
    try:
        index = int(tokens[1])
    except ValueError:
        raise ValueError(usage)
    if check_range(index - 1, len(todos)):
        todo = todos[index - 1]
        todos.pop(index - 1)
        save_store(FILEPATH, todos)
        return f"\"#{index}. {todo.title()}\" has been removed from the ToDo list."
    else:
        raise ValueError(f"Todo #{index} not found.")

def get_todos(todos) -> list:
    """ get todos """
    return todos

def display_help() -> list:
    """ display help """
    return HELP_TEXT