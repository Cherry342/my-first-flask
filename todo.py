import os
from flask import Flask, render_template, request
app= Flask(__name__)

my_todos=[ 
    'Game',
    'Review'

]
@app.route("/")
def index(my_todos):
    return render_template(
        "todo.html.jinja", 
        todos= my_todos)



@app.route("/add", methods=['POST', 'GET'])
def add():


    new_todo=request.form['new_todo']
   
    my_todos.append(new_todo)
    #ADD TO LIST
    #REDIRECT BACK TO INDEX
    return new_todo


    

             
             
