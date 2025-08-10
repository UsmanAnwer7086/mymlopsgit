from flask import Flask, render_template

"""
It creates an instance of Flask class, 
which will be your WSGL (Web Server Gateway interface) application
"""


app=Flask(__name__) #To execute main function


@app.route("/")
def welcome():
    return "<h1>Hello from Flask. My First Day with Flask!</h1>"

@app.route("/index")
def index():
    return "<h1>Welcome to Index Page</h1>"

if __name__=="__main__":
    app.run(debug=True)