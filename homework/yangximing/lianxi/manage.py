# -*- coding: utf-8 -*-
# @Time      :2019/7/16 0016 18:14
# @Author    :lebo_ximing
# @Email     :1228902900@qq.com
# @File      : manage.py.py

from flask import Flask,render_template,request
import pymysql
app = Flask(__name__)
@app.route('/index')
def index_xxx():
    return render_template('html/login.html')
@app.route('/commit')
def commit():
    db = pymysql.connect("localhost","root","123456","test",3306)
    cur = db.cursor()
    username=request.args["username"]
    pwd=request.args["psw"]
    sql="select * from ximing where y_name='%s' and y_id ='%s'" %(username,pwd)
    print(sql)
    cur.execute(sql)
    info=str(cur.fetchone())
    cur.close()
    db.close()
    return  info
app.debug = True
app.run()
