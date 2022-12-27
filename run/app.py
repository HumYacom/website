from flask import Flask,render_template,request
import pymysql

db = pymysql.connect(host="localhost",user="root",passwd="",database="table")

app = Flask(__name__)

@app.route("/")
def show():
    with db:
        cur = db.cursor()
        sql = "SELECT * FROM list_products"
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        return "ok"
   # return render_template("index.html",mydata = data)

@app.route("/work") 
def work():
    return render_template("work.html")





if __name__ == "__main__":
    app.run(debug=True)