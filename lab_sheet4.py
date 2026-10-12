import sqlite3

# Connect to database
connection = sqlite3.connect("college.db")

# Create cursor
cursor = connection.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON")

# 1. Create Department table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Department (
    Department_ID INTEGER PRIMARY KEY,
    Department_Name VARCHAR(100) NOT NULL,
    HOD_Name VARCHAR(100)
)
""")

# 2. Create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    Student_ID INTEGER PRIMARY KEY,
    Student_Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    Department_ID INTEGER,

    FOREIGN KEY (Department_ID)
    REFERENCES Department(Department_ID)
)
""")

# 3. Create Course table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Course (
    Course_ID INTEGER PRIMARY KEY,
    Course_Name VARCHAR(100) NOT NULL,
    Credits INTEGER,
    Department_ID INTEGER,

    FOREIGN KEY (Department_ID)
    REFERENCES Department(Department_ID)
)
""")

# 4. Create Enrollment table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    Enrollment_ID INTEGER PRIMARY KEY,
    Student_ID INTEGER,
    Course_ID INTEGER,
    Enrollment_Date DATE,
    Grade VARCHAR(5),

    FOREIGN KEY (Student_ID)
    REFERENCES Student(Student_ID),

    FOREIGN KEY (Course_ID)
    REFERENCES Course(Course_ID)
)
""")

# Save changes
connection.commit()

print("Database and tables created successfully!")

# Display table names
cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table'
""")

tables = cursor.fetchall()

print("\nTables in the database:")
for table in tables:
    print(table[0])

# Close connection
connection.close()
