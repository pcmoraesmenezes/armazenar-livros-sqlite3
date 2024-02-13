import sqlite3
from configs import (
    TABLE_NAME,
    DB_FILE,
    AUTHORS_TABLE,
    GENRES_TABLE,
    LANGUAGES_TABLE
)


def update_language_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    option = int(input('Choose the language id to update: '))
    new_language = input('New language name: ')

    cursor.execute(
        f"UPDATE {LANGUAGES_TABLE} SET name = ? WHERE id = ?;",
        (new_language, option)
    )

    connection.commit()
    connection.close()


def update_genre_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    option = int(input('Choose the genre id to update: '))
    new_genre = input('New genre name: ')

    cursor.execute(
        f"UPDATE {GENRES_TABLE} SET name = ? WHERE id = ?;",
        (new_genre, option)
    )

    connection.commit()
    connection.close()


def update_author_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    option = int(input('Choose the author id to update: '))
    new_author = input('New author name: ')

    cursor.execute(
        f"UPDATE {AUTHORS_TABLE} SET name = ? WHERE id = ?;",
        (new_author, option)
    )

    connection.commit()
    connection.close()


def table_book():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    option = int(input('Choose the book id to update: '))
    print('Choose the field to update: ')
    print('1 - Title')
    print('2 - Author')
    print('3 - Genre')
    print('4 - Start Date')
    print('5 - End Date')
    print('6 - Rating')
    print('7 - Pages')
    print('8 - Language')
    print('9 - Format')
    field = input()

    if field == '1':
        new_title = input('New title: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET title = ? WHERE id = ?;",
            (new_title, option)
        )
    elif field == '2':
        new_author = input('New author id: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET id_author = ? WHERE id = ?;",
            (new_author, option)
        )
    elif field == '3':
        new_genre = input('New genre id: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET id_genre = ? WHERE id = ?;",
            (new_genre, option)
        )
    elif field == '4':
        new_start_date = input('New start date: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET start_date = ? WHERE id = ?;",
            (new_start_date, option)
        )
    elif field == '5':
        new_end_date = input('New end date: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET end_date = ? WHERE id = ?;",
            (new_end_date, option)
        )
    elif field == '6':
        new_rating = input('New rating: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET rating = ? WHERE id = ?;",
            (new_rating, option)
        )
    elif field == '7':
        new_pages = input('New pages: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET pages = ? WHERE id = ?;",
            (new_pages, option)
        )
    elif field == '8':
        new_language = input('New language id: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET id_language = ? WHERE id = ?;",
            (new_language, option)
        )
    elif field == '9':
        new_format = input('New format id: ')
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET id_format = ? WHERE id = ?;",
            (new_format, option)
        )
    else:
        print('Invalid option')
        table_book()

    connection.commit()
    connection.close()


def update_table():
    print('Which table do you want to update?')
    print('1 - Authors')
    print('2 - Genres')
    print('3 - Languages')
    print('4 - Books')
    option = input()

    if option == '1':
        update_author_table()
    elif option == '2':
        update_genre_table()
    elif option == '3':
        update_language_table()
    elif option == '4':
        table_book()
    else:
        print('Invalid option')
        update_table()
