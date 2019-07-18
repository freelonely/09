# 我是blanny
#DATE ：2019-07-09
# 补0701作业
"""
1、创建一个对象后默认调用( A )
A、__init__    B、__str__    C、__add__    D、__and__
2、类是对象的__抽象_____、对象是类的__实例_____.
3、对象是由_数据_、__相关操作___两部分构成.
"""

"""
4、创建学生类：
	类名：Student
	属性：name（姓名）、age（年龄）、sex（性别）
方法：
	def info(self) # 打印学生的姓名、年龄、性别
	def draw(self) #打印”XX会画画呢”
描述：创建学生类，通过学生类创建一个学生对象，分别调用学生的info方法和draw方法.
"""
# class  Student(object):
#     def __init__(self, i_name = None, i_age  = None, i_sex = None):
#         self.name = i_name
#         self.age = i_age
#         self.sex = i_sex
#
#     # 打印学生的姓名、年龄、性别
#     def info(self):
#         print("学生姓名：%s\n年龄： %s\n性别：%s" % (self.name, self.age,self.sex))
#
#     # 打印”XX会画画呢”
#     def draw(self):
#         print("%s会画画呢" % self.name)
#
# jiajia = Student("佳佳", 12, "女")
# jiajia.info()
# jiajia.draw()

"""
5、创建动物类：
	类名：animal
	属性(使用魔法方法实现)：name（姓名）、age（年龄）、color（颜色） 
方法：
	def info(self) # 打印姓名、年龄、毛颜色
	def run（self）#打印“XX会跑呢”
描述：创建动物类，通过动物类创建一个动物对象，分别调用动物的info和run方法.
"""
class animal(object):
    def __init__(self, a = None,b = None, c = None):
        self.name = a
        self.age = b
        self.color = c

        # 打印姓名、年龄、毛颜色
    def info(self):
        print("名字：%s\n年龄： %s\n毛颜色：%s" % (self.name, self.age, self.color))

        # 打印”XX会跑呢”
    def run(self):
        print("%s会跑呢" % self.name)

dd = animal("豆豆", 2, "白色")
dd.info()
dd.run()