import sqlite3
from insert_on_table import insert_table
from update_table import update_table
from configs import TABLE_NAME, DB_FILE, print_text, print_horizontal_line
from configs import clear_terminal, print_table_after_changes
from read_table import read_table


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "title TEXT NOT NULL,"
    "author TEXT NOT NULL,"
    "genre TEXT,"
    "start_date DATE,"
    "end_date DATE,"
    "rating REAL,"
    "pages INTEGER,"
    "language TEXT,"
    "format TEXT"
    ")"
)
connection.commit()
while True:
    print_horizontal_line()
    print_text()
    print("To View your DataBase press (1)")
    print("To Update your DataBase press (2)")
    print("To Insert in your DataBase press (3)")
    print("To exit press (4)")
    nav = input()

    if nav == '1':
        clear_terminal()
        while True:
            read_table()
            print('\nDo you want to see another information? Yes or No')
            nav = input()

            if nav.lower() == 'y' or nav.lower() == 'yes':
                pass
            else:
                print('Are you sure? ')
                nav = input()

                if nav.lower() == 'y' or nav.lower() == 'yes':
                    break

    if nav == '2':
        clear_terminal()
        while True:
            update_table()
            print('Do you want to change something else? Yes or No')
            nav = input()
            if nav.lower() == 'y' or nav.lower() == 'yes':
                pass
            else:
                print('Are you sure? Yes or No ')
                nav = input()
                if nav.lower() == 'y' or nav.lower() == 'yes':
                    print('Table after changes:')
                    print_table_after_changes()
                    break
    if nav == '3':
        clear_terminal()
        while True:
            insert_table()
            print('Do you want to insert more informations? Yes or No ')
            nav = input()
            if nav.lower() == 'y' or nav.lower() == 'yes':
                pass
            else:
                print('Are you sure? Yes or No')
                nav = input()
                if nav.lower() == 'y' or nav.lower() == 'yes':
                    print('Table after changes: ')
                    print_table_after_changes()
                    break
                pass

    if nav == '4':
        break

cursor.close()
connection.close()
