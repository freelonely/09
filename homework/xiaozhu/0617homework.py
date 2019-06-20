#猜拳游戏
import random
player = input("请输入石头、剪刀、布：\n")
computer = random.choice(["剪刀","石头","布"])
print(computer)
if (player == "石头" and computer == "剪刀") or (player == "剪刀" and computer == "布") or (player == "布" and computer == "石头"):
    print("玩家获胜")
elif (player == computer):
    print("平局")
else:
    print("玩家输了")

# 打印图形
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*",end="")
        j += 1
    print()
    i += 1
a = 1
while a <= 4:
    b = 4
    while b >= a:
        print("*",end="")
        b -= 1
    print()
    a +=1