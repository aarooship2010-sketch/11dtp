import sqlite3

db = sqlite3.connect("Grades_tracker.db")
cursor = db.cursor()
sql= "SELECT * from Grades_tracker;"
results = cursor.fetchall()
print(results)

db.close()