import sqlite3
from configs import TABLE_NAME, DB_FILE


def read_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    print("Do you want to:\n"
          "1. Print all books info\n"
          "2. Search for a book by Title\n"
          "3. List all books by Genre, author, format, or Language?")
    answer = input()

    if answer == '1':
        cursor.execute(
            f"SELECT title, author, genre, "
            f"start_date, end_date, rating, pages, language, format "
            f"FROM {TABLE_NAME} "
        )
        books = cursor.fetchall()
        for book in books:
            print()
            print("Title:", book[0])
            print("Author:", book[1])
            print("Genre:", book[2])
            print("Start Date:", book[3])
            print("End Date:", book[4])
            print("Rating:", book[5])
            print("Pages:", book[6])
            print("Language:", book[7])
            print("Format:", book[8])
            print("-" * 30)

    if answer == '2':
        print('\nEnter the title of the book: ')
        book_title = input()
        print()
        cursor.execute(
            f"SELECT title, author, genre, "
            f"start_date, end_date, rating, pages, language, format "
            f"FROM {TABLE_NAME} "
            f"WHERE title=?",
            (book_title,)
        )

        book = cursor.fetchone()
        if book:
            print("Title:", book[0])
            print("Author:", book[1])
            print("Genre:", book[2])
            print("Start Date:", book[3])
            print("End Date:", book[4])
            print("Rating:", book[5])
            print("Pages:", book[6])
            print("Language:", book[7])
            print("Format:", book[8])
            print("-" * 30)
        else:
            print("Book not found.")

    cursor.close()
    connection.close()


read_table()
