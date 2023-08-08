import sqlite3
import os

DB_NAME = "db.sqlite3"
TABLE_NAME = 'books'

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()


def insert_book(cursor):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    rating = float(input("Enter rating: "))
    pages = int(input("Enter number of pages: "))
    language = input("Enter language: ")
    book_format = input("Enter book format: ")

    cursor.execute(
        'INSERT INTO books (title, author, genre, start_date, end_date, rating'
        ', pages, language, format) '
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (title, author, genre, start_date, end_date,
            rating, pages, language, book_format)
    )


cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)
books = cursor.fetchall()
for book in books:
    print(books)

while True:
    os.system('clear')
    print('\n', '-' * 50, 'Welcome to Library Database', '-' * 50)
    print(
        'Menu:\n'
        'To read, press 1: View the list of books you have read.\n'
        'To Insert, press 2: Add a new book to the database.\n'
        'To Update, press 3: Update the rating or details of a book.\n'
        'To exit, press 4: Exit the program.'
    )

    nav = int(input(''))
    if nav == 1:
        print('You choose to view the list of books you have read!')
        print('Do you want to search for a specific book (1)')
        print('or do you want to list all books (2)?')

        choice = int(input(''))

        if choice == 1:
            search_term = input(
                'Enter a search term (title, author, genre, etc.): '
            )
            cursor.execute(
                'SELECT * FROM books WHERE title LIKE ?'
                ' OR author LIKE ? OR genre LIKE ?',
                (
                    '%' + search_term + '%',
                    '%' + search_term + '%',
                    '%' + search_term + '%'
                )
            )
            books = cursor.fetchall()
            for book in books:
                print(book)  # Print book details

        elif choice == 2:
            cursor.execute(f'SELECT * FROM {TABLE_NAME}')
            books = cursor.fetchall()
            for book in books:
                print(book)  # Print book details

    if nav == 2:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
            '('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'title TEXT NOT NULL,'
            'author TEXT NOT NULL,'
            'genre TEXT,'
            'start_date DATE,'
            'end_date DATE,'
            'rating REAL,'
            'pages INTEGER,'
            'language TEXT,'
            'format TEXT'
            ')'
        )
        connection.commit()
        insert_book(cursor)
        connection.commit()

    if nav == 3:
        pass

    if nav == 4:
        break

cursor.close()
connection.close()
