
# 假设班级有95人 70人年龄都是 18 25人年龄分布于19~40

# 函数参数之缺省参数
# 在定义函数的时候 某个形参有自己的默认值(初始值)
# 在定义函数的时候 如果某个形参是缺省参数 
那么后面的形参都应该为缺省参数
def print_info(name, age=18):
    print("名字:%s" % name)
    print("年龄:%d" % age)
    print("-"*30)

# # 小明 20
# print_info("小明", 20)

# 函数的调用
# 如果一个形参为缺省参数 那么在调用函数的时候 
可以不传实参 那么默认会使用形参的初始值(默认值)
# print_info("小刚")
# # 小红 22
# 如果在缺省参数的位置传递了一个实参 
那么实参的值 会覆盖缺省参数的值
# print_info("小红", 22)

# my_list = [10, 3.14, True, "HELLO"]

# 开发中如何知道形参需要什么类型呢?
# 找当前函数定义者
# 找到函数的定义

# 崇尚的一切靠自觉
# def my_func(new_list):
#     print(new_list[0])
#     print(new_list[1])
#     print(new_list[2])
#     print(new_list[3])
#
# my_func([10, 3.14, True, "HELLO"])


# *args 不定长参数之元组
def my_func(*args):
    print(args)
    print(type(args))
    # print(args[0])

# 如果一个函数是不定长参数之元组 在调用其函数的时候 不需要写()
# 不定长参数 我们也称之为可变参数(函数的定义 不确定有多少个形参)
# 不定长参数之元组 这个元组还是一个缺省参数
# my_func(10, 3.14, True)
# my_func()


# 不定长参数之元组
# def my_func1(*args):
#     pass

# 调用 -> 遵循 位置参数(一一对应)
# my_func1(1, 2, 3)


# 不定长参数之字典
def my_func(**kwargs):
    # 验证kwargs是否是字典
    # print(type(kwargs))
    # print(kwargs["name"])
    # print(kwargs["age"])
    # print(kwargs["no"])
    print(kwargs)

# 调用 -> 遵循 关键字参数 (只要保证形参存在即可)
# my_func(name="小明", age=20, no="007")
# 验证如果不传入实参 说明不定长参数之字典 也是一个缺省参数
my_func()




# 定义一个函数(正常的形参 缺省参数 不定长参数之元组 不定长参数之字典)

# 函数的定义:
# 总结: 缺省参数的位置和不定长参数之元组的位置可以互换
(缺省参数级别和元组是同等)
# 如果在函数的定义中参数为不定长参数之字典 
那么应该定义在函数的最后面
def my_func(a, b, c=10, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


# 函数的调用
my_func(1, 3, 5, 7, 9, 11, name="小王", age=10)

# TypeError: my_func() got multiple values for argument 'a'
# 避免不定长参数之字典的key 和形参的名字相同
# my_func(1, 3, 5, 7, 9, 11, a=10)


# 传入小明 22 返回 姓名:小明 年龄:20
# 列表
# def deal_info(name, age):
#     # 构造两个字符串
#     my_name = "姓名:%s" % name
#     my_age = "年龄:" + str(age)
#     return [my_name, my_age]
#
# # 调用
# ret = deal_info("小明", 20)
# print(ret[0])
# print(ret[1])

# 字典
# def deal_info(name, age):
#     # 构造两个字符串
#     my_name = "姓名:%s" % name
#     my_age = "年龄:" + str(age)
#     return {"name": my_name, "age": my_age}
#
# # 调用
# ret = deal_info("小明", 20)
# print(ret["name"])
# print(ret["age"])


# 如果一个函数返回多个数据 可以使用return 返回值1, 返回值2,...
# return后面的数据其实就是一个省略了小括号的元组
# 元组 建议
def deal_info(name, age):
    # 构造两个字符串
    my_name = "姓名:%s" % name
    my_age = "年龄:" + str(age)
    return my_name, my_age

# 调用
ret = deal_info("小明", 20)
print(type(ret))
print(ret[0])
print(ret[1])
# 定义几个变量
# a = 10
# pi = 3.14
# flag = True
# my_str = "hello"

# 比较pythonic写法(变量名和值要一一对应)
# a, pi, flag, my_str = 10, 3.14, True, "hello"

# # 拆包 列表 和元组
# my_list = ["小明", "小红"]
# # 可读性不强
# # print(my_list[0])
# # print(my_list[1])
# my_name1, my_name2 = my_list
# print(my_name1)
# print(my_name2)
#
# # 元组
# num1, num2 = (10, 11)
# print(num1, num2)

# 如果一个函数有多个返回数据 也可以使用拆包技术
# def my_func(name, age):
#     return "姓名:" + name, "年龄:" + str(age)
# my_name, my_age = my_func("小明", 22)
# print(my_name, my_age)

# 交换2个变量的值
# 第1种方式
# a = 4
# b = 5
# c = 0
#
# c = a # c = 4
# a = b # a = 5
# b = c # b = 4
#
#
# print(a)
# print(b)

# 第2种方式
# a = 4
# b = 5
# a = a+b  # a = 9
# b = a-b  # b = 4
# a = a-b  # a = 5
# print(a)
# print(b)


# 第3种方式
a, b = 4, 5 # a = 4， b = 5
# 当61没有执行完 不能说明a就是等于5
a, b = b, a # a = 5， b = 4

print(a)
print(b)

