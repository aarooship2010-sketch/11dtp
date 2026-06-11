# Import the sqlite3 library so Python can work with databases
import sqlite3

# Define the database filename as a constant variable
DATABASE_NAME = "grades.db"


# ==========================================
# MASTER BLUEPRINT FUNCTION (The "Mold")
# ==========================================

def run_query(sql, parameters=()):
    """
    Acts as the master structure for all database actions.
    It handles the repetitive setup, execution, and cleanup,
    using parameters to dynamically inject unique SQL queries and data.
    """
    # Open a connection to the database file
    db = sqlite3.connect(DATABASE_NAME)
    # Create a cursor object to send commands
    cursor = db.cursor()
    
    # Run the SQL query with its corresponding data parameters
    cursor.execute(sql, parameters)
    # Grab all matching records from the database
    results = cursor.fetchall()
    
    # Close the database connection safely to prevent file locking
    db.close()
    # Return the records back to the function that requested them
    return results


# ==========================================
# MENU FUNCTIONS (Filling in the parameters)
# ==========================================

# FUNCTION 1: Print all students
def print_all_students():
    # Define the static query to pull all student records
    sql = "SELECT * FROM Students;"
    # Call the master blueprint to fetch the records
    ds_students = run_query(sql)
    
    # Print the column text headers on the screen
    print("\nID        Name                 Gender       Ethnicity")
    
    # Loop through each individual student row in the results list
    for student in ds_students:
        # Print the student details with clean spacing between columns
        print(f"{student[0]:<10}{student[1]:<21}{student[2]:<13}{student[3]}")


# FUNCTION 2: Search student grades
def search_student_grades():
    # Ask the user to type in a Student ID number
    search_id = input("\nEnter Student ID: ").strip()
    
    # Write the relational query that joins all three tables together
    sql = """
    SELECT Students.Name, Classes.name, Assignments.name, Assignments.marks, Assignments.Grade
    FROM Assignments
    JOIN Students ON Assignments.Student_id = Students.student_id
    JOIN Classes ON Assignments.Class_id = Classes.Class_id
    WHERE Students.student_id = ?;
    """
    # Pass the SQL statement and the search ID parameter as a tuple
    results = run_query(sql, (search_id,))
    
    # Check if the database actually found any matching rows
    if results:
        # Print the name of the student (grabbed from the first row)
        print(f"\nGrades for {results[0][0]}:")
        # Loop through each grade record found for that student
        for row in results:
            # Print the class code, assignment name, numeric mark, and letter grade
            print(f"Class: {row[1]} | Assignment: {row[2]} | Mark: {row[3]}% | Grade: {row[4]}")
    else:
        # Print an error message if no data came back
        print("No records found.")


# FUNCTION 3: Calculate a Student's Subject Average
def calculate_subject_average():
    # Ask the user for the Student ID and the Subject name
    search_id = input("\nEnter Student ID: ").strip()
    search_subject = input("Enter Subject (e.g., Math, Science): ").strip()
    
    # Write the query using AVG() to calculate the mathematical average
    sql = """
    SELECT Students.Name, AVG(Assignments.marks)
    FROM Assignments
    JOIN Students ON Assignments.Student_id = Students.student_id
    JOIN Classes ON Assignments.Class_id = Classes.Class_id
    WHERE Students.student_id = ? AND Classes.Subject LIKE ?;
    """
    # Send both parameters over to the master function in order
    results = run_query(sql, (search_id, search_subject))
    
    # Extract the first matching row from our results list if it exists
    result = results[0] if results else None
    
    # Check if a student name was found and the calculated average is not empty
    if result and result[0] is not None and result[1] is not None:
        # Round the average to 1 decimal place and print the result
        print(f"\n{result[0]}'s current average for {search_subject} is: {round(result[1], 1)}%")
    else:
        print("No records found for that student and subject combination.")


# FUNCTION 4: Sort all Grades Chronologically for a specific subject
def sort_grades_chronologically():
    # Ask the user for the Subject name
    search_subject = input("\nEnter Subject (e.g., Math, Science): ").strip()
    
    # Select the data and sort strictly by the completion date field
    sql = """
    SELECT Assignments.date, Students.Name, Assignments.name, Assignments.marks, Assignments.Grade
    FROM Assignments
    JOIN Students ON Assignments.Student_id = Students.student_id
    JOIN Classes ON Assignments.Class_id = Classes.Class_id
    WHERE Classes.Subject LIKE ?
    ORDER BY Assignments.date ASC;
    """
    # Feed the subject parameter into the master function
    results = run_query(sql, (search_subject,))
    
    # Check if the database actually found any matching rows
    if results:
        print(f"\nResults in Chronological Order for {search_subject}:")
        # Loop through each record found
        for row in results:
            # Print the line formatted with the date first so the rows flow in time order
            print(f"Date: {row[0]} | Student: {row[1]} | Assignment: {row[2]} | Mark: {row[3]}% | Grade: {row[4]}")
    else:
        print("No records found for that subject.")


# ==========================================
# MAIN MENU LOOP
# ==========================================

while True:
    # Print the five main menu choices
    print("\n1. Print all students")
    print("2. Search student grades")
    print("3. Calculate subject average")
    print("4. Sort grades chronologically")
    print("5. Exit")
    
    # Ask the user to type their choice and remove any extra spaces
    user_input = input("Select 1, 2, 3, 4, or 5: ").strip()
    
    # Route the user input to the correct function call
    if user_input == "1":
        print_all_students()
    elif user_input == "2":
        search_student_grades()
    elif user_input == "3":
        calculate_subject_average()
    elif user_input == "4":
        sort_grades_chronologically()
    elif user_input == "5":
        print("\nThank you for using the Grades Database System. Goodbye!")
        break
    else:
        print("Not an option.")