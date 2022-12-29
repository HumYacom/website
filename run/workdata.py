from flask import Blueprint,render_template
import pymysql
from host_connect import *

db = pymysql.connect(host=HOST,user=USER,passwd=PASS,database=DATABASE)


workdata = Blueprint('workdata',__name__)

@workdata.route("/")
def workindex():
    cur = db.cursor()
    try:
        sql = "SELECT * FROM cerficate"
        cur.execute(sql)
        rows = cur.fetchall()
    except:         
        print(rows)
    return render_template("work.html", datas = rows)