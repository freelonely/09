# # Date: 2019/7/14
#
# 三、编程题：(第17、18，19# 题10分，第20、21# 题12分，共55分)
# 17.# 利用条件运算符的嵌套来完成此题：请输入成绩的分值，如果学习成绩 >= 90 分用A表示，60 - 89分之间用B表示，60分以下用C表示，将对应的结果输出。

# sort = int(input("请输入成绩："))
# if sort >= 90:
#     print("A")
# elif sort >= 60 and sort < 90:
#     print("B")
# else:
#     print("C")


# 18.从键盘输入一个用户名和密码，判断是否正确，如果正确则显示‘登录系统成功’，否则显示‘用户名或密码错误’，密码正确即退出，密码错误重新输入。
# 用户名：username = “username”   密码：password = “passwd”

# username = "username"
# password = "passwd"
#
# while True:
#     name = input("请输入用户名：")
#     pwd = input("请输入密码：")
#     if name == username and pwd == password:
#        print("登录系统成功")
#        break
#     else:
#       print("用户名或密码错误")


# 19.# 定义一个学生类，属性有姓名（name）、年龄（age）、性别（sex），方法有学习、休息，然后创建一个学生对象，调用学习和休息方法。
# class Student(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def Study(self):
#         print("%s,%d岁,%s, 要好好学习，天天向上哦！"%(self.name,self.age,self.sex))
#
#     def Rest(self):
#         print("%s,%d岁,%s, 学习的过程中，也要学会休息哦！"%(self.name,self.age,self.sex))
#
# stu = Student("小明", 12, "男")
# stu.Study()
# stu.Rest()

# 20.请代码实现：利用下划线将列表的每一个元素拼接成字符串，li = ['alex', 'eric', 'rain'] 。
li = ['alex', 'eric', 'rain']
str_li= "_".join(li)
print(str_li)

# 21.求每门成绩都大于80的学生名字。（注意：不能有重复的名字出现，需要在一条语句中完成）
"""
tb_user
name   kecheng     fenshu
张三     语文       81
张三    数学       75
李四    语文       76
李四    数学       90
王五    语文       81
王五    数学      100
王五    英语      90
"""
# select * from tb_user where group by kecheng having fenshu > 80;


