#   Date: 2019/7/16 0016
#   Name: life
#  _*_ coding:UTF-8  _*_

from flask import Flask,render_template,request
import pymysql

# #flask本身，创建对象
app=Flask(__name__)
# #路由访问地址
@app.route('/index')
def index_new():
# #返回模版用前端内容
    return render_template('html/login.html')

#需要提交到数据库
@app.route('/commit')
def commit():
    db=pymysql.connect("localhost","root","654321","test",3306)
    cur=db.cursor()
    username=request.args["username"]
    pwd=request.args["pwd"]
    sql="select * from student where name='%s' and pwd='%s'" % (username,pwd)
    print(sql)
    cur.execute(sql)
    info=str(cur.fetchone())
    cur.close()
    db.close()
    return info
app.debug=True
app.run()
