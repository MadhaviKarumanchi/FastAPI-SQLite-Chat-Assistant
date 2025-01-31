# FastAPI-SQLite-Chat-Assistant


## Overview
This is a simple chatbot-style API built with **FastAPI** and **SQLite**. It allows users to query employee and department-related information from an SQLite database using natural language.

## Features
- Retrieve employees from a specific department
- Get the manager of a department
- List employees hired after a specific date
- Calculate the total salary expense for a department

## Installation & Setup

### Prerequisites
- Python 3.7+
- FastAPI
- SQLite3

### Install Dependencies
```bash
pip install fastapi uvicorn
```

### Run the Server
```bash
uvicorn main:app --reload
```

## API Endpoints & Example Queries

### Get all employees in the Sales department
**URL:**  
`http://127.0.0.1:8000/query/?user_query=Show me all employees in Sales`

**Response:**
```json
{
  "employees": ["Alice"]
}
```

### Get the manager of Engineering
**URL:**  
`http://127.0.0.1:8000/query/?user_query=Who is the manager of Engineering`

**Response:**
```json
{
  "manager": "Bob"
}
```

### Employees hired after 2021-01-01
**URL:**  
`http://127.0.0.1:8000/query/?user_query=List all employees hired after 2021-01-01`

**Response:**
```json
{
  "employees": ["Alice", "Charlie"]
}
```

### Total salary expense for Marketing
**URL:**  
`http://127.0.0.1:8000/query/?user_query=What is the total salary expense for Marketing`

**Response:**
```json
{
  "total_salary_expense": 60000
}
```

## Database Schema
### Employees Table
| Column     | Type    | Description           |
|------------|--------|-----------------------|
| ID         | INTEGER | Primary Key          |
| Name       | TEXT    | Employee Name        |
| Department | TEXT    | Department Name      |
| Salary     | INTEGER | Employee Salary      |
| Hire_Date  | TEXT    | Date of Hiring       |

### Departments Table
| Column  | Type    | Description          |
|---------|--------|----------------------|
| ID      | INTEGER | Primary Key         |
| Name    | TEXT    | Department Name     |
| Manager | TEXT    | Department Manager  |


