# 17.
# 利用条件运算符的嵌套来完成此题：请输入成绩的分值，如果学习成绩 >= 90
# 分用A表示，60 - 89
# 分之间用B表示，60
# 分以下用C表示，将对应的结果输出。

score = int(input("分数:"))
if score >=90:
    print("B")
elif score >=60 and <=89:
    print("B")
else:
    print("C")


# 18.
# 从键盘输入一个用户名和密码，判断是否正确，如果正确则显示‘登录系统成功’，否则显示‘用户名或密码错误’，密码正确即退出，密码错误重新输入。
# 用户名：username = “username”   密码：password = “passwd”

username = input("用户名:")
password = input("密码:")
if username == "username" and password == "passwd":
    print("登录系统成功")
else:
    print("用户名或密码错误")

# 19.
# 定义一个学生类，属性有姓名（name）、年龄（age）、性别（sex），方法有学习、休息，然后创建一个学生对象，调用学习和休息方法。

class Student(object):
    def __init__(self, name, age, sex):
        name = name
        age = age
        sex = sex
    def study(self):
        print("学习")
    def rest(self):
        print("休息")
stu1 = Student("xiaozhu", 10, "female")
stu1.study()
stu1.rest()

# 20.
# 请代码实现：利用下划线将列表的每一个元素拼接成字符串，li = ['alex', 'eric', 'rain'] 。

li = ['alex', 'eric', 'rain']
s = '_'.join(li)
print(s)

#
# 21.
# 求每门成绩都大于80的学生名字。
# （注意：不能有重复的名字出现，需要在一条语句中完成）
select name from score group by name having min(fenshu)>80
