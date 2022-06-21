from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template


app = Flask(__name__,)
app.debug = True



@app.route('/')
def index():
    return render_template("/index.html")

@app.route("/about)
def about():
    return render_template("about.html")
    
if __name__=='__main__':
    app.run(debug=True)
