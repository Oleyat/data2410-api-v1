from db.db import DatabaseManager
from flask import Flask, jsonify
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / 'db' / 'students.db'
database = DatabaseManager(str(DB_PATH))


def getAllStudents():
    with database as cursor:
        cursor.execute('SELECT * FROM users')
        students = cursor.fetchall()
        return jsonify([dict(student) for student in students])

def getStudentById(student_id):
    with database as cursor:
        cursor.execute('SELECT * FROM users WHERE id = ?', (student_id,))
        student = cursor.fetchone()
        if student:
            return jsonify(dict(student))
        else:
            return jsonify({'error': 'Student not found'}), 404

def create_student(student_data):
    with database as cursor:
        cursor.execute('INSERT INTO users (name, course, marks) VALUES (?, ?, ?)', (student_data['name'], student_data['course'], student_data['marks']))
        database.commit()
        return jsonify({'message': 'Student created successfully'}), 201

def update_student(student_id, student_data):
    with database as cursor:
        cursor.execute('UPDATE users SET name = ?, course = ?, marks = ? WHERE id = ?', (student_data['name'], student_data['course'], student_data['marks'], student_id))
        database.commit()
        return jsonify({'message': 'Student updated successfully'}), 200

def delete_student(student_id):
    with database as cursor:
        cursor.execute('DELETE FROM users WHERE id = ?', (student_id,))
        database.commit()
        return jsonify({'message': 'Student deleted successfully'}), 200

def student_calculate_grades():
    students = getAllStudents().json
    for student in students:
        student["grade"] = get_grade(student["marks"])
    return students

def update_grades(student_id, student_data):
    with database as cursor:
        cursor.execute('UPDATE users SET grade = ? WHERE id = ?', (student_data['grade'], student_id))
        database.commit()

def get_grade(marks):
    return (
        "A" if marks >= 90 else
        "B" if marks >= 80 else
        "C" if marks >= 60 else
        "D"
    )

def coursewise_report():
    with database as cursor:
        data = cursor.execute("""
        SELECT 
            course,
            COUNT(id) AS total_students,
            AVG(marks) AS average_marks,
            SUM(CASE WHEN grade = 'A' THEN 1 ELSE 0 END) AS grade_A,
            SUM(CASE WHEN grade = 'B' THEN 1 ELSE 0 END) AS grade_B,
            SUM(CASE WHEN grade = 'C' THEN 1 ELSE 0 END) AS grade_C,
            SUM(CASE WHEN grade = 'D' THEN 1 ELSE 0 END) AS grade_D
        FROM users
        GROUP BY course
    """)
        rows = cursor.fetchall()
    report = []
    for row in rows:    
        report.append({
            "courseName": row[0],
            "totalStudents": row[1],
            "averageMarks": round(row[2], 2),
            "gradeDistribution": {
                "A": row[3], "B": row[4], "C": row[5], "D": row[6]
            }
        })
    return jsonify(report)

def get_health():
    with database as cursor:
        cursor.execute('SELECT 1')
        return jsonify({'status': 'healthy'}), 200
    return jsonify({'status': 'unhealthy'}), 500
