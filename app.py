from fastapi import FastAPI
import sqlite3

app = FastAPI()

def execute_query(query: str, params=()):
    """Execute a database query and return results."""
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

@app.get("/")
async def home():
    return {"message": "Welcome to the SQLite Chat Assistant!"}

@app.get("/query/")
async def query_database(user_query: str):
    try:
        user_query = user_query.lower()

        if "employees in" in user_query:
            department = user_query.split("employees in ")[1].strip().capitalize()
            query = "SELECT Name FROM Employees WHERE Department = ?"
            results = execute_query(query, (department,))
            return {"employees": [row[0] for row in results]} if results else {"message": "No employees found in this department."}

        elif "manager of" in user_query:
            department = user_query.split("manager of ")[1].strip().capitalize()
            query = "SELECT Manager FROM Departments WHERE Name = ?"
            results = execute_query(query, (department,))
            return {"manager": results[0][0]} if results else {"message": "Department not found."}

        elif "hired after" in user_query:
            date = user_query.split("hired after ")[1].strip()
            query = "SELECT Name FROM Employees WHERE Hire_Date > ?"
            results = execute_query(query, (date,))
            return {"employees": [row[0] for row in results]} if results else {"message": "No employees hired after this date."}

        elif "total salary expense for" in user_query:
            department = user_query.split("expense for ")[1].strip().capitalize()
            query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
            results = execute_query(query, (department,))
            return {"total_salary_expense": results[0][0]} if results[0][0] else {"message": "Department not found."}

        else:
            return {"message": "Invalid query. Try another format."}

    except Exception as e:
        return {"error": str(e)}
