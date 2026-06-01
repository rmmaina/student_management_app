Student Management System

A full-stack student management application built with React and Flask that allows users to create, manage, update, and delete student records through a responsive web interface.
________________________________________
Features

•	Create student records
•	View all students
•	Update existing student information
•	Delete student records
•	RESTful API integration
•	Persistent SQLite database
•	Full CRUD functionality
•	Frontend and backend integration
________________________________________
Tech Stack

Frontend
•	React
•	Vite
•	Axios
Backend
•	Flask
•	Flask-CORS
•	Flask-SQLAlchemy
Database
•	SQLite
________________________________________
Project Structure
student-management-app/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── students.db
│   └── venv/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
________________________________________
Installation

1. Clone the Repository
git clone <repository-url>
Move into the project folder:
cd student-management-app
________________________________________
Backend Setup

Navigate to the backend directory:
cd backend
Create a virtual environment:
python -m venv venv
Activate the virtual environment:
Windows (Git Bash)

source venv/Scripts/activate
Install backend dependencies:
pip install -r requirements.txt
Run the Flask server:
python app.py
The backend server will run on:
http://127.0.0.1:5000
________________________________________
Frontend Setup

Open a new terminal and navigate to the frontend directory:
cd frontend
Install frontend dependencies:
npm install
Start the React development server:
npm run dev
The frontend application will run on:
http://localhost:5173
________________________________________


API Endpoints

Method	Endpoint	Description
GET	/students	Retrieve all students
POST	/students	Create a new student
PUT	/students/:id	Update student information
DELETE	/students/:id	Delete a student
________________________________________
Application Workflow

1.	Users enter student information through the React frontend.
2.	Axios sends API requests to the Flask backend.
3.	Flask processes requests and interacts with the SQLite database.
4.	Updated data is returned and displayed in the frontend interface.
________________________________________
CRUD Functionality

Create
Add new student records to the database.
Read
Fetch and display all student records.
Update
Modify existing student information.
Delete
Remove student records permanently.
________________________________________
Future Improvements

•	User authentication
•	Search and filter functionality
•	Responsive UI styling
•	Form validation
•	Pagination
•	Deployment to cloud platforms
________________________________________
Author

Robert Maina
________________________________________
