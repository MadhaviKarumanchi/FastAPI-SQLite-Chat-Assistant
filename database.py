import sqlite3

def create_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    # Create Employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Department TEXT NOT NULL,
            Salary INTEGER NOT NULL,
            Hire_Date TEXT NOT NULL
        )
    ''')

    # Create Departments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Manager TEXT NOT NULL
        )
    ''')

    # Insert sample data only if table is empty
    cursor.execute("SELECT COUNT(*) FROM Employees")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES ('Alice', 'Sales', 50000, '2021-01-15')")
        cursor.execute("INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES ('Bob', 'Engineering', 70000, '2020-06-10')")
        cursor.execute("INSERT INTO Employees (Name, Department, Salary, Hire_Date) VALUES ('Charlie', 'Marketing', 60000, '2022-03-20')")

    cursor.execute("SELECT COUNT(*) FROM Departments")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Departments (Name, Manager) VALUES ('Sales', 'Alice')")
        cursor.execute("INSERT INTO Departments (Name, Manager) VALUES ('Engineering', 'Bob')")
        cursor.execute("INSERT INTO Departments (Name, Manager) VALUES ('Marketing', 'Charlie')")

    # Remove duplicate employees while keeping the first occurrence
    cursor.execute("""
        DELETE FROM Employees WHERE ID NOT IN (
            SELECT MIN(ID) FROM Employees GROUP BY Name, Department, Salary, Hire_Date
        )
    """)

    # Remove duplicate departments while keeping the first occurrence
    cursor.execute("""
        DELETE FROM Departments WHERE ID NOT IN (
            SELECT MIN(ID) FROM Departments GROUP BY Name, Manager
        )
    """)

    conn.commit()
    conn.close()  # Close connection at the end

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
