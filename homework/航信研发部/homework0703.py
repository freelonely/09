# 我是blanny
#DATE ：2019-07-09
# 补0703作业
"""
3. 创建猫类：
	类名：Cat
	属性：无
描述：创建一个Cat类，通过Cat类创建一个对象cat，执行print(cat)输出“喵？喵？喵？”.
"""
# class Cat(object):
#     def __str__(self):
#         return "喵？喵？喵？"
# cat = Cat()
# print(cat)
"""
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
描述：创建计算器类，通过计算器类创建一个计算器对象，在创建对象时需要传入数字一和数字二，分别调用计算器的四种方法.
"""
# class Calculator(object):
#     def __init__(self, number_1 = None, number_2  = None):
#         self.number_1 = number_1
#         self.number_2 = number_2
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
# Cala = Calculator(6, 3)
# print(Cala.add())
# print(Cala.sub())
# print(Cala.div())
# print(Cala.mul())
"""
5.创建Cat和Dog类分别继承Animal类，分别重写shut和eat方法，创建Cat类对象cat和Dog类对象dog，分别调用cat和dog的shut和eat方法
"""
# class Animal(object):
#     def shut(self):
#         print("动物的叫声")
#
#     def eat(self):
#         print("动物爱吃的食物WWWWWWW")
#
# class Cat(Animal):
#     def shut(self):
#         print("喵喵喵")
#     def eat(self):
#         print("鱼")
#
# class Dog(Animal):
#     def shut(self):
#         print("汪汪汪")
#     def eat(self):
#         print("骨头")
#
# cat = Cat()
# cat.shut()
# cat.eat()
#
# dog = Dog()
# dog.shut()
# dog.eat()


