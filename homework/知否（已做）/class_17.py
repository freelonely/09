# Date：2019/7/6
# Name: TONGQIANG
# -*- coding:utf-8 -*-


'''
1、下列程序结果是______.初始化- 类A - 销毁
'''
# class A:
#
#     def __init__(self):
#         print("初始化")
#
#     def __del__(self):
#         print("销毁")
#
#     def __str__(self):
#         return "类A"
#
#
# a = A()
# print(a)


'''
2. 下列程序执行结果______.动物在叫 - 汪汪汪
'''


# class Animal(object):
#
#     def shut(self):
#         print("动物在叫")
#
#
# class Dog(Animal):
#
#     def shut(self):
#         super().shut()
#         print("汪汪汪")
#
#
# dog = Dog()
# dog.shut()

'''
3. 创建猫类：
类名：Cat
属性：无
描述：创建一个Cat类，通过Cat类创建一个对象cat，
执行print(cat)输出“喵？喵？喵？”.
'''


# class Cat(object):
#
#     def __init__(self):
#         pass
#
#     def cat(self):
#          print("小花猫，喵喵喵！！！")
#
#
# A = Cat()
# A.cat()


'''
4.创建计算器类：
类名：Calculator
属性：number_1（数字一）、number_2（数字二） 
方法：
def __init__(self,number_1,number_2): 
# 类的初始化方法
def add(self) # 返回数字一加数字二的值 
def sub(self) # 返回数字一减去数字二的值
def div(self) # 返回数字一除以数字二的值
def mul(self) # 返回数字一乘以数字二的值
描述：创建计算器类，通过计算器类创建一个计算器对象，
在创建对象时需要传入数字一和数字二，分别调用计算器的四种方法.
'''


# class Calculator(object):
#     def __init__(self, number_1, number_2):
#         self.number_1 = number_1
#         self.number_2 = number_2
#
#     def add(self):
#         return self.number_1 + self.number_2
#
#     def sub(self):
#         return self.number_1 - self.number_2
#
#     def div(self):
#         return self.number_1 / self.number_2
#
#     def mul(self):
#         return self.number_1 * self.number_2
#
#
# HL = Calculator(40, 2)
# print(HL.add())
# print(HL.div())
# print(HL.mul())
# print(HL.sub())

'''
5.创建Cat和Dog类分别继承Animal类，分别重写shut和eat方法，
创建Cat类对象cat和Dog类对象dog，分别调用cat和dog的shut和eat方法
class Animal:

def shut(self):
# 打印叫声
pass

def eat(self):
# 打印爱吃的食物
pass
'''


# class Animal(object):
#
#     def __init__(self):
#         pass
#
#     def shut(self):
#         pass
#
#     def eat(self):
#         pass
#
#
# class Cat(Animal):
#
#     def __init__(self):
#         super().__init__()
#
#     def shut(self):
#         print("小花猫，喵喵喵！！！")
#
#     def eat(self):
#         print("小花猫，最爱吃鱼！！！")
#
#
# class Dog(Cat):
#
#     def __init__(self):
#         super().__init__()
#
#     def shut(self):
#         print("小欢狗，汪汪汪！！！")
#         super().shut()
#
#     def eat(self):
#         print("小欢狗，最爱吃骨头！！！")
#         super().eat()
#
#
# AL = Dog()
# AL.shut()
# AL.eat()


'''
1、面向对象三大特性是:封装、继承、多态
'''