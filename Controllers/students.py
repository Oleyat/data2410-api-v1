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