# and	x and y	布尔"与"：如果 x 为 False，x and y 返回 False，否则它返回 y 的值。	True and False， 返回 False。
# or	x or y	布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。	False or True， 返回 True。
# not	not x	布尔"非"：如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not True 返回 False, not False 返回 True


# and
# 同真则真 一假则假
# 假设 用户名 mngr 密码 123456  告知用户您输入的用户名和密码正确 登录成功

# 引导用户输入用户名和密码
# user = input("请输入您的用户名:")
# passwd = input("请输入您的密码:")

# 判断
# if user == "mngr" and passwd == "123456":
#     print("您输入的用户名和密码正确 登录成功")


# or
# 一真则真 全假则假
# 您输入的用户名或者密码错误

# if user != "mngr" or passwd != "123456":
#     print("您输入的用户名或者密码错误")


# not(取反)
# 非真则假 非假则真
# 定义一个变量 判断是否是男人
# is_man = True
#
# if not is_man:
#     print("是男人")

is_man = not True

if is_man:
    print("是男人")
	
	
	
# 安检
# 定义一个变量 记录是否是危险品
# 如果为True 就代表没有危险品
# is_flag = not True
# if is_flag:
#     print("没有危险品 可以进入")
# else:
#     print("有危险品 不可以进入火车站")
#
# print("测试")

# 网吧
# 请输入您的年龄 如果年龄大于等于18岁 可以进入网吧吃鸡 如果年龄小于18 回去学习吧
# age = input("请输入您的年龄:")
# new_age = int(age)

# 简写
# age = int(input("请输入您的年龄:"))
# if age >= 18:
#     print("可以进入网吧吃鸡")
# else:
#     print("回去学习吧")

# 保险柜
# 引导用户输入密码 密码正确 打印 密码正确 密码错误 密码错误
# passwd = input("请输入密码:")
#
# if passwd == "12345":
#     print("密码正确")
# else:
#     print("密码错误")

# elif -> else if

# 定义一个变量 记录分数
score = 44
# 如果分数>=90 显示 优  如果分数 >= 80 良  分数 >= 60 中 分数 >= 0 差
# if score >= 90 and score <= 100:
#     print("优")
# elif score >= 80 and score < 90:
#     print("良")
# elif score >= 60 and score < 80:
#     print("中")
# elif score >= 0 and score < 60:
#     print("差")

# 简写
# if score >= 90:
#     print("优")
# elif score >= 80:
#     print("良")
# elif score >= 60:
#     print("中")
# elif score >= 0:
#     print("差")

# 也可以使用else
if score >= 90:
    print("优")
elif score >= 80:
    print("良")
elif score >= 60:
    print("中")
else:
    print("差")

# if语句多种组合
# if语句
# if-else
# if-elif-elif
# if-elif-elif-xx-else


# 进入火车站
# 火车票 刀具
"""
伪代码
01- 进入火车站
    - 判断是否有火车票
        - 如果有 -> 可以进入火车站
            - 判断刀具的长度
                - 如果刀具的长度 < 10cm -> 可以进入火车站
                - 如果刀具的长度 >= 10cm -> 不可以进入火车站
        - 如果没有 -> 请买票后 再进入火车站
"""

# 定义一个变量判断是否有火车票(只有等于1的时候代表有火车票)
chePiao = 1
# 刀具的长度
daoLenght = 7
# 判断火车票
if chePiao == 1:
    # 有车票
    print("可以进入火车站")
    # 判断刀具的长度
    if daoLenght < 10:
        print("拿着您的小刀进入吧")
    else:
        print("不要拿着您的宝剑指着我")
    print("测试")
else:
    # 没有火车票
    print("请买票后 再进入火车站")


# 情节描述：上公交车，并且可以有座位坐下
#
# 要求：输入公交卡当前的余额，只要超过2元，就可以上公交车；如果车上有空座位，就可以坐下。


# 定义一个变量 记录余额
money = eval(input("请输入公交卡的余额:"))
# 定义一个变量 判断是否有空座
flag = not True

# 判断余额
if money >= 2:
    print("可以上车")
    # 判断是否有座位
    if flag:
        print("有座位可以坐下")
    else:
        print("没有座位")
else:
    print("卡中余额不足")
	
	
	
# 随机数模块
import random
# 引导用户输入拳法(剪刀 石头 布)
# 玩家 或者 用户
player = int(input("请输入: 剪刀(0) 石头(1) 布(2):"))

# 电脑(随机出拳)
# randint(0, 2) == [0, 2](闭区间)
computer = random.randint(0, 2)

# 记住 用户 是第一视角
# 赢了
# 用户->剪刀 电脑-> 布
# 用户->石头 电脑-> 剪刀
# 用户->布   电脑-> 石头

# 平局
# 用户的拳法==电脑的拳法

# 输了
# 除了赢得和平的 就是输的
print("玩家:%d--电脑:%d" % (player, computer))
# 赢了
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("玩家胜利!!!")
# 平局
elif (player == computer):
    print("平局")
# 输了
else:
    print("玩家失败!!!")