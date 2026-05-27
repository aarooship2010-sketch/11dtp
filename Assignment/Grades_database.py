import sqlite3

# 1. Connect to the new database file
conn = sqlite3.connect('grades.db')
cursor = conn.cursor()

# Enable Foreign Keys
cursor.execute("PRAGMA foreign_keys = ON;")

# ==========================================
# 2. CREATE TABLES
# ==========================================

# Create Students Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Gender TEXT,
    Ethnicity TEXT
)
''')

# Create Classes Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Classes (
    Class_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    Subject TEXT NOT NULL,
    Teacher_name TEXT,
    Year TEXT
)
''')

# Create Assignments Table (with working links/Foreign Keys)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Assignments (
    Assignment_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    Class_id INTEGER,
    Student_id INTEGER,
    date TEXT,
    marks INTEGER,
    Grade TEXT,
    FOREIGN KEY (Student_id) REFERENCES Students(student_id),
    FOREIGN KEY (Class_id) REFERENCES Classes(Class_id)
)
''')

# ==========================================
# 3. INSERT RECONSTRUCTION SAMPLE DATA
# ==========================================

# Mock Student Data
students_data = [
    (1001, 'Liam Smith', 'Male', 'European'),
    (1002, 'Aroha Te Ao', 'Female', 'Māori'),
    (1003, 'Chloe Wang', 'Female', 'Asian')
]

# Mock Class Data
classes_data = [
    (201, '11MAT_A', 'Math', 'Mr. Harrison', '2026'),
    (204, '11SCI_1', 'Science', 'Dr. Reynolds', '2026'),
    (208, '11HIS_A', 'History', 'Mrs. Fitzgerald', '2026')
]

# Mock Assignment Data (Linked back to the students and classes above)
assignments_data = [
    (5001, 'Quiz 1', 201, 1001, '2026-02-15', 85, 'A'),
    (5002, 'Midterm Exam', 201, 1001, '2026-04-10', 92, 'E'),
    (5003, 'Lab Report 1', 204, 1001, '2026-02-28', 78, 'M'),
    (5004, 'Quiz 1', 201, 1002, '2026-02-15', 90, 'E'),
    (5005, 'Lab Report 1', 204, 1002, '2026-02-28', 88, 'E'),
    (5006, 'Midterm Exam', 204, 1002, '2026-04-12', 81, 'M'),
    (5007, 'Essay 1', 208, 1003, '2026-03-05', 95, 'E'),
    (5008, 'Essay 1', 208, 1001, '2026-03-05', 63, 'A')
]

# Insert data safely (INSERT OR IGNORE avoids errors if run twice)
cursor.executemany("INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?)", students_data)
cursor.executemany("INSERT OR IGNORE INTO Classes VALUES (?, ?, ?, ?, ?)", classes_data)
cursor.executemany("INSERT OR IGNORE INTO Assignments VALUES (?, ?, ?, ?, ?, ?, ?)", assignments_data)

# Commit changes and shut down cleanly
conn.commit()
conn.close()

print("🎉 Success! 'grades.db' has been rebuilt and populated with fresh records.")