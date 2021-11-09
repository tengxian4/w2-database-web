import sqlite3

con = sqlite3.connect('Students.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE Student
               (Id integer primary key, Name varchar,Password varchar)''')


cur.execute('''CREATE TABLE Topic
				(Id integer primary key, Name varchar)''')
				
cur.execute('''CREATE TABLE Grade
				(Student_Id integer,Topic_Id integer, Result integer,PRIMARY KEY(Student_Id,Topic_Id), FOREIGN KEY(Student_Id) REFERENCES Student(Id), FOREIGN KEY(Topic_Id) REFERENCES Topic(Id))''')
				
con.commit()
con.close()