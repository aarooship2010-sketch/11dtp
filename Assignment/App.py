# Import the sqlite3 library so Python can work with databases
import sqlite3

# Define the database filename as a constant variable
DATABASE = "grades.db"


# FUNCTION 1: Print all students

def print_all_students():
    # Open a connection to the database file
    db = sqlite3.connect(DATABASE)
    # Create a cursor object to send your commands
    cursor = db.cursor()
    
    # Write the SQL query to select everything from the Students table
    cursor.execute("SELECT * FROM Students;")
    # Grab all the resulting rows from the query and save them in results
    results = cursor.fetchall()
    
    # Print the column text headers on the screen
    print("\nID        Name                 Gender       Ethnicity")
    
    # Loop through each individual student row in the results list
    for student in results:
        # Print the student details with clean spacing between columns
        print(f"{student[0]:<10}{student[1]:<21}{student[2]:<13}{student[3]}")
    
    # Close the database connection to clean up
    db.close()

# FUNCTION 2: Search student grades

def search_student_grades():
    # Open a connection to the database file
    db = sqlite3.connect(DATABASE)
    # Create a cursor object to send commands
    cursor = db.cursor()
    
    # Ask the user to type in a Student ID number
    search_id = input("\nEnter Student ID: ").strip()
    
    # Write the relational query that joins all three tables together based on ID matches
    sql = """
    SELECT Students.Name, Classes.name, Assignments.name, Assignments.marks, Assignments.Grade
    FROM Assignments
    JOIN Students ON Assignments.Student_id = Students.student_id
    JOIN Classes ON Assignments.Class_id = Classes.Class_id
    WHERE Students.student_id = ?;
    """
    # Run the query, safely replacing the '?' with the ID the user typed in
    cursor.execute(sql, (search_id,))
    # Grab all matching grade rows and store them in 'results'
    results = cursor.fetchall()
    
    # Check if the database actually found any matching rows
    if results:
        # Print the name of the student
        print(f"\nGrades for {results[0][0]}:")
        # Loop through each grade record found for that student
        for row in results:
            # Print the class code, assignment name, numeric mark, and letter grade
            print(f"Class: {row[1]} | Assignment: {row[2]} | Mark: {row[3]}% | Grade: {row[4]}")
    # If no matching rows were found in the database
    else:
        # Print an error message
        print("No records found.")
        
    # Close the database connection safely
    db.close()




# MAIN MENU LOOP

while True:
    # Print the three main menu choices
    print("\n1. Print all students")
    print("2. Search student grades")
    print("3. Exit")
    
    # Ask the user to type their choice and remove any extra spaces
    user_input = input("Select 1, 2, or 3: ").strip()
    
    # If the user typed "1", run the print_all_students function
    if user_input == "1":
        print_all_students()
    # If the user typed "2", run the search_student_grades function
    elif user_input == "2":
        search_student_grades()
    # If the user typed "3", break out of the while loop to close the program
    elif user_input == "3":
        break
    # If the user typed anything else, show an error message
    else:
        print("Not an option.")