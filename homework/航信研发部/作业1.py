# 我是：航信研发部
#DATE ：2019-07-05
# 第一次作业补
"""
1、使用while，完成以下图形的输出
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

i = 1
while i <= 6:
    j = 1
    while j <=i:
        print("*",end="")
        j +=1
    print()
    i +=1
i = 1
while i < 5:
    j = 1
    while j <=(5 - i):
        print("*",end="")
        j +=1
    print()
    i +=1


"""
2、break和continue的区别：
break 是跳出所在循环块
continue是跳出所在循环块的本次循环，直接进入下一次循环
"""

"""
3、用循环的方式做出石头剪刀布的游戏并且输入中文
"""
import  random
for i in range(1,4):
    print("第%d局开始：" % i)
    player =input("请输入石头、剪刀、布\n")
    computer = random.choice(['石头','剪刀','布'])

    print("电脑出的是 %s" %computer)
    print("您出的是：%s" % player)

    if ((player == '石头' and computer == '剪刀') or (player == '剪刀' and computer == '布') or (player == '布' and computer == '石头')):
        print("您赢了！耶！！！")
    elif computer == player:
        print("平手")
    else:
        print("您输了，加油，再来一局")
    print("------------------------------")
    i += 1

# 我是blanny
#DATE ：2019-07-08
"""
4、编写程序，完成以下要求：
•	提示用户进行输入数据
•	获取用户的数据（需要获取2个）
•	对获取的两个数字进行求和运行，并输出相应的结果
"""
# a = int(input("请输入数字A："))
# b = int(input("请输入数字B："))
# c = a + b
# print("您输入的值为%d、%d，其和为：%d" % (a, b, c))

"""
5、编写程序，完成以下信息的显示: 
•	==================================
•	=        欢迎进入到身份认证系统V1.0
•	= 1. 登录
•	= 2. 退出
•	= 3. 认证
•	= 4. 修改密码
•	==================================
"""
# print("=" * 50)
# print("=",end = "")
# my_str = "欢迎进入到身份认证系统 V1.0"
# print("%30s" % my_str)
# print("= 1. 登录")
# print("= 2. 退出")
# print("= 3.认证")
# print("= 4. 修改密码")
# print("=" * 50)

"""
6、编写程序，通过input()获取一个人的信息，然后按照下面格式显示
==================================
姓名: xxxxx    
QQ:xxxxxxx
手机号:131xxxxxx
公司地址:北京市xxxx
"""
# my_name = input("请输入您的姓名：\n")
# my_qq = input("输入您的QQ号：\n")
# my_phone = input("输入您的手机号：\n")
# my_url = input("输入您的公司地址：\n")
# print("=" * 50)
# print("姓名：%s" % my_name)
# print("QQ：%s" % my_qq)
# print("手机号：%s" % my_phone)
# print("公司地址：%s" % my_url)
# print("=" * 50)

"""
7、使用if，编写程序，实现以下功能： 
•	从键盘获取用户名、密码
•	如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
"""
# a_name = "abc"
# a_pw = "123456"
# my_name = input("输入您的用户名：\n")
# my_pw = input("输入您的密码：\n")
# if (a_name == my_name and a_pw == my_pw):
#     print("欢迎来的python的世界")
# else:
#     print("密码或者用户名错误")

