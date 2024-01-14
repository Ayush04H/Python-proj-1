from flask import Flask,request,render_template
import sqlite3
from datetime import datetime

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return render_template('search_student.html')
    else:
        conn = sqlite3.connect('students.db')
        c = conn.cursor()

        student_name = request.form.get('studentname')

        c.execute(f"""SELECT * FROM info
                        WHERE name LIKE '%{student_name}%'
                 """)
        results=c.fetchall()
        column_names=['Name','StudentID','Address','Gender','Date of Birth']
        conn.close()

        return render_template('search_results.html',headings=column_names,mylist=results)

@app.route('/add_student',methods=['GET','POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        return 'Placeholder'