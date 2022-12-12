from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    data = {"name":"menu","adddoc":"AddDoc"}
    return render_template("index.html",mydata = data)

@app.route("/admin")
def admin():
    username = "admin"
    return render_template("admin.html",username = username)

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/sendDoc")
def signupfrom():
    idn = request.args.get("Name")
    des = request.args.get("Description")
    return render_template("sendDoc.html",data={"Name":idn,"Description":des})

if __name__ == "__main__":
    app.run(debug=True)