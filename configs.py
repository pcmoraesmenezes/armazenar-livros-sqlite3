from pathlib import Path
import os
import shutil
import sqlite3
from tabulate import tabulate   # type: ignore

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "books"
AUTHORS_TABLE = "authors"
GENRES_TABLE = "genres"
LANGUAGES_TABLE = "languages"


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


def print_table_after_changes():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(
            f"SELECT {TABLE_NAME}.title, {AUTHORS_TABLE}.name, "
            f"{GENRES_TABLE}.name, start_date, end_date, rating, pages, "
            f"{LANGUAGES_TABLE}.name "
            f"FROM {TABLE_NAME}, {AUTHORS_TABLE}, "
            f"{GENRES_TABLE}, {LANGUAGES_TABLE} "
            f"WHERE {TABLE_NAME}.id_author = {AUTHORS_TABLE}.id "
            f"AND {TABLE_NAME}.id_genre = {GENRES_TABLE}.id "
            f"AND {TABLE_NAME}.id_language = {LANGUAGES_TABLE}.id; "
        )
    books = cursor.fetchall()

    headers = [
                    "Title", "Author", "Genre", "Start Date",
                    "End Date", "Rating", "Pages", "Language", "Format"
                ]

    table_data = []
    for book in books:
        table_data.append(list(book))

    print(tabulate(table_data,
                   headers=headers, tablefmt="grid"))

    cursor.close()
    connection.close()
