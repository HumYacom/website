from flask import Blueprint,render_template,request
import pymysql
from host_connect import *

db = pymysql.connect(host=HOST,user=USER,passwd=PASS,database=DATABASE)


admindata = Blueprint('admindata',__name__)

@admindata.route("/")
def adminindex():
    cur = db.cursor()
    try:
        sql = "SELECT * FROM cerficate"
        cur.execute(sql)
        rows = cur.fetchall()
    except:         
        print(rows)
    return render_template("index.html", datas = rows)

@admindata.route("/adminedit",methods=['POST'])
def adminedit():
    
    
        return "5"