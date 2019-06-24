# Date：2019/6/24
# Name: TONGQIANG
# -*- coding:utf-8 -*-

'''
1.下列将字符串"100"转换为数字100的正确的是( A )

A、int(“100”)  B、int[“100”]  C、toInt(“100”)  D、toUp(”100”)

'''
# a = int["100"]
# print(type(a))

'''
2.下列程序执行结果是(  A  )                                                 
numbers = [1，5，3，9，7]                                                                          
numbers.sort(reverse=True)                                                                               
print(numbers)                                                                                      
A、[9，7，5，3，1]                                                                                                        
B、[1，3，5，7，9]                                                                                      
C、1，3，5，7，9                                                                                        
D、9，7，5，3，1
'''

# numbers = [1, 5, 3, 9, 7]
# numbers.sort(reverse=True)
# print(numbers)

'''
3.如何在列表中添加一个元素
'''

# list1 = ["天下", "月龄", "紫霞", "青霞"]
# list1.append("花和尚")
# print(list1)
#
# list1.extend(["天河", "小溪"])
# print(list1)
#
# list1.insert(0, "水源")
# print(list1)

'''
4.对于列表什么是越界
    索引越界
'''

'''
5.说出变量类型中，哪些是可变数据类型，哪些不可变数据类型
  不可变数据类型：数字、字符串、元组、buer
  可变数据类型：列表、字典
'''

'''
6.从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母
'''
# student_Name = []
# i = 0
# while i < 5:
#     a = input("请输入您的姓名：")
#     student_Name.append(a)
#     i += 1
# print(student_Name)
#
# for stu in student_Name:
#     print("%s同学的名为：%s" % (stu, stu[1]))


# a = "小河流水"
# print(a[3])

'''
7.随机生成五个数字保存在列表中，取反并输出至终端.(取反:求出相反数，随机数范围是0到100)
'''

# import  random
#
# i = 0
# A = []
# B = []
# while i < 5:
#     list_1 = random.randint(0, 100)
#     A.append(list_1)
#     i += 1
# # print(A)
# for a in A:
#     if a >= 0:
#         a = -a
#         B.append(a)
#
# print(B)

'''
8.将下列两个列表合并，将合并后的列表升序并输出.
list1 = [1,3,4,5,7]
list2 = [0,66,8,9]
python对容器内数据的排序有两种，一种是容器自己的sort函数，一种是内建的sorted函数。

sort函数和sorted函数唯一的不同是，sort是在容器内排序，sorted生成一个新的排好序的容器。
'''
# list1 = [1, 3, 4, 5, 7]
# list2 = [0, 66, 8, 9]
# list3 = list1 + list2
# print(list3)
# list_1 = sorted(list3, reverse=True)
# print(list_1)
# # 第二种
# list3.sort(reverse=True)
# print(list3)


'''
9.使用字典来存储一个人的信息(姓名、年龄[数字]、学号)，这些信息来自键盘的输入，
储存完输出至终端.
'''
# dict_1 = {}
# a = input("请输入您的姓名：")
# b = input("请输入您的年龄：")
# if type(b) != int:
#     print("年龄请输入数字！！!")
#     b = int(input("请输入您的年龄："))
# c = input("请输入你的学号：")
# dict_1["name"] = a
# dict_1["age"] = b
# dict_1["number"] = c
#
# print(dict_1)

'''
10.有下列字典dict1,查找值为“lebo”对应的key并输出到终端.(结果应该是输出school)
dict1={“school”:”lebo”,”date”:2018,”address”:”beijing”}
'''

# dict_2 = {'school': 'lebo', 'date': 2018, 'address': 'beijing'}
# for key, values in dict_2.items():
#
#      if values == "lebo":
#          print(key)

'''
11.使用切片翻转列表num，将翻转完后的列表中所有偶数位置的元素相加求和并输出至终端.
num = [0,1,2,3,4,5,6,7,8,9]
'''
# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = num[::-1]
# print(b)
# sum = 0
# for i in b:
#    if i % 2 == 0:
#        sum += i
# print(sum)


'''
用任意编程语言循环输出整数0到10
'''
# a = []
# for i in range(11):
#     a.append(i)
# print(a)

'''
用任意语言实现逆序输出一个字符串，比如[欢乐狂欢迎您]，
输出[您欢迎狂欢乐]
'''
A = "北京欢迎您"
# a = A[::-1]
# print(a)

# a = list(A)
# a.sort(reverse=True)
# for i in a:
#     print(i, end="")

# s = ""
# for i in A:
#     s = i + s
# print(s)

'''
1、str = "a,hello" 在字符串str 中查找hello；
2、str = "a,b,c,d"用逗号分割str字符串，并保存到列表；
3、将"笔试题123A"中123替换为"进行中"
'''
# str = "a,hello"
# print(str.find("hello"))
# print(str[0])
#
# str = "a,b,c,d"
# strlist = str.split(",")
# print(strlist)
#
#
# L = "笔试题123A"
# L1 = L.replace("123", "进行中")
# print(L1)
