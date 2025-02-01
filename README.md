# Department Management System

## Overview
This project is a Department Management System designed to manage departments, employees, tasks, and performance efficiently within an organization.

## Features
- **Department Management**: Create, update, and delete departments.
- **User Authentication**: User registration, login, and logout functionality.
- **Task Management**: Assign and manage tasks for each department.
- **Responsive Design**: User-friendly interface optimized for various devices.
- **Role-Based Access**: Separate access for administrators and employees.

## Technologies Used
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python (Django Framework)
- **Database**: MySQL
- **Other Tools**: Django Admin Panel, SMTP for email functionality

## Installation Guide

### Prerequisites
- Python (v3.8 or higher)
- MySQL Database
- A working internet connection

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/department-management.git
   ```
2. Navigate to the project folder:
   ```bash
   cd department-management
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - Open `settings.py` and configure your database credentials under `DATABASES`.
   - Run the following commands:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Usage
- **Register**: Create a user account via the registration page.
- **Login**: Use your credentials to log in.
- **Manage Departments**: Add, edit, or delete departments from the dashboard.
- **Task Assignment**: Assign and track tasks in real-time.

## Deployment
You can deploy this project on platforms like **Heroku**, **AWS**, or **PythonAnywhere**. For local testing, use Django's built-in development server.

## Contact
- **Email**: [umme2509@example.com](mailto:umme2509@example.com)
- **GitHub**: [https://github.com/Umme797](https://github.com/Umme797)
