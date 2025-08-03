import json, os, tempfile, logging
from pathlib import Path
from platformdirs import user_data_dir

APP_NAME = "pytodo"
APP_AUTHOR = "rowsey.org"


def get_store_path(filename: str = "store.json") -> Path:
    base = Path(user_data_dir(APP_NAME, APP_AUTHOR))
    base.mkdir(parents=True, exist_ok=True)
    return base / filename

FILEPATH = get_store_path()
LOG = get_store_path(filename="pytodo.log")

logging.basicConfig(filename=LOG,
                    encoding="utf-8",
                    filemode='a',
                    format="{asctime} - {levelname} - {message}",
                    style="{",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    )

def load_store() -> list:
    """ if path doesn't exist, return empty list, else load store """
    if not FILEPATH.exists():
        return []
    with FILEPATH.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_store(data: list):
    """ write store to FILEPATH and save a backup """
    tmp_fd, tmp_name = tempfile.mkstemp(dir=FILEPATH.parent, prefix=FILEPATH.name, text=True)
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as tmp:
            json.dump(data, tmp, ensure_ascii=False, indent=2)
            tmp.flush()
            os.fsync(tmp.fileno())
        # optional one-file backup
        if FILEPATH.exists():
            backup = FILEPATH.with_suffix(FILEPATH.suffix + ".bak")
            try: os.replace(FILEPATH, backup)
            except OSError: pass
        os.replace(tmp_name, FILEPATH)  # atomic on same filesystem
    finally:
        try: os.unlink(tmp_name)
        except FileNotFoundError: pass

def check_range(index, length) -> bool:
    """ check if index is between 0 and length """
    if index < 0 or index >= length:
        return False
    else:
        return True

def add(todo: str) -> bool:
    """ add new task to the todos list - return True for success, False for failure """
    todos = load_store()
    todos.append(todo)
    try:
        save_store(todos)
        return True
    except FileNotFoundError:
        logging.error(f"save_store: File {FILEPATH} not found")
        return False

def edit(index, todo) -> bool:
    """ edit a selected task - return True for success, False for failure """
    # edit should load data file, replace indicated task, save data file, log errors to log file, report success or failure
    todos = load_store()
    if check_range(index - 1, len(todos)):
        todos[index - 1] = todo
        try:
            save_store(todos)
            return True
        except FileNotFoundError:
            logging.error(f"save_store: File {FILEPATH} not found")
            return False
    else:
        logging.error(f"Todo #{index} not found.")
        return False

def insert(index, task) -> bool:
    """ insert new task - return True for success, False for failure """
    todos = load_store()
    if check_range(index - 1, len(todos) - 1):
        todos.insert(index, task)
        try:
            save_store(todos)
            return True
        except FileNotFoundError:
            logging.error(f"save_store: File {FILEPATH} not found")
            return False
    else:
        logging.error(f"Todo #{index} not found.")
        return False

def complete(index) -> bool:
    """ complete todos - return True for success, False for failure """
    todos = load_store()
    if check_range(index - 1, len(todos)):
        todos.pop(index - 1)
        try:
            save_store(todos)
            return True
        except FileNotFoundError:
            logging.error(f"save_store: File {FILEPATH} not found")
            return False
    else:
        logging.error(f"Todo #{index} not found.")
        return False
