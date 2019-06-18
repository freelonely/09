# Date：2019/6/18 0018
# Name: 天然卷
# -*- coding:utf-8 -*-


"""
1、说出变量名字可以由那些字符组成
   字母、数字、下划线。

2、写出变量命名时的规则
    由字母、数字、下划线组成（最好有含义），数字不能开头
   
3、写出什么是驼峰法
    大驼峰 MyName 小驼峰 myName
"""


#4、编写程序，完成以下要求：
#提示用户进行输入数据
#获取用户的数据（需要获取2个）
#对获取的两个数字进行求和运行，并输出相应的结果
"""
# print("欢迎来到天才第一步，小葵花其乐无穷了计算器!")
# print("请输入第一个数字")
# a = input()
# b = int(a)
# print("请输入第二个数字")
# c = input()
# d = int(c)
# print("结果为",d + b)
"""

# 5、编写程序，完成以下信息的显示:
# ==================================
# =        欢迎进入到身份认证系统V1.0
# = 1. 登录
# = 2. 退出
# = 3. 认证
# = 4. 修改密码
# ==================================
"""
 print("===================================")
 print("=       欢迎进入身份认证系统,\nV1.0")
 print("=1.\t登录")
 print("=2.\t退出")
 print("=3.\t认证")
 print("=4.\t修改密码")
 print("===================================")
"""

# 6、编写程序，通过input()获取一个人的信息，然后按照下面格式显示
#
# ==================================
# 姓名: xxxxx
# QQ:xxxxxxx
# 手机号:131xxxxxx
# 公司地址:北京市xxxx
# ==================================

"""
print("请输入姓名查询个人资料")
a = input()
if(a):
    print("===================================")
    print("姓名：xxxx")
    print("QQ:xxxxxxx")
    print("手机号：138XXXXXXXXX")
    print("公司地址:北京市XXXXX")
    print("===================================")
"""

# 7、使用if，编写程序，实现以下功能：
# 从键盘获取用户名、密码
# 如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”
# ，否则提示密码或者用户名错误


"""
Name = "t"
passwd = 1

Name1 = input("请输入账号:\n")
passwd1 = int(input("请输入密码\n"))
if(Name1 == Name) and (passwd1 == passwd):
    print("欢迎来到“T”的世界")
else:
    print("用户名密码错误")
"""


# 8、用循环的方式做出石头剪刀布的游戏并且输入中文
"""
import random
print("剪刀石头布1v1决赛")
computer = random.choice(["剪刀","石头","布"])
player = input("请输入：\n")

print("用户：%s 电脑：%s" % (player,computer))
if(player == "剪刀" and computer == "布") or (player == "石头" and computer == "剪刀") or(
    player == "布" and computer == "石头"):
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")
"""



# 1、使用while，完成以下图形的输出
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# i = 1
# while i <= 5:
#     print("*")
#     i += 1
# j = 1
# while j <= 5:
#     print("*",end="")
#     j += 1


i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*",end="")
        j += 1
    print()
    i += 1
i = 4
while i > 0:
    j = 0
    while j < i:
        print("*",end="")
        j += 1
    print()
    i -= 1

"""
break和continue的区别
break：跳出循环
continue：跳出本次循环
"""