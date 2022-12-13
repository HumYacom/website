from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    data = {"name":"menu","adddoc":"AddDoc"}
    return render_template("index.html",mydata = data)

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/sendData")
def adminup():
    idname = request.args.get("idname")
    level = request.args.get("level")
    department = request.args.get("department")
    sos = request.args.get("sos")
    notify = request.args.get("notify")
    return render_template("youfuck.html",data={"name":idname ,"level":level,"department":department,"sos":sos,"notify":notify})

if __name__ == "__main__":
    app.run(debug=True)