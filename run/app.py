from flask import Flask,render_template,request
from admindata import *


app = Flask(__name__)
app.register_blueprint(admindata)

@app.route("/")
def index():
    return

@app.route("/work") 
def work():
    return render_template("work.html")


if __name__ == "__main__":
    app.run(debug=True)