# Date: 2019/6/26

# python 基础
#     1.1 str = 'a,hello'在字符串str中查找hello;
str = 'a,hello'
new_str = str.find("hello")
print(new_str)

#     1.2 str = 'a,b,c,d'用逗号分割str字符串，并保存到列表；
str = 'a,b,c,d'
list_str = str.split(",")
print(list_str)

#     1.3 将“笔试题  123A”中123替换为"进行中"；
str = "笔试题  123A"
new_str = str.replace("123", "进行中")
print(new_str)

# 用任意编程语言循环输出整数0-10.
i = 0
while i <= 10:
    print(i)
    i +=1
# 用任意语言实现逆序输出一个字符串，比如[欢乐逛欢迎您]，输出[您迎欢逛乐欢]。
str = "欢乐逛欢迎您"
new_str = str[::-1]
print(new_str)

#-----------------------6.	从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母----------------

'''

# 循环从键盘中输入5个学生的名字，且存储到列表name_list
name_list = []
for i in range(1, 6):
    name = input("请输入第%d个学生的名字：" %i)
    name_list.append(name)
print(name_list)

# 依次打印每个学生名字中的第2个字母
for i in range(5):
    stu_name = name_list[i]
    print("第%d个学生名字中第2个字母是：%s" %(i+1, stu_name[1]))

'''
#--------------------7.	随机生成五个数字保存在列表中，取反并输出至终端.(取反:求出相反数，随机数范围是0到100)------------
'''
import random

# 循环随机生成五个数字保存在列表中
num = []
for i in range(5):
    num.append(random.uniform(0, 100))
print("列表正向打印：%s" % num)

#列表数字取反(求相反数)并输出至终端
new_num = []
for j in range(5):
    new_num.append(-num[j])
print("列表取反打印：%s" % new_num )
'''

# -----------------------------------8.	将下列两个列表合并，将合并后的列表升序并输出.-----------------------------------
'''
list1 = [1,3,4,5,7]
list2 = [0,66,8,9]

# 将两个列表合并
list1.extend(list2)

# 将合并后的列表升序并输出
list1.sort()
print(list1)
'''

#------------9.	使用字典来存储一个人的信息(姓名、年龄[数字]、学号)，这些信息来自键盘的输入，储存完输出至终端.-----------
'''
name = input("请输入姓名：")
age = input("请输入年龄：")
id = input("请输入学号：")

if not age.isdigit():
    print("年龄非数字类型，请重新输入！")
else:
    stu_dict = {}
    stu_dict["姓名:"] = name
    stu_dict["年龄:"] = int(age)
    stu_dict["学号:"] = id
    print(stu_dict)
'''

#-----------------------10.	有下列字典dict1,查找值为“lebo”对应的key并输出到终端.(结果应该是输出school)----------------
'''
dict1={"school":"lebo", "date":2018, "address":"beijing"}
for key, values in dict1.items():
    if values == "lebo":
        print(key)
'''

#-----------------------11.	使用切片翻转列表num，将翻转完后的列表中所有偶数位置的元素相加求和并输出至终端.--------------
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 切片翻转列表num
new_num = num[::-1]
print(new_num )

# 列表中所有偶数求和
sum = 0
for i in new_num:
    if i % 2 == 0:
        sum += i
print(sum)



