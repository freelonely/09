#   Date: 2019/7/14 0014
#   Name: life
#  _*_ coding:UTF-8  _*_


#17
num=int(input("请输入成绩的分值："))
if num>=90:
    print("A")
elif num>=60 and num<=89:
    print("B")
elif num<60:
    print("C")


#18、用户名：username = “username” 密码：password = “passwd”
# username = "username"
# password = "passwd"
#
# while True:
#     name = input("请输入用户名：")
#     paw = input("请输入密码：")
#     if name==username:
#        if paw==password:
#            print("登录系统成功")
#            break
#        else:
#            print("密码输入错误！")
#            continue
#     else:
#          print("用户名输入错误！")

"""19. 定义一个学生类，属性有姓名（name）、年龄（age）、性别（sex），
方法有学习、休息，然后创建一个学生对象，调用学习和休息方法。
"""
# class Student(object):
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def xuexi(self):
#         print(("姓名：%s，年龄：%d,性别：%s在学习") % (self.name,self.age,self.sex))
#     def xuxi(self):
#         print(("姓名：%s，年龄：%d,性别：%s在休息") % (self.name,self.age,self.sex))
# stu=Student("Lily",28,"女")
# stu.xuexi()
# stu.xuxi()

#20. 请代码实现：利用下划线将列表的每一个元素拼接成字符串，li = ['alex', 'eric', 'rain'] 。
# li = ['alex', 'eric', 'rain']
# b="_".join(li)
# print(b)

#21
select name from tb_user where fenshu>80 group by name having  kecheng