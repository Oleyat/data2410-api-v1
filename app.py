from flask import Flask

from Controllers.students import getAllStudents

app = Flask(__name__)

@app.route('/api/Students', methods=['GET'])
def get_students():
    return getAllStudents()

if __name__ == "__main__":
    app.run(debug=True)