import sqlite3

def create_database():
    conn = sqlite3.connect('registery.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            height REAL,
            weight REAL,
            gender TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
