from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    course = db.Column(db.String(100))


@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    result = []

    for student in students:
        result.append({
            "id": student.id,
            "name": student.name,
            "course": student.course
        })

    return jsonify(result)


@app.route("/students", methods=["POST"])
def add_student():
    data = request.json

    new_student = Student(
        name=data["name"],
        course=data["course"]
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student added"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

#UPDATE Route (Edit Student)

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.json

    student.name = data["name"]
    student.course = data["course"]

    db.session.commit()

    return jsonify({"message": "Student updated"})

#DELETE Route (Delete Student)
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted"})
