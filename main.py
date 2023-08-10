import sqlite3
from insert_on_table import insert_table
# from update_table import update_table
from configs import TABLE_NAME, DB_FILE

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

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
insert_table()

# update_table()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

for row in cursor.fetchall():
    print(row)

cursor.close()
connection.close()
