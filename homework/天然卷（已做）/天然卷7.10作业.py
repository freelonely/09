# Date：2019/7/11 0011
# Name: 天然卷
# -*- coding:utf-8 -*-

import pymysql

while True:
    #链接数据库
    sq = pymysql.connect(host="127.0.0.1", port=3306, database="test", user="root", password="root", charset="utf8")

    #获取游标
    cur = sq.cursor()
    ld = int(input("登陆输入1，注册输入2，退出请输入3\n"))
    if ld == 1:
        print("-"*20 + "开始登陆" + "-"*50)
        #登陆
        acc = int(input("学号："))
        pas = input("姓名：")
        sql = "select * from students WHERE id ='%d' and name ='%s'" % (acc, pas)
        aa = cur.execute(sql)
        if aa == 1:
            print("登陆成功")
        elif aa == 0:
            print("失败")
        sq.close()

    elif ld == 2:
        print("-"*50 + "开始注册" + "-"*50)
        #注册
        pswd = int(input("请输入学号："))
        user = input("请输入姓名：")
        #查看信息是否已被注册
        sql = "select * from students WHERE (name = '%s')" % user
        bb = cur.execute(sql)
        if bb == 1:
            print("已存在")
        elif bb == 0:
            sql = "insert into students(id, name) values ('%d', '%s')" % (pswd, user)
            cur.execute(sql)
            #对数据进行操作一定要用commit进行提交
            sq.commit()
            print("注册成功")
    elif ld == 3:
        print("您已退出")
        break
    else:
        print("输入错误")
