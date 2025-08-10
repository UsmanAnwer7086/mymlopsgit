from flask import Flask, render_template,request
# Some change of mind is always applicable
"""
It creates an instance of Flask class, 
which will be your WSGL (Web Server Gateway interface) application
"""


app=Flask(__name__) #To execute main function


@app.route("/") # creating views with static response. 
def welcome():
    return "<h1>Hello from Flask. My First Day with Flask!</h1>"

@app.route("/index")  # to render HTML File
def index():
    return render_template("index.html")

@app.route("/form", methods=["GET","POST"])
def form(): # Flask view to render data from html template and render post data
    if request.method=="POST":
        name=request.form["name"]
        passw=request.form["password"]
        return f"Hello {name}!. Your password is {passw}"
    return render_template("form.html")
"""
Jinja 2 template engine is used to share data dynamically between 
flask view and template. 
Multiple constructs of Jinja 2 template engine in html pages. 
a) {{}} expressions to print output in html
b) {%...%} conditions - for loop
c) {#...#} this is for comment
 """
# Building URLS dynamically
"""
Views takes data from url and send results to a template. 
"""
@app.route("/success/<int:score>") # To expect a parameters from url
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template("result.html",results=res)

@app.route("/successres/<int:score>") # To expect multiple values from views to html page
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={"score":score,"res":res} # mutiple data is to be shared via key-value pairs

    return render_template("resultsres.html",results=exp)

if __name__=="__main__":
    app.run(debug=True)