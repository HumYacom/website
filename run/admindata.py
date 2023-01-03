from flask import Blueprint,render_template,request,url_for,redirect
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
    if request.method == 'POST':
        name_products = request.form['name_products']
        size = request.form['size']
        cur = db.cursor()
        try:
            sql = "UPDATE cerficate SET  name_products= %s, size = %s"
            cur.execute(sql,(name_products,size))
            
        except:
            db.commit()
        
        return redirect(url_for('admindata.adminindex'))