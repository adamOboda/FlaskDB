import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE students (name TEXT, surnm TEXT)')
print ("Table created successfully");
conn.close()

@app.route('/enternew')
def new_student():
   return render_template('index.html')


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         surnm = request.form['surnm']
         
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,surnm) VALUES (?,?)",(nm,surnm) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

if __name__ == '__main__':
   app.run(debug = True)
