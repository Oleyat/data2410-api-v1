from flask import Flask

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

    

if __name__ == "__main__":
    app.run(debug=True)