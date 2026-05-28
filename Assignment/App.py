#docstring -Aarooshi Pandit-Grades tracking database
#import
import sqlite3


#constants and variables
DATABASE = "grades.db"



#functions
def print_all_students():
    '''print all students nicely'''
    db = sqlite3.connect("grades.db")     #  Connect to your database file
    cursor = db.cursor()
    sql = "SELECT * FROM Students;"     #selects all data from student table 
    cursor.execute(sql)            #  Execute the query (this sends the command to the database)
    results = cursor.fetchall()     # Fetch the results from the cursor and print them
    #loop through all the results
    for students in results:
        print(f"student_id       Name   Gender Ethnicity                       speed              ")
            print(f"{students[1]:<20} {students[2]:<20} {students[3]:<10}")
    #loop finished here
    print(results)
    db.close()            # 5. Clean up and close the connection



#main code
while True:
     user_input = input("What would you like to do.\n1. Print all students\n2.Exit")
    if user_input == "1":
        print_all_students()
    elif user_input == "2":
        break
    else:
        print('That was not an option\n')
