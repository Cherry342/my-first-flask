import os
from flask import (Flask, render_template, request,)
app= Flask(__name__)

import pymysql
import pymysql.cursors
connection=pymysql.connect(
    host= "10.100.33.60",
    user= "aokagejasmin",
    password= "220221337",
    database= "aokagejasmin_todo",
    cursorclass= pymysql.cursors.DictCursor,
    autocommit=True 
)
my_todos=[ 
    'Game',
    'Review'
]

@app.route("/")
def index():
    cursor=connection.cursor()
    cursor.execute("SELECT *  FROM 'Todos'")
    result= cursor.fetchall(),
    return render_template(
    "todo.html.jinja", 
    todos= result)



@app.route("/add", methods=['POST', 'GET'])
def add():


    new_todo=request.form['new_todo']
   
    my_todos.append(new_todo)
    
    
    #ADD TO LIST
    #REDIRECT BACK TO INDEX
    return new_todo
    

@app.route("/complete", methods=["POST"])
def complete():
    
    todo_id=request.form('todo_id')

    cursor= connection.cursor()
    cursor.excecute(f"UPDATE 'my_todos' SET 'complete' = 1 WHERE 'id'= {todo_id}")
   
    

    

             
             
