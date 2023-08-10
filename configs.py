from pathlib import Path
import os
import shutil

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "books"


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def center_text(text, width):
    return text.center(width)


def print_text():
    terminal_width = shutil.get_terminal_size().columns
    welcome_message = "Welcome to your book DataBase"
    centered_welcome = center_text(welcome_message, terminal_width)
    print(centered_welcome)


def print_horizontal_line(character="-"):
    terminal_width = shutil.get_terminal_size().columns
    horizontal_line = character * terminal_width
    print(horizontal_line)
