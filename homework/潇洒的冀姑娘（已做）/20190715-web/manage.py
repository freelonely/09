# Date: 2019/7/20

# render_template模块，返回的是前端的内容
# render_template,request 这两都是必须要用到的，所以要导入
from flask import Flask,render_template,request
import pymysql

# 必须要写，app相当于一个对象，也相当于一个服务器的儿子，以后所有都用到
app = Flask(__name__)

# route相当于一个路由，可以连接多台电脑，在此表示：路由连接的index(可称可随意起)
@app.route('/index')
def index_xx():
    # 导入前端的代码，先必须创建一个文件夹template，将前端的代码放到此文件夹中
    # 可以直接返回数据，返回home.html文件里的内容
    return render_template('login.html')
# 提交,只要登录，就将数据提交到数据库
@app.route('/commit')
def commit():
    # 写具体的sql代码
    conn = pymysql.connect("127.0.0.1", "root", "123456", "school", 3306)
    cur = conn.cursor()
    # name获取的是前端的代码，要获取前端的username
    name1 = request.args['username']
    pwd1 = int(request.args['password'])
    sql = "select * from stu WHERE stu_id = '%d' and stu_name = '%s' " % (pwd1, name1)
    aa = cur.execute(sql)
    # cur.fetchone()返回的是元组，因需要返回的是字符串，所以转换一下
    select01 = str(cur.fetchone())
    cur.close()
    # 返回查询到的数据到前端页面中
    return select01

# 让服务器运行起来
# 打印每一行出错的内容，debug高度状态
app.debug = True
app.run()
"""
结果：
 * Serving Flask app "manage" (lazy loading)                            服务器Flask，名称为manage要运行了
 * Environment: production                                              环境：生产环境
   WARNING: This is a development server. Do not use it in a production deployment. 警告：这是一个开发的环境，不要使用生产的服务器
   Use a production WSGI server instead.                                使用的WSGI协议
 * Debug mode: on                                                       on表示debug已开
 * Restarting with stat         服务开始                             
 * Debugger is active!          debug开始
 * Debugger PIN: 165-088-729    批号  
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)             服务开始跑，将地址复制到网页中，可打开
"""
# 打开网页地址后，NO found 。 将路由“/index"放在地址后，则可显示出错误来