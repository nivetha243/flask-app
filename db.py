import sqlite3

def view_users():
    conn = sqlite3.connect('nivi.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def user_check(st):
    conn = sqlite3.connect('nivi.db')
    cursor = conn.cursor()
    cursor.execute(st)
    rows = cursor.fetchall()
    print(rows, 'rowsss')
    for row in rows:
        print(row)
    conn.close()

def delete_all_users():
    conn = sqlite3.connect('nivi.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users')
    conn.commit()
    print("All users have been deleted.")
    conn.close()


if __name__ == '__main__':
    # Example usage
    view_users()
    # n = int(input("give me a number of query"))
    # st = str(input("enter the query"))
    # for i in range((n)):
    #     user_check(st)

    confirm = input("Are you sure you want to delete all users? (yes/no): ")
    if confirm.lower() == 'yes':
        delete_all_users()
    view_users()
