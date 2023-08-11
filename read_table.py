import sqlite3
from tabulate import tabulate  # type: ignore
from configs import TABLE_NAME, DB_FILE


def read_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    print(
        "Do you want to:\n"
        "1. Print all books info\n"
        "2. Search for a book by Title\n"
        "3. List all books by Genre, author, format, or Language?"
    )
    answer = input()

    if answer == "1":
        cursor.execute(
            f"SELECT title, author, genre, "
            f"start_date, end_date, rating, pages, language, format "
            f"FROM {TABLE_NAME} "
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
            f"SELECT title, author, genre, "
            f"start_date, end_date, rating, pages, language, format "
            f"FROM {TABLE_NAME} "
            f"WHERE title=?",
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
                f"SELECT title, author, genre, "
                f"start_date, end_date, rating, pages, language, format "
                f"FROM {TABLE_NAME} "
                f"WHERE genre=?",
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
                f"SELECT title, author, genre, "
                f"start_date, end_date, rating, pages, language, format "
                f"FROM {TABLE_NAME} "
                f"WHERE author=?",
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
                f"SELECT title, author, genre, "
                f"start_date, end_date, rating, pages, language, format "
                f"FROM {TABLE_NAME} "
                f"WHERE format=?",
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
                f"SELECT title, author, genre, "
                f"start_date, end_date, rating, pages, language, format "
                f"FROM {TABLE_NAME} "
                f"WHERE language=?",
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
    cursor.close()
    connection.close()
