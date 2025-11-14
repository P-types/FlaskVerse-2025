# FlaskVerse-2025
# Student Management System (Flask Project)

This is a beginner-friendly **Flask web application** built for learning purposes.  
It covers all the basic concepts of Flask including routing, templates, form handling, sessions (login), and SQLite database operations.

The project allows a faculty/teacher to:
- Log in securely  
- Add new students  
- View all students  
- Update student details  
- Delete student records  
- Filter students by marks  
- Search students by name or roll number  

The UI is designed using a modern **glassmorphism theme** with glowing effects.

---

## 🔥 Features

### ✔ Authentication System
- Login page using Flask sessions  
- Only logged-in users can access all pages  
- Logout option clears the session  

### ✔ Student CRUD Operations
- **C**reate: Add student
- **R**ead: Display all student records
- **U**pdate: Edit existing student details
- **D**elete: Remove student record

### ✔ Search and Filter
- Filter students based on marks range  
- Search by name or roll number  

### ✔ Beautiful Frontend
- Glass UI  
- Neon gradient backgrounds  
- Same theme across all pages  

---

## 📁 Project Structure

FLASKVERSE/
│── app.py # Main Flask application
│── students.db # SQLite database file
│── setup_db.py # Script to create database/table
│
├── templates/ # All HTML pages (Jinja templates)
│ ├── login.html # Login screen
│ ├── home.html # Dashboard
│ ├── add.html # Add student form
│ ├── list.html # List all students
│ ├── edit.html # Edit student details
│ ├── filter.html # Filter students by marks
│ └── search.html # Search student records
│
└── static/
└── style.css # Global CSS (glass theme)

## 🎓 What You Will Learn From This Project

This project is ideal for beginners who want to learn Flask by building a real web application.  
Here’s everything you will understand by studying and running this project:

### 🔹 Flask Routing
How `@app.route` connects URLs to Python functions.

### 🔹 Jinja2 Templates
How dynamic HTML pages work with:
- `{{ variables }}`
- `{% loops %}`
- `{% conditions %}`

### 🔹 Form Handling
How to read values from input forms using:
