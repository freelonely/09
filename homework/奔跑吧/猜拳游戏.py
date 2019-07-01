import random                       # 调用随机数模块
pc = random.randint(1,3)            # 产生1-3的随机数
print('==================\n来玩个猜拳游戏吧！\n==================')

a = '石头'
b = '剪刀'
c = '布'

user = input('请输入（石头，剪刀，布）：')

if user == '石头':
    print("你出了石头")
elif user == '剪刀':
    print("你出了剪刀")
else:
    print("你出了布")


if pc == 1:
    print('电脑出了石头')
elif pc == 2 :
    print('电脑出了剪刀')
else:
    print('电脑出了布')


if user == '石头' and pc == 2 or user =='剪刀' and pc == 3 or pc == 3 or user == '布' and pc == 1:
    print("你赢了")
elif user == '石头' and pc ==3 or user == '剪刀' and pc == 1 or user == '布' and pc == 2:
    print('你输了')
else:
    print('平局')