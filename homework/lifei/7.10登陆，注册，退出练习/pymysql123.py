#   Date: 2019/7/9 0009
#   Name: life
#  _*_ coding:UTF-8  _*_

from pymysql import *

conn = Connection("127.0.0.1","root","654321","test",3306)
#链接数据库
cur = conn.cursor()
#创建游标


while True:
    num = int(input("输入1登陆，输入2注册，输入3退出\n"))
    #判断输入是要干嘛（注意这里必须强转int,不然接受str又拿int判断）
    if num == 1:
        #登陆
        username = input("请输入用户名：\n")
        #接收用户输入用户名
        passwor = int(input("请输入登陆密码：\n"))
        #接收用户输入密码（这里强转和数据库number做判断）
        sql = "select * from student where name='%s' and pwd='%d'; " % (username,passwor)
        a=cur.execute(sql)
        if a == 1:
            print("登陆成功！")
            break
        else:
            print("用户名或密码错误！")
    elif num == 2:
        #注册
        username = input("请输入用户名：\n")
        # 接收用户输入用户名
        #先判断注册用户是否存在
        sql = "select * from student where name='%s';" % (username)
        a = cur.execute(sql)
        #a=1表示数据库查出来已经存在用户名
        if a == 1:
            print("用户已存在")
        elif a == 0:
            #a=0表示数据库未查出来，可以进行注册操作
            info = "insert into student (name)  VALUE  ('%s');" % (username)
            cur.execute(info)
            conn.commit()
            #再在数据库查询是否存在这个用户名
            cha = "select * from student where name='%s';" % (username)
            d = cur.execute(cha)
            #查询等于1说明添加成功
            if d ==1 :
                print("注册成功")
            else:
                print("注册失败")
                conn.rollback()
    elif num == 3:
        #退出
        print("退出成功")
        break
#关闭游标
cur.close()
#关闭数据库连接
conn.close()