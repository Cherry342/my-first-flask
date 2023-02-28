from flask import Flask, render_template, request
app= Flask(__name__)

my_todos=[
    'Game',
    'Review'
]
@app.route("/")

def index():
    return render_template(
        "todo.html.jinja", 
        todos= my_todos 
     my_variable="reviewing"
     my_list=["review", "kahoot"]
     )
@app.route("/add", methods=['POST'])
def add(new_todo):
    new_todo=request.form['new_todo']
    return new_todo
   

    

             
             
