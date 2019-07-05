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


