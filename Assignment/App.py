#docstring -Aarooshi Pandit-Grades tracking database
#import
import sqlite3


#constants and variables
DATABASE = "grades.db"



#functions
def print_all_students():
    db = sqlite3.connect("grades.db")     #  Connect to your database file
    cursor = db.cursor()
    sql = "SELECT * FROM Students;"     #selects all data from student table 
    cursor.execute(sql)            #  Execute the query (this sends the command to the database)
    results = cursor.fetchall()     # Fetch the results from the cursor and print them
    print(results)
    db.close()            # 5. Clean up and close the connection



#main code
print_all_students()
