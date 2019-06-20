# -*- coding: utf-8 -*-

import mysql.connector

from exceptions.exceptions import MyError


class mysqlTool(object):
    def __init__(self,**kwargs):
        if kwargs.get('user')==None or kwargs.get('password')==None or kwargs.get('host')==None:
            raise MyError('错误的参数',kwargs)
        try:
            self.cnx = mysql.connector.connect(**kwargs)
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)
            self.cnx.close()


    def doselect(self,sql,param=None):
        if isinstance(param,tuple):
            self.cursor.execute(sql,param)
        elif param==None:
            self.cursor.execute(sql)
        else:
            raise MyError('参数错误',param)
        list =[]
        for i in self.cursor:
            list.append(i)
        return  list

    def doupdate(self,sql,param):
        if isinstance(param,tuple):
            self.cursor.execute(sql,param)
        elif param==None:
            self.cursor.execute(sql)
        else:
            raise MyError('参数错误',param)
        self.cnx.commit()

    def doinsert(self,sql,param):
        return self.doupdate(sql,param)



# arg1 = {'user':'dev','password':'dev','host':'l-test18.dev.cn2.corp.agrant.cn'}
#
# sql1 ="SELECT * from finance_app.user WHERE id='d4dc89b856034cb7b70bd7b750fef512'"
# sql2 ="select * from finance_app.user where mobile =%s"
# tup1=('15652798209',)
#
#
# sql3="UPDATE finance_app.`user` SET `name`=%s WHERE id='d4dc89b856034cb7b70bd7b750fef512'"
# tup2=('范彦彦',)
#
# re1 =mysqlTool(**arg1).doupdate(sql3,tup2)
# print(re1)