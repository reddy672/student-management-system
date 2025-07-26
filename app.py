from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Initialize DB
def init_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks INTEGER,
            attendance INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Routes
@app.route('/students', methods=['GET'])
def get_students():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1], "marks": r[2], "attendance": r[3]} for r in rows])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, marks, attendance) VALUES (?, ?, ?)",
                (data['name'], data['marks'], data['attendance']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student added"})
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('''
        UPDATE students
        SET name = ?, marks = ?, attendance = ?
        WHERE id = ?
    ''', (data['name'], data['marks'], data['attendance'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student updated"})


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student deleted"})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
