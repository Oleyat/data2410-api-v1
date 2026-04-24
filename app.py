from flask import Flask, request, jsonify

from Controllers.students import getAllStudents

app = Flask(__name__)

@app.route('/api/Students', methods=['GET'])
def get_students():
    return getAllStudents()

@app.route('/api/Students/{id}', methods=['GET'])
def get_studentID():
    return getStudentbyID()

@app.route('/api/Students', methods=['POST'])
def create_Student():
    studentdata = request.get_json()
    return create_Student(studentdata)

    
@app.route("/calculate-grades", methods=["POST"])
def calculate_grades():

    # Beregn og oppdater karakterer
    for student in students:
        student["grade"] = get_grade(student["marks"])

    # Returner alle studenter med karakterer
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)