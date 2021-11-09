import sqlite3
import cgi

form = cgi.FieldStorage()
searchterm =  form.getvalue('search_student')



con = sqlite3.connect('Students.db')
cur = con.cursor()  
cur.execute('select result from Grade where Student_Id='+str(searchterm))
r = cur.fetchone()
con.close()
print("<td>" + str(r[0])+ "</td>")

    
