import sqlite3
from configs import (
    DB_FILE,
    TABLE_NAME,
    AUTHORS_TABLE,
    GENRES_TABLE,
    LANGUAGES_TABLE
)


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


def create_database_(cursor, connection):

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {AUTHORS_TABLE}"
        "("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name TEXT NOT NULL"
        ")"

    )

    connection.commit()

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {GENRES_TABLE}"
        "("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name TEXT NOT NULL"
        ")"


    )

    connection.commit()

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {LANGUAGES_TABLE}"
        "("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name TEXT NOT NULL"
        ")"



    )

    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
        "("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "title TEXT NOT NULL,"
        "id_author INTEGER,"
        "id_genre INTEGER,"
        "start_date DATE,"
        "end_date DATE,"
        "rating REAL,"
        "pages INTEGER,"
        "id_language INTEGER,"
        "id_format INTEGER,"
        "FOREIGN KEY (id_author) REFERENCES authors(id),"
        "FOREIGN KEY (id_genre) REFERENCES genres(id),"
        "FOREIGN KEY (id_language) REFERENCES languages(id),"
        "FOREIGN KEY (id_format) REFERENCES formats(id)"
        ")"
    )

    connection.commit()
    cursor.close()
    connection.close()
