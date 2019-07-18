# Date:2019/7/12
# Name:tanqin

from pymysql import * #导入pymysql模块
db =  Connection(host="106.13.46.164",port=3306,database="19",user="19_qi_test",password="123456")#连接数据库
cur = db.cursor()  #获取游标


while True:
    pd = int(input("登录请输入1，注册请输入2，退出请输入3\n"))
    if pd == 1:  #登录
        username = input("姓名：\n")
        password = int(input("学号：\n"))
        sql = "select * from a_students where name='%s' and studentNo='%d'; " % (username,password)
        a = cur.execute(sql)#执行sql语句
        if a == 1:
            print("登录成功")
            break
        elif a == 0:
            print("登录失败")
        cur.close()  # 关闭游标

    if pd == 2: #注册
        username = input("用户名：\n")
        password = int(input("密码：\n"))

        sql = "select * from a_students where name='%s'and studentNo='%d';" % (username, password)#先查询表中是否存在该用户名和学生号
        a = cur.execute(sql)#执行sql语句

        if a == 1:
            print("用户已存在")
        elif a == 0:
            sql = "insert into a_students (name,studentNo) VALUE  ('%s','%d');" % (username,password)#如果存在该数据提示用户已存在，不存在该数据则插入该条数据
            cur.execute(sql)
            db.commit()

            sql = "select * from a_students where name='%s'and studentNo='%d';" % (username, password)#插入数据后再查询，有该数据表示注册成功，没有该数据表示注册失败
            a = cur.execute(sql)#执行sql语句

            if a == 1:
                print("注册成功")
            else:
                print("注册失败")
                db.rollback()#如果失败重新回滚

    elif db == 3:  # 退出
        print("退出")


cur.close()  # 关闭游标
db.close()  # 关闭数据库连接



