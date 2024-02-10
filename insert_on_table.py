import sqlite3
from configs import (
    TABLE_NAME,
    DB_FILE,
    clear_terminal,
    AUTHORS_TABLE,
    GENRES_TABLE,
    LANGUAGES_TABLE
)


def insert_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    insertions = {
        "author": f"INSERT INTO {AUTHORS_TABLE} (name) VALUES (?)",
        "genre": f"INSERT INTO {GENRES_TABLE} (name) VALUES (?)",
        "language": f"INSERT INTO {LANGUAGES_TABLE} (name) VALUES (?)",
        "book": f"INSERT INTO {TABLE_NAME} (title, id_author, id_genre, "
                "start_date, end_date, rating, pages, id_language, format) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    }

    try:
        title = input('Title: ')
        author = input('Author: ')
        genre = input('Genre: ')
        start_date = input('Start Date: ')
        end_date = input('End Date: ')
        rating = input('Rating: ')
        pages = input('Pages: ')
        language = input('Language: ')
        book_format = input('Format: ')

        values = (title, author, genre, start_date, end_date, rating,
                  pages, language, book_format)

        clear_terminal()
        print('-'*50, '\nBook that will be inserted:')
        for field, value in zip(['Title', 'Author', 'Genre',
                                'Start Date', 'End Date', 'Rating', 'Pages',
                                 'Language', 'Format'], values):
            print(f"{field}: {value}")

        print('Do you want to change some info? Yes or No?')
        choice = input()

        while choice.lower() in ('yes', 'y'):
            clear_terminal()
            print('Choose the field to change:')
            print('1. Title\n2. Author\n3. Genre\n4. Start Date')
            print('5. End Date\n6. Rating\n7. Pages\n8. Language\n9. Format')
            field_choice = int(input())

            if 1 <= field_choice <= 9:
                new_value = input(f'Enter new {field_choice}: ')
                values = list(values)
                values[field_choice - 1] = new_value
                values = tuple(values)
                print('Field updated.')

            print('Do you want to change another field? Yes or No?')
            choice = input()

        print('Confirm insertion? Yes or No')
        confirm_choice = input()

        clear_terminal()

        if confirm_choice.lower() == 'yes' or confirm_choice.lower() == 'y':
            cursor.execute(sql, values)
            connection.commit()

            clear_terminal()

            print('Book inserted into the database.')
        else:
            clear_terminal()

            print('Insertion cancelled.')

    except Exception as e:
        print('An error occurred:', e)

    finally:
        cursor.close()
        connection.close()
