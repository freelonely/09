# Date: 2019/6/18
# Name: connor
# _*_ conding:utf-8 _*_

a = int(input("请输入第一个数字"))
b = int(input("请输入第二个数字"))
c = a + b
print(c)

user = "张三"
pwd = 123456
user1 = input("请输入用户名")
pwd1 = int(input("请输入密码"))
if (user1 == user) and (pwd1 == pwd):
    print("欢迎进入xxx的世界")
else:
    print("密码或者用户名错误")


i=1
while i<=5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i +=1

i=1
while i<5:
    j = 4
    while j > i:
        print("*", end="")
        j -= 1
    print("*")
    i +=1

import random
computer = random.choice(("石头", "剪刀", "布"))
player = input("请输入剪刀石头布")
if ( player == "剪刀" and computer == "布" ) or ( player == "石头" and computer == "剪刀" ) or ( player == "布" and computer == "石头"):
    print("玩家获胜")
else:
    print("电脑获胜")