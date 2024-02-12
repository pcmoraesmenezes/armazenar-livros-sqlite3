import sqlite3
from tabulate import tabulate  # type: ignore
from configs import (
    TABLE_NAME,
    DB_FILE,
    AUTHORS_TABLE,
    GENRES_TABLE,
    LANGUAGES_TABLE
)


def read_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    print(
        "Do you want to:\n"
        "1. Print all books info\n"
        "2. Search for a book by Title\n"
        "3. List all books by Genre, author, format, or Language?\n"
        "4. Print all Authors\n"
        "5. Print all Genres\n"
        "6. Print all Languages\n"
    )
    answer = input()

    if answer == "1":
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

        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    if answer == "2":
        book_title = input("Enter the title of the book: ")
    
        cursor.execute(
            f"SELECT {TABLE_NAME}.title, {AUTHORS_TABLE}.name, "
            f"{GENRES_TABLE}.name, start_date, end_date, rating, pages, "
            f"{LANGUAGES_TABLE}.name "
            f"FROM {TABLE_NAME}, {AUTHORS_TABLE}, "
            f"{GENRES_TABLE}, {LANGUAGES_TABLE} "
            f"WHERE {TABLE_NAME}.id_author = {AUTHORS_TABLE}.id "
            f"AND {TABLE_NAME}.id_genre = {GENRES_TABLE}.id "
            f"AND {TABLE_NAME}.id_language = {LANGUAGES_TABLE}.id "
            f"AND {TABLE_NAME}.title = ?",
            (book_title,),
        )

        book = cursor.fetchone()
        if book:
            headers = [
                "Title", "Author", "Genre", "Start Date",
                "End Date", "Rating", "Pages", "Language", "Format"
            ]
            table_data = [list(book)]

            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("Book not found.")

    if answer == "3":
        print("Select one:\nGenre (1)\nAuthor (2)\nFormat (3)\nLanguage (4)")
        choice = input()

        if choice == "1":
            genre = input("Enter the genre: ")
            cursor.execute(
                f"SELECT {TABLE_NAME}.title, {AUTHORS_TABLE}.name, "
                f"{GENRES_TABLE}.name, {TABLE_NAME}.start_date, "
                f"{TABLE_NAME}.end_date, {TABLE_NAME}.rating, "
                f"{TABLE_NAME}.pages, {LANGUAGES_TABLE}.name "
                f"FROM {TABLE_NAME}, {AUTHORS_TABLE}, {GENRES_TABLE}, "
                f"{LANGUAGES_TABLE} "
                f"WHERE {TABLE_NAME}.id_author = {AUTHORS_TABLE}.id "
                f"AND {TABLE_NAME}.id_genre = {GENRES_TABLE}.id "
                f"AND {TABLE_NAME}.id_language = {LANGUAGES_TABLE}.id "
                f"AND {GENRES_TABLE}.name = ?",
                (genre,),
            )
            books = cursor.fetchall()
            if books:

                headers = [
                    "Title", "Author", "Genre", "Start Date",
                    "End Date", "Rating", "Pages", "Language", "Format"
                ]

                table_data = []
                for book in books:
                    table_data.append(list(book))

                print(tabulate(table_data, headers=headers, tablefmt="grid"))

            else:
                print('Genre not found ')

        if choice == "2":
            author = input("Enter the author: ")
            cursor.execute(
                f"SELECT {TABLE_NAME}.title, {AUTHORS_TABLE}.name, "
                f"{GENRES_TABLE}.name, {TABLE_NAME}.start_date, "
                f"{TABLE_NAME}.end_date, {TABLE_NAME}.rating, "
                f"{TABLE_NAME}.pages, {LANGUAGES_TABLE}.name "
                f"FROM {TABLE_NAME}, {AUTHORS_TABLE}, {GENRES_TABLE}, "
                f"{LANGUAGES_TABLE} "
                f"WHERE {TABLE_NAME}.id_author = {AUTHORS_TABLE}.id "
                f"AND {TABLE_NAME}.id_genre = {GENRES_TABLE}.id "
                f"AND {TABLE_NAME}.id_language = {LANGUAGES_TABLE}.id "
                f"AND {AUTHORS_TABLE}.name = ?",
                (author,),
            )
            books = cursor.fetchall()
            if books:
                headers = [
                    "Title", "Author", "Genre", "Start Date",
                    "End Date", "Rating", "Pages", "Language", "Format"
                ]

                table_data = []
                for book in books:
                    table_data.append(list(book))

                print(tabulate(table_data, headers=headers, tablefmt="grid"))

            else:
                print('Author not found')

        if choice == "3":
            book_format = input("Enter the format: ")
            cursor.execute(
                f"SELECT {TABLE_NAME}.title, {AUTHORS_TABLE}.name, "
                f"{GENRES_TABLE}.name, {TABLE_NAME}.start_date, "
                f"{TABLE_NAME}.end_date, {TABLE_NAME}.rating, "
                f"{TABLE_NAME}.pages, {LANGUAGES_TABLE}.name "
                f"FROM {TABLE_NAME}, {AUTHORS_TABLE}, {GENRES_TABLE}, "
                f"{LANGUAGES_TABLE} "
                f"WHERE {TABLE_NAME}.id_author = {AUTHORS_TABLE}.id "
                f"AND {TABLE_NAME}.id_genre = {GENRES_TABLE}.id "
                f"AND {TABLE_NAME}.id_language = {LANGUAGES_TABLE}.id "
                f"AND {TABLE_NAME}.id_format = ?",
                (book_format,),
            )
            books = cursor.fetchall()

            if books:

                headers = [
                    "Title", "Author", "Genre", "Start Date",
                    "End Date", "Rating", "Pages", "Language", "Format"
                ]

                table_data = []
                for book in books:
                    table_data.append(list(book))

                print(tabulate(table_data, headers=headers, tablefmt="grid"))

            else:
                print('Format not found')

        if choice == "4":
            language = input("Enter the language: ")
            cursor.execute(
                f"SELECT {TABLE_NAME}.title, {AUTHORS_TABLE}.name, "
                f"{GENRES_TABLE}.name, {TABLE_NAME}.start_date, "
                f"{TABLE_NAME}.end_date, {TABLE_NAME}.rating, "
                f"{TABLE_NAME}.pages, {LANGUAGES_TABLE}.name "
                f"FROM {TABLE_NAME}, {AUTHORS_TABLE}, {GENRES_TABLE}, "
                f"{LANGUAGES_TABLE} "
                f"WHERE {TABLE_NAME}.id_author = {AUTHORS_TABLE}.id "
                f"AND {TABLE_NAME}.id_genre = {GENRES_TABLE}.id "
                f"AND {TABLE_NAME}.id_language = {LANGUAGES_TABLE}.id "
                f"AND {LANGUAGES_TABLE}.name = ?",
                (language,),
            )
            books = cursor.fetchall()
            if books:
                headers = [
                    "Title", "Author", "Genre", "Start Date",
                    "End Date", "Rating", "Pages", "Language", "Format"
                ]

                table_data = []
                for book in books:
                    table_data.append(list(book))

                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            else:
                print('Language not found')
    if answer == "4":
        cursor.execute(f"SELECT * FROM {AUTHORS_TABLE}")
        authors = cursor.fetchall()
        print(tabulate(authors, headers=["id", "Author"], tablefmt="grid"))

    if answer == "5":
        cursor.execute(f"SELECT * FROM {GENRES_TABLE}")
        genres = cursor.fetchall()
        print(tabulate(genres, headers=["id", "Genre"], tablefmt="grid"))

    if answer == "6":
        cursor.execute(f"SELECT * FROM {LANGUAGES_TABLE}")
        languages = cursor.fetchall()
        print(tabulate(languages, headers=["id", "Language"], tablefmt="grid"))

    cursor.close()
    connection.close()
