from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def index():
    return render_template(
        "home.html.jinja", 
        my_variable="ancientheroes",
        my_list=["purevanilla", "hollyberry", "darkcacao"])
    #return """
#"<p> Happy, World! </p>"
#<h1>This is a heading</h1>
#"""
@app.route("/ping")
def ping():
    return "<p>pong</p>"

@app.route("/hello/<name>")
def hello(name):
    return f"<p>Hello, {name}!</p>"
