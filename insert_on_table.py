import sqlite3
from configs import TABLE_NAME, DB_FILE


def insert_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    sql = (
        f'INSERT INTO {TABLE_NAME} '
        '(title, author, genre, start_date, end_date,'
        'rating, pages, language, format) '
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
    )
    title = input('Title: ')
    author = input('Author: ')
    genre = input('Genre: ')
    start_date = input('start_date: ')
    end_date = input('end_date: ')
    rating = input('rating: ')
    pages = input('Pages: ')
    language = input('language: ')
    book_format = input('book_format: ')

    values = (title, author, genre, start_date, end_date, rating,
              pages, language, book_format)

    cursor.execute(sql, values)
    connection.commit()

    cursor.close()
    connection.close()
