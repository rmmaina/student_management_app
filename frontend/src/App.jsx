import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [students, setStudents] = useState([]);
  const [name, setName] = useState("");
  const [course, setCourse] = useState("");
  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:5000/students"
      );

      setStudents(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const addOrUpdateStudent = async () => {
    try {

      if (editingId) {

        await axios.put(
          `http://127.0.0.1:5000/students/${editingId}`,
          {
            name,
            course,
          }
        );

        setEditingId(null);

      } else {

        await axios.post(
          "http://127.0.0.1:5000/students",
          {
            name,
            course,
          }
        );

      }

      setName("");
      setCourse("");

      fetchStudents();

    } catch (error) {
      console.log(error);
    }
  };

  const editStudent = (student) => {
    setName(student.name);
    setCourse(student.course);
    setEditingId(student.id);
  };

  const deleteStudent = async (id) => {
    try {

      await axios.delete(
        `http://127.0.0.1:5000/students/${id}`
      );

      fetchStudents();

    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Student Management App</h1>

      <input
        type="text"
        placeholder="Student Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <input
        type="text"
        placeholder="Course"
        value={course}
        onChange={(e) => setCourse(e.target.value)}
      />

      <br /><br />

      <button onClick={addOrUpdateStudent}>
        {editingId ? "Update Student" : "Add Student"}
      </button>

      <hr />

      {students.map((student) => (
        <div
          key={student.id}
          style={{
            border: "1px solid gray",
            padding: "10px",
            marginBottom: "10px"
          }}
        >
          <h3>{student.name}</h3>
          <p>{student.course}</p>

          <button
            onClick={() => editStudent(student)}
          >
            Edit
          </button>

          <button
            onClick={() => deleteStudent(student.id)}
            style={{ marginLeft: "10px" }}
          >
            Delete
          </button>

        </div>
      ))}
    </div>
  );
}

export default App;