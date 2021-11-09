import sqlite3

con = sqlite3.connect('Students.db')
cur = con.cursor()
cur.execute("INSERT INTO Student VALUES (1, 'Abu','123')")

cur.execute("INSERT INTO Topic VALUES(1,'Abstract')")
cur.execute("INSERT INTO Grade VALUES(1,1,60)")


# Save (commit) the changes
con.commit()
con.close()