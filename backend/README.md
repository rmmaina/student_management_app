# Student Management Application (Full Stack)

## Project Overview

This is a full-stack Student Management System built using React for the frontend and Flask for the backend. The application demonstrates CRUD (Create, Read, Update, Delete) operations using REST API communication between the frontend and backend.

The backend stores data in memory and provides API endpoints, while the frontend provides a user interface to interact with the data.

---

## Tech Stack

Frontend:
- React
- JavaScript
- Fetch/Axios for API calls

Backend:
- Python
- Flask
- Flask-CORS

---

## Features

### Student Management
- Add a new student with name and age
- View all students
- Update existing student details
- Delete a student

### System Features
- REST API communication
- Real-time UI updates after each operation
- CORS enabled for frontend-backend communication
- Simple and responsive UI

---

## Project Structure


---

## Backend Setup (Flask)

### Requirements
- Python 3.x
- pip

### Installation

Navigate to backend folder:
cd backend

python -m venv venv
venv\Scripts\activate
Install dependencies:

pip install flask flask-cors

Run the backend server:

python app.py

Backend runs at:http://127.0.0.1:5000


---

## Frontend Setup (React)

### Requirements
- Node.js
- npm

### Installation

Navigate to frontend folder:
cd frontend


Install dependencies:
npm install


Start development server:
npm start


Frontend runs at:http://localhost:3000


---

## API Endpoints

| Method | Endpoint         | Description           |
|--------|------------------|---------------------|
| GET    | /students        | Get all students     |
| GET    | /students/<id>   | Get student by ID    |
| POST   | /students        | Add new student      |
| PUT    | /students/<id>   | Update student       |
| DELETE | /students/<id>  | Delete student       |

---

## How It Works

1. User opens React frontend
2. Frontend sends API requests to Flask backend
3. Backend processes CRUD operations
4. Updated data is returned to frontend
5. UI refreshes automatically after each operation

---

## Important Notes

- Data is stored in memory (not persistent)
- Backend must run before frontend
- Ensure CORS is enabled in Flask
- API base URL must match backend server (http://127.0.0.1:5000)

---

## Learning Outcome

This project demonstrates:
- Full-stack application development
- REST API design and integration
- React state management using hooks
- CRUD operations handling
- Frontend-backend communication
