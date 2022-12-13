from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    data = {"name":"menu","adddoc":"AddDoc"}
    return render_template("index.html",mydata = data)

@app.route("/work") 
def work():
    return render_template("work.html")

@app.route("/return")
def adminup():
    idname = request.args.get("idname")
    sale = request.args.get("sale")
    mail = request.args.get("mail")
    price = request.args.get("price")
    tax = request.args.get("tax")
    Payment = request.args.get("Payment")
    tel = request.args.get("tel")
    addr = request.args.get("addr")
    return render_template("su.html",data={"name":idname ,"sale":sale,"mail":mail,"price":price,"tax":tax,"Payment":Payment,"tel":tel,"addr":addr})

if __name__ == "__main__":
    app.run(debug=True)