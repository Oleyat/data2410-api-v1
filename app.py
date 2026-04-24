from flask import Flask

app = Flask(__name__)

@app.route('/api/Students', methods=['GET'])
def get_students():
    return "students"

if __name__ == "__main__":
    app.run(debug=True)