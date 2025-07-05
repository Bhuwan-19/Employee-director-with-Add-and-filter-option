import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        department TEXT
    )
''')

employees = [
    ('Alice Johnson', 'alice@example.com', '1234567890', 'HR'),
    ('Bob Smith', 'bob@example.com', '9876543210', 'Engineering'),
    ('Carol White', 'carol@example.com', '5555555555', 'Marketing'),
]

cursor.executemany('INSERT INTO employees (name, email, phone, department) VALUES (?, ?, ?, ?)', employees)
conn.commit()
conn.close()
