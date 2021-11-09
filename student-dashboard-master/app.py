"""
Author: Alexandre Nesovic
"""
from flask import Flask, render_template, request
import sqlite3
import pandas as pd
import os
import time
import traceback


app = Flask(__name__)

sql_output = []
SQL_COMMAND = ""
DB_USER_INPUT = ""
INIT_DB_USER_INPUT = True
currentWD = os.path.dirname(__file__)  # WD = working directory

@app.route('/')
@app.route('/grades-sem-1', methods=['GET'])
def readData():
    Id = request.form['Student_Id']
    cursor = mysql.connection.cursor(Students.db)
    sql = f"SELECT result from Student WHERE Id = '{Id}'"
    cursor.execute(sql)
    account = cursor.fetchone()
    return render_template('grades-sem-1.html',result=result)
    
    
if __name__ == '__main__':
    app.run(debug=True)