import requests
from flask import *
import sqlite3
from flask import render_template
app = Flask(__name__)  # creating the Flask class object

def establish_connection():
    db_connection = sqlite3.connect('todoList.db')
    db_connection.row_factory = sqlite3.Row
    return db_connection
def addrow(title,desc):
    db_connection = establish_connection()
    cur=db_connection.cursor()
    cur.execute('INSERT INTO todo(title, todoDesc) VALUES (?, ?)', (title, desc))
    db_connection.commit()
    cur.close()
    db_connection.close()
def updaterow(title,desc,sno):
    db_connection = establish_connection()
    cur=db_connection.cursor()
    cur.execute('UPDATE todo SET title =? ,todoDesc =? WHERE sno=?',(title,desc,sno))
    db_connection.commit()
    cur.close()
    db_connection.close()
@app.route('/',methods=['GET','POST','PUT','DELETE'])  
def home():
    if request.method=="POST":
        title=request.form['title'] 
        desc=request.form['desc']
        addrow(title,desc)
    db_connection = establish_connection()
    all_todos = db_connection.execute('SELECT * FROM todo').fetchall()
    db_connection.close()
    return render_template("index.html",alltodos=all_todos);

@app.route('/update/<int:sno>',methods=['GET','POST','PUT','DELETE']) 
def update(sno):
    if request.method=="POST":
        title=request.form['title'] 
        desc=request.form['desc']
        updaterow(title,desc,sno)
        return redirect('/') 

    db_connection = establish_connection()
    todos = db_connection.execute('SELECT * FROM todo where sno='+str(sno)).fetchall()
    db_connection.close()
    return render_template("update.html",todos=todos);

@app.route('/delete/<int:sno>',methods=['GET','POST','PUT','DELETE']) 
def delete(sno):
    db_connection = establish_connection()
    cur=db_connection.cursor()
    cur.execute('DELETE FROM todo WHERE sno ='+str(sno))
    db_connection.commit()
    cur.close()
    db_connection.close() 
    return redirect('/')
@app.route('/mytodos')  
def mytodo():
    db_connection = establish_connection()
    all_todos = db_connection.execute('SELECT * FROM todo').fetchall()
    db_connection.close()
    return render_template("mytodo.html",alltodos=all_todos);
@app.route('/about',methods=['GET','POST','PUT','DELETE']) 
def about():
    return render_template("about.html")
if __name__ == '__main__':
    app.run(host=None,port=None,debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
