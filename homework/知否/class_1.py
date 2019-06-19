# Date：2019/6/18
# Name: TONGQIANG
# -*- coding:utf-8 -*-


'''
一、变量名可以由哪些字符组成,写出变量命名时的规则，写出什么是驼峰法。
1、变量名可以包括字母、数字、下划线，但是数字不能做为开头。例如：name1是合法变量名，而1name就不可以。
2、系统关键字不能做变量名使用
3、除了下划线之个，其它符号不能做为变量名使用
4、Python的变量名是除分大小写的，例如：name和Name就是两个变量名，而非相同变量
    PS:
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）

骆驼式命名法就是当变量名或函数名是由一个或多个单词连结在一起，而构成的唯一识别字时，第一个单词以小写
字母开始;从第二个单词开始以后的每个单词的首字母都采用大写字母，例如:myFirstName、myLastName，这样的
变量名看上去就像骆驼峰一样此起彼伏，故得名。

骆驼式命名法(Camel-Case)一词来自 Perl 语言中普遍使用的大小写混合格式，而 Larry Wall 等人所著的畅销
书《Programming Perl》(O'Reilly 出版)的封面图片正是一匹骆驼。

骆驼式命名法的命名规则可视为一种惯例，并无绝对与强制，为的是增加识别和可读性。

折叠小驼峰法
变量一般用小驼峰法标识。驼峰法的意思是:除第一个单词之外，其他单词首字母大写。譬如

int myStudentCount;

变量myStudentCount第一个单词是全部小写，后面的单词首字母大写。

常用于函数名。

折叠大驼峰法
相比小驼峰法，大驼峰法(即帕斯卡命名法)把第一个单词的首字母也大写了。常用于类名，属性，命名空间等。譬如

public class DataBaseUser;
'''
'''
4、编写程序，完成以下要求： 提示用户进行输入数据；获取用户的数据（需要获取2个）；
对获取的两个数字进行求和运行，并输出相应的结果
'''

# a = int(input("您好！请您输入第一个数字:"))
# b = int(input("您好！请您输入第二个数字:"))
# c = a + b
# print(c)
print("="*50,end="")
print("下一题",end="")
print("="*50)
'''
5、编写程序，完成以下信息的显示:
欢迎进入到身份认证系统V1.0
= 1. 登录
= 2. 退出
= 3. 认证
= 4. 修改密码
'''
# print("="*50)
# print("欢迎进入到身份认证系统V1.0")
# print("1.登录\n2.退出\n3.认证\n4.修改密码")
# print("="*50,end="\n")
'''
6、编写程序，通过input()获取一个人的信息，然后按照下面格式显示:
姓名: xxxxx    
QQ:xxxxxxx
手机号:131xxxxxx
公司地址:北京市xxxx
'''
# print("="*50)
# Name = input("请输入您的姓名：")
# Name_qq = input("请输入您的qq号码：")
# Name_phone = input("请输入您的手机号码：")
# Name_compary = input("请输入您的公司地址：")
# print("姓名：%s"%Name)
# print("QQ号码：%s"%Name_qq)
# print("手机号码：%s"%Name_phone)
# print("公司地址：%s"%Name_compary)
# print("="*50,end="\n")
'''
7、使用if，编写程序，实现以下功能： 
从键盘获取用户名、密码
如果用户名和密码都正确（预先设定一个用户名和密码），那么就显示“欢迎进入xxx的世界”，
否则提示密码或者用户名错误

'''
# print("="*50)
# Name_YY = input("请输入您的用户名：")
# Name_password = input("请输入您的密码：")
# if Name_YY == "小可爱" and  Name_password == "123456":
#     print("欢迎进入新的虚拟世界！！！")
# else:
#     print("请输入正确的用户名和密码！")
print("="*50)

'''
8、用循环的方式做出石头剪刀布的游戏并且输入中文
random.
'''
# import random
# player = input("请输入您要出的拳头 石头/剪刀/布：")
# choice = ["石头","剪刀","布"]
# computer = random.sample(choice,1)
# computer_1 = computer[0]
# print("玩家选择的拳头是：%s - 电脑出的拳是：%s"%(player,computer_1))
# if (player == "石头" and computer_1 == "剪刀") or (player == "剪刀" and computer_1 == "布") or (player == "布" and  computer_1 == "石头"):
#    print("你这电脑弱爆了！！！")
# elif player == computer_1:
#     print("果然有缘，心有灵犀，加个微信吧！！！")
# else:
#     print("不服气，再来，不死不休！！！")

print("="*50)

'''
1、使用while，完成以下图形的输出
'''
# # 行
# i = 1
# while i < 10 :
#     print("$")
#     i += 1
#
# # 列
# j = 1
# while j < 10 :
#     print("#",end="")
#     j += 1

i = 0
while i <10:
    j = i
    while j > 0 :
        print("*",end="")
        j -= 1
    print("*")
    i += 1

i = 0
while i < 10:
    j = i+1
    while j < 9:
        print("*",end="")
        j += 1
    print("*")
    i += 1

# # 打印三角形
# i = 1
# while i < 10:
#     j = i+1
#     while j < 10:
#         print("*",end="")
#         j += 1
#     print("*")
#     i +=1
#
# for i in range(10):
#     for j in range(0,i):
#         print("*",end="")
#     print()
# i = 10
# while i > 1:
#     j = i-1
#     while j > 1:
#         print("*",end="")
#         j -= 1
#     print("*")
#     i -=1

'''
2、break和continue的区别：
break
1.break 语句可用于跳出循环。
2.break所在的循环体已经结束。
continue
1.continue 语句中断循环中的迭代，如果出现了指定的条件，然后继续循环中的下一个迭代。
2.continue所在的循环体并没有结束。
 
'''
#1.break意思为结束循环,例：
i = 0
while i < 10:
    i += 1
    if i == 5:  # 当i=5时，结束整个循环
        break
    print("i=%d" % i)

#2.continue意思为结束当前循环进入下一个循环,例：
i = 0
while i < 10:
    i += 1
    if i == 5:  # 当i=5时，结束当前循环进入下一个循环
        continue
    print("i=%d" % i)