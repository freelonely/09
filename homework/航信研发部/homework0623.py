# 我是blanny
#DATE ：2019-07-08
# my_list = list()
# my_list.append("d323")
# my_list.extend("121213dffdf212")
# print(my_list)

"""
6.	从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母
"""
# stu_name = list()
# for i in range(0,5):
#     name_i = input("请输入第%d个学生名字：\n")
#     stu_name.append(name_i)
#     print(stu_name[i][1])

"""
7.	随机生成五个数字保存在列表中，取反并输出至终端.(取反:求出相反数，随机数范围是0到100)
"""
# import random
# my_list = list()
# for i in range(0,5):
#     my_list.append(random.randint(0,100))
# print(my_list)
# for i in range(0,5):
#     print("-%d" % my_list[i])

"""
8.	将下列两个列表合并，将合并后的列表升序并输出.
list1 = [1,3,4,5,7]
list2 = [0,66,8,9]
"""
# list1 = [1, 3, 4, 5, 7]
# list2 = [0, 66, 8, 9]
# list3 = list1 + list2
# list3.sort()
# print(list3)


"""
10.	使用字典来存储一个人的信息(姓名、年龄[数字]、学号)，这些信息来自键盘的输入，储存完输出至终端.
"""
# my_dict = dict()
# a_name = input("请输入姓名：")
# my_dict["姓名"] = a_name
# a_age = int(input("请输入年龄："))
# my_dict["年龄"] = a_age
# a_num = input("请输入学号：")
# my_dict["学号"] = a_num
# print(my_dict)


"""
11.	有下列字典dict1,查找值为“lebo”对应的key并输出到终端.(结果应该是输出school)
dict1={“school”:”lebo”,”date”:2018,”address”:”beijing”}

"""
# dict1 = {"school" : "lebo", "date" : 2018, "address" : "beijing"}
# for key, value in dict1.items():
#     if value == "lebo":
#         print(key)

"""
12.	使用切片翻转列表num，将翻转完后的列表中所有偶数位置的元素相加求和并输出至终端.
num = [0,1,2,3,4,5,6,7,8,9]
"""
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num = num[::-1]
# print(num)
tmp = num[1::2]
print(sum(tmp))

