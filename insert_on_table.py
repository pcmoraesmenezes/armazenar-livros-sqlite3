import sqlite3
from configs import (
    TABLE_NAME,
    DB_FILE,
    clear_terminal,
    AUTHORS_TABLE,
    GENRES_TABLE,
    LANGUAGES_TABLE
)


def insert_into_author_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    authors_ = input("Author name: ")

    cursor.execute(
        f"INSERT INTO {AUTHORS_TABLE} (name) VALUES (?);",
        (authors_,)
    )

    connection.commit()
    connection.close()


def insert_into_genre_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    genres_ = input("Genre name: ")

    cursor.execute(
        f"INSERT INTO {GENRES_TABLE} (name) VALUES (?);",
        (genres_,)
    )

    connection.commit()
    connection.close()


def insert_into_language_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    languages_ = input("Language name: ")

    cursor.execute(
        f"INSERT INTO {LANGUAGES_TABLE} (name) VALUES (?);",
        (languages_,)
    )

    connection.commit()
    connection.close()


def insert_into_book_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    title = input("Title: ")
    id_author = input("Author id: ")
    id_genre = input("Genre id: ")
    start_date = input("Start date: ")
    end_date = input("End date: ")
    rating = input("Rating: ")
    pages = input("Pages: ")
    id_language = input("Language id: ")
    id_format = input("Format id: ")

    cursor.execute(
        f"INSERT INTO {TABLE_NAME} (title, id_author, id_genre, start_date, "
        f"end_date, rating, pages, id_language, id_format) "
        f"VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
        (title, id_author, id_genre, start_date,
            end_date, rating, pages, id_language, id_format)
    )

    connection.commit()
    connection.close()


def navegate_menu():
    clear_terminal()
    print("1 - Insert into author table")
    print("2 - Insert into genre table")
    print("3 - Insert into language table")
    print("4 - Insert into book table")
    print("5 - Exit")
    option = input("Choose an option: ")

    if option == "1":
        insert_into_author_table()
    elif option == "2":
        insert_into_genre_table()
    elif option == "3":
        insert_into_language_table()
    elif option == "4":
        insert_into_book_table()
    elif option == "5":
        print("Exiting...")
        exit()
    else:
        print("Invalid option")
        navegate_menu()
