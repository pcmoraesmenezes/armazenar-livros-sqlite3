import sqlite3
from configs import TABLE_NAME, DB_FILE


def update_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    print("Available columns to update:")
    print("1. Title")
    print("2. Author")
    print("3. Genre")
    print("4. Start Date")
    print("5. End Date")
    print("6. Rating")
    print("7. Pages")
    print("8. Language")
    print("9. Format")

    column_choice = int(input("Select the column to update (1-9): "))
    new_value = input("Enter the new value: ")

    columns = [
        'title', 'author', 'genre', 'start_date', 'end_date',
        'rating', 'pages', 'language', 'format'
    ]

    selected_column = columns[column_choice - 1]

    record_id = int(input('Enter the ID of the record to update: '))

    sql = f'UPDATE {TABLE_NAME} SET {selected_column}=? WHERE id=?'
    values = (new_value, record_id)

    cursor.execute(sql, values)

    connection.commit()

    cursor.close()
    connection.commit()
