
from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'employees.db')

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                department TEXT NOT NULL
            )
        """)

def get_employees(search='', department=''):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM employees WHERE name LIKE ? AND department LIKE ?"
        cursor.execute(query, ('%' + search + '%', '%' + department + '%'))
        data = cursor.fetchall()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    search = request.form.get('search', '')
    department = request.form.get('department', '')
    employees = get_employees(search, department)
    return render_template('index.html', employees=employees, search=search, department=department)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    department = request.form['department']
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT INTO employees (name, email, phone, department) VALUES (?, ?, ?, ?)",
                     (name, email, phone, department))
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
