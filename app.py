from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'registery.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        height = request.form['height']
        weight = request.form['weight']
        gender = request.form['gender']

        conn = get_db_connection()
        conn.execute('INSERT INTO users (first_name, last_name, email, height, weight, gender) VALUES (?, ?, ?, ?, ?, ?)',
                     (first_name, last_name, email, height, weight, gender))
        conn.commit()
        conn.close()

        return redirect('/')
    
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)

