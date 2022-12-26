from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    data = {"name":"menu","adddoc":"AddDoc"}
    return render_template("index.html",mydata = data)

@app.route("/work") 
def work():
    return render_template("work.html")



if __name__ == "__main__":
    app.run(debug=True)