from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
from datetime import datetime

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
            marks INTEGER CHECK (marks >= 0 AND marks <= 100),
            attendance INTEGER CHECK (attendance >= 0 AND attendance <= 100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Helper function to validate student data
def validate_student_data(data):
    if not data:
        return False, "No data provided"
    
    if 'name' not in data or not data['name'].strip():
        return False, "Name is required"
    
    if 'marks' not in data:
        return False, "Marks is required"
    
    if 'attendance' not in data:
        return False, "Attendance is required"
    
    try:
        marks = int(data['marks'])
        attendance = int(data['attendance'])
        
        if marks < 0 or marks > 100:
            return False, "Marks must be between 0 and 100"
        
        if attendance < 0 or attendance > 100:
            return False, "Attendance must be between 0 and 100"
            
    except ValueError:
        return False, "Marks and attendance must be numbers"
    
    return True, "Valid"

# Routes
@app.route('/students', methods=['GET'])
def get_students():
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT id, name, marks, attendance FROM students ORDER BY created_at DESC")
        rows = cur.fetchall()
        conn.close()
        
        students = [{"id": r[0], "name": r[1], "marks": r[2], "attendance": r[3]} for r in rows]
        return jsonify(students), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch students", "details": str(e)}), 500

@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.json
        
        # Validate input
        is_valid, message = validate_student_data(data)
        if not is_valid:
            return jsonify({"error": message}), 400
        
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, marks, attendance) VALUES (?, ?, ?)",
                    (data['name'].strip(), int(data['marks']), int(data['attendance'])))
        conn.commit()
        student_id = cur.lastrowid
        conn.close()
        
        return jsonify({"message": "Student added successfully", "id": student_id}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({"error": "Database constraint violation", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Failed to add student", "details": str(e)}), 500

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    try:
        data = request.json
        
        # Validate input
        is_valid, message = validate_student_data(data)
        if not is_valid:
            return jsonify({"error": message}), 400
        
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        
        # Check if student exists
        cur.execute("SELECT id FROM students WHERE id = ?", (id,))
        if not cur.fetchone():
            conn.close()
            return jsonify({"error": "Student not found"}), 404
        
        cur.execute('''
            UPDATE students
            SET name = ?, marks = ?, attendance = ?
            WHERE id = ?
        ''', (data['name'].strip(), int(data['marks']), int(data['attendance']), id))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Student updated successfully"}), 200
    except sqlite3.IntegrityError as e:
        return jsonify({"error": "Database constraint violation", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Failed to update student", "details": str(e)}), 500

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        
        # Check if student exists
        cur.execute("SELECT id FROM students WHERE id = ?", (id,))
        if not cur.fetchone():
            conn.close()
            return jsonify({"error": "Student not found"}), 404
        
        cur.execute("DELETE FROM students WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to delete student", "details": str(e)}), 500

@app.route('/')
def home():
    return jsonify({
        "message": "Student Management System API",
        "version": "1.0",
        "endpoints": {
            "GET /students": "Get all students",
            "POST /students": "Add new student",
            "PUT /students/{id}": "Update student",
            "DELETE /students/{id}": "Delete student"
        }
    }), 200

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 