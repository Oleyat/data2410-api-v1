from flask import Flask, request, jsonify

from Controllers.students import *

app = Flask(__name__)

@app.route('/api/Students', methods=['GET'])
def get_students():
    return getAllStudents()

@app.route('/api/Students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    return getStudentById(student_id)

@app.route('/api/Students', methods=['POST'])
def createStudent():
    studentdata = request.get_json()
    return create_student(studentdata)

@app.route('/api/Students/<int:student_id>', methods=['PUT'])
def updateStudent(student_id):
    studentdata = request.get_json()
    return update_student(student_id, studentdata)

@app.route('/api/Students/<int:student_id>', methods=['DELETE'])
def deleteStudent(student_id):
    return delete_student(student_id)

@app.route("/calculate-grades", methods=["POST"])
def calculate_grades():

    # Beregn og oppdater karakterer
    for student in students:
        student["grade"] = get_grade(student["marks"])

    # Returner alle studenter med karakterer
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)