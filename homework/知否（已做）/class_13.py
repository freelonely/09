# Date：2019/7/2
# Name: TONGQIANG
# -*- coding:utf-8 -*-

# 类

#
# class Myhero():
#
#     def __init__(self, height=150, weight=150, name="hhhh"):
#         self.height = height
#         self.weight = weight
#         self.name = name
#
#     def move_def(self):
#         print(self.height)
#         print(self.name)
#         print(self.weight)
#
#     def __del__(self):   # 监听对象是否被销毁
#         print("再见")
#
#
# A = Myhero(130, 140, "kaishi")
# A.move_def()

'''
1、创建一个对象后默认调用( A )
A、__init__    B、__str__    C、__add__    D、__and__
'''

'''
2、类是对象的 抽象表达 、对象是类的 具体表达.
'''

'''
3、对象是由属性、方法 两部分构成.
'''
'''
4、创建学生类：
	类名：Student
	属性：name（姓名）、age（年龄）、sex（性别） 
方法：
	def info(self) # 打印学生的姓名、年龄、性别
	def draw(self) #打印”XX会画画呢”
描述：创建学生类，通过学生类创建一个学生对象，分别调用学生的info方法和draw方法.	
'''


class Student(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def info(self):
        print(self.name)
        print(self.age)
        print(self.sex)

    def draw(self):
        print(self.name + ": 会画画呢！")


stu = Student("张珊", 25, "女")
stu.info()
stu.draw()


'''
5、创建动物类：
	类名：animal
	属性(使用魔法方法实现)：name（姓名）、age（年龄）、color（颜色） 
方法：
	def info(self) # 打印姓名、年龄、毛颜色
	def run（self）#打印“XX会跑呢”
描述：创建动物类，通过动物类创建一个动物对象，分别调用动物的info和run方法.
'''
print("="*50)

class Animal(object):

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print(self.name)
        print(self.age)
        print(self.color)

    def run(self):
        print(self.name + ": 会跑呢！")


animal = Animal("小黄狗", 6, "淡黄色")
animal.info()
animal.run()