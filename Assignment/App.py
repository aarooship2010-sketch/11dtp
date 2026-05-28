# docstring - Aarooshi Pandit - Grades tracking database
# import
import sqlite3

# constants and variables
DATABASE = "grades.db"

# functions
def print_all_students():
    '''print all students nicely'''
    db = sqlite3.connect(DATABASE)     # Connected using your constant variable
    cursor = db.cursor()
    
    sql = "SELECT * FROM Students;"    # selects all data from student table 
    cursor.execute(sql)                # Execute the query
    results = cursor.fetchall()        # Fetch the results from the cursor
    
    print(f"\n{'ID':<10}{'Name':<20}{'Gender':<12}{'Ethnicity':<15}")
    print("-" * 57)
    
    # loop through all the results
    for student in results:
        # student[0] = ID, student[1] = Name, student[2] = Gender, student[3] = Ethnicity
        print(f"{student[0]:<10}{student[1]:<20}{student[2]:<12}{student[3]:<15}")
    
    # loop finished here
    db.close()                         # Clean up and close the connection

# main code
while True:
    user_input = input("\nWhat would you like to do?\n1. Print all students\n2. Exit\nSelect an option (1-2): ").strip()
    
    if user_input == "1":
        print_all_students()
    elif user_input == "2":
        print("\nThank you for using the system. Goodbye!")
        break
    else:
        print(' That was not an option. Please try again.\n')