print("APP.PY IS RUNNING")

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

students = []
current_id = 1

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Get student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s["id"] == id), None)
    return jsonify(student) if student else ("Not Found", 404)

# Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    global current_id
    data = request.json

    student = {
        "id": current_id,
        "name": data["name"],
        "age": data["age"]
    }

    students.append(student)
    current_id += 1

    return jsonify(student), 201

# Update a student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json

    for student in students:
        if student["id"] == id:
            student["name"] = data["name"]
            student["age"] = data["age"]
            return jsonify(student)

    return ("Not Found", 404)

# Delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [s for s in students if s["id"] != id]
    return ("Deleted", 200)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)

