# Date: 2019/6/24

"""
•	从键盘获取用户名、密码
•	如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误

"""

userName = "aaa"
passWord = 123
Name = input("请输入用户名：")
Pwd = int(input("请输入密码："))

if Name == userName and Pwd == passWord:
    print("欢迎进入Python的世界")
else:
    print("用户名或密码错误")