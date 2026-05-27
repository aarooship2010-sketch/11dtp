import sqlite3

#  Connect to your database file
db = sqlite3.connect("grades.db")
cursor = db.cursor()
#selects all data from student table 
sql = "SELECT * FROM Students;"

#  Execute the query (this sends the command to the database)
cursor.execute(sql)

# Fetch the results from the cursor and print them
results = cursor.fetchall()
print(results)

# 5. Clean up and close the connection
db.close()