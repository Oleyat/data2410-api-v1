from db.db import DatabaseManager
from flask import Flask, jsonify

database = DatabaseManager('../db/students.db')

def getAllStudents():
    with database as cursor:
        cursor.execute('SELECT * FROM users')
        students = cursor.fetchall()
        return jsonify([dict(student) for student in students])