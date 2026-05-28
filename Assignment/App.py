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

# FUNCTION 3: Calculate a Student's Subject Average
def calculate_subject_average():
    # Open a connection to the database file
    db = sqlite3.connect(DATABASE)
    # Create a cursor object to send commands
    cursor = db.cursor()
    
    # Ask the user for the Student ID and the Subject name
    search_id = input("\nEnter Student ID: ").strip()
    search_subject = input("Enter Subject (e.g., Math, Science): ").strip()
    
    # Write the query using AVG() to calculate the mathematical average of the marks column
    sql = """
    SELECT Students.Name, AVG(Assignments.marks)
    FROM Assignments
    JOIN Students ON Assignments.Student_id = Students.student_id
    JOIN Classes ON Assignments.Class_id = Classes.Class_id
    WHERE Students.student_id = ? AND Classes.Subject LIKE ?;
    """
    
    # Run the query, replacing the '?' markers with the user's inputs
    cursor.execute(sql, (search_id, search_subject))
    # Grab the resulting row
    result = cursor.fetchone()
    
    # Check if a student name was found and the calculated average is not None
    if result and result[0] is not None and result[1] is not None:
        # Round the average to 1 decimal place and print the result
        print(f"\n{result[0]}'s current average for {search_subject} is: {round(result[1], 1)}%")
    # If no matching assignment scores were found
    else:
        # Print an error message
        print("No records found for that student and subject combination.")
        
    # Close the database connection safely
    db.close()

# FUNCTION 4: Sort all Grades Chronologically for a specific subject
def sort_grades_chronologically():
    # Open a connection to the database file
    db = sqlite3.connect(DATABASE)
    # Create a cursor object to send commands
    cursor = db.cursor()
    
    # Ask the user for the Subject name
    search_subject = input("\nEnter Subject (e.g., Math, Science): ").strip()
    
    # Select the data and tell SQL to sort strictly by the completion date field
    sql = """
    SELECT Assignments.date, Students.Name, Assignments.name, Assignments.marks, Assignments.Grade
    FROM Assignments
    JOIN Students ON Assignments.Student_id = Students.student_id
    JOIN Classes ON Assignments.Class_id = Classes.Class_id
    WHERE Classes.Subject LIKE ?
    ORDER BY Assignments.date ASC;
    """
    
    # Run the query, replacing the '?' marker with the user's input
    cursor.execute(sql, (search_subject,))
    # Grab all matching sorted rows
    results = cursor.fetchall()
    
    # Check if the database actually found any matching rows
    if results:
        # Print the success message header
        print(f"\nResults in Chronological Order for {search_subject}:")
        # Loop through each record found
        for row in results:
            # Print the line formatted with the date first so the rows flow in time order
            print(f"Date: {row[0]} | Student: {row[1]} | Assignment: {row[2]} | Mark: {row[3]}% | Grade: {row[4]}")
    # If no records match that subject
    else:
        # Print an error message
        print("No records found for that subject.")
        
    # Close the database connection safely
    db.close()

# MAIN MENU LOOP
while True:
    # Print the five main menu choices
    print("\n1. Print all students")
    print("2. Search student grades")
    print("3. Calculate subject average")
    print("4. Sort grades chronologically")
    print("5. Exit")
    
    # Ask the user to type their choice and remove any extra spaces
    user_input = input("Select 1, 2, 3, 4, or 5: ").strip()
    
    # If the user typed "1", run the print_all_students function
    if user_input == "1":
        print_all_students()
    # If the user typed "2", run the search_student_grades function
    elif user_input == "2":
        search_student_grades()
    # If the user typed "3", run the calculate_subject_average function
    elif user_input == "3":
        calculate_subject_average()
    # If the user typed "4", run the sort_grades_chronologically function
    elif user_input == "4":
        sort_grades_chronologically()
    # If the user typed "5", break out of the while loop to close the program
    elif user_input == "5":
        break
    # If the user typed anything else, show an error message
    else:
        print("Not an option.")