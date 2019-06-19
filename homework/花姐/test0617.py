# Date 2019/6/17
# Name huajie
# -*- coding:utf-8 -*-
# 4题 start
a = input("please input the first number:")
b = input ("please input the second number:")
c = int(a) + int(b)
print("the result is ",c)
# 4题 end
# 5题 start
print("=========================")
print("=欢迎进入到身份认证系统 \nV1.0")
print("=1. 登录")
print("=2. 退出")
print("=3. 认证")
print("=4. 修改密码")
print("=========================")
# 5题  end
#6题 start
name = input("Please input your name:")
qq = input("Please input your qq number:")
phone = input("Please input your phone number:")
addr = input("Please input your company address:")
print("==================================")
print("姓名： ",name)
print("QQ: ",qq)
print("手机号：",phone)
print("公司地址： ",addr)
print("==================================")
#6题 end
# 7题 start
name = "june"
pwd = "june123"
inputname = input("Please input your name:")
inputpwd = input("Please input your password:")
if (inputname == name) and (inputpwd == pwd):
    print("欢迎进入火星的世界")
else:
    print("密码或者用户名错误")
# 7题 end
