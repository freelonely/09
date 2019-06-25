
# 单元划分(python)
# 变量 -> 函数 -> 类 -> 模块 -> 包 -> 项目
def my_print():
    print("                            _ooOoo_  ")
    print("                           o8888888o  ")
    print("                           88  .  88  ")
    print("                           (| -_- |)  ")
    print("                            O\\ = /O  ")
    print("                        ____/`---'\\____  ")
    print("                      .   ' \\| |// `.  ")
    print("                       / \\||| : |||// \\  ")
    print("                     / _||||| -:- |||||- \\  ")
    print("                       | | \\\\\\ - /// | |  ")
    print("                     | \\_| ''\\---/'' | |  ")
    print("                      \\ .-\\__ `-` ___/-. /  ")
    print("                   ___`. .' /--.--\\ `. . __  ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                            `=---='  ")
    print("  ")
    print("         .............................................  ")
    print("                  佛祖镇楼                  BUG辟易1  ")
    print("          佛曰:  ")
    print("                  写字楼里写字间，写字间里程序员；  ")
    print("                  程序人员写程序，又拿程序换酒钱。  ")
    print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                  酒醉酒醒日复日，网上网下年复年。  ")
    print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                  奔驰宝马贵者趣，公交自行程序员。  ")
    print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                  不见满街漂亮妹，哪个归得程序员？")

# 函数的调用
my_print()

#函数的作用:
# 提高开发效率 减少重复代码的出现
# 函数是对某个功能点的解释


# 定义一个变量
num = 10
# 使用num
print(num)

# 函数定义
# def -> define 定义的意思(定义函数或者方法的关键字)
# 格式: def 函数名():
#           代码实现
def my_print():
    print("你好中国")

# 函数的调用(执行)
# 格式: 函数名()
my_print()


#
# # 求和 -> 函数 (10 + 5)
# def my_func():
#     # 定义两个变量
#     a = 10
#     b = 5
#     ret = a + b
#     print("和:%d" % ret)
#
#
# # 调用函数
# my_func()
#
# # 求和 -> 函数 (11 + 6)
# def my_func1():
#     # 定义两个变量
#     a = 11
#     b = 6
#     ret = a + b
#     print("和:%d" % ret)
#
#
# # 调用函数
# my_func1()

# # 定义一个有参数的函数(有多少个形参看的是业务需求)
# # 格式: def 函数名(参数1(形参1), 参数2(形参2),...):
# #          代码逻辑
# def my_func(num1, num2):
#     ret = num1 + num2
#     print("和:%d" % ret)
#
# # 调用一个有参数的函数(有多少个实参要看函数有多少个形参)
# # 格式: 函数名(参数1(实参1), 参数2(实参2),...)
# my_func(10, 5)
# my_func(11, 6)





# 定义一个有参数的函数(有多少个形参看的是业务需求)
# 格式: def 函数名(参数1(形参1), 参数2(形参2),...):
#          代码逻辑
def my_func(num1, num2):
    ret = num1 + num2
    print("和:%d" % ret)

# 调用一个有参数的函数(有多少个实参要看函数有多少个形参)
# 格式: 函数名(参数1(实参1), 参数2(实参2),...)
a = 10
b = 5
my_func(a, b)


# 函数的定义
# def add2num(a, b):
#     ret = a + b
#     return ret
#
# # 函数的调用
# # a = 10
# # b = 11
# # add2num(a, b)
# result = add2num(10, 11)
# print(result)

# 定义一个函数 计算列表的的元素个数 -> 模拟python内置函数的len函数
# 格式: 函数名(形参1, 形参2,...):
#       代码逻辑
#       return 返回值
def hm_len(my_list):
    #定义一个变量记录循环次数
    index = 0
    # 遍历my_list
    for value in my_list:
        index += 1

    return index

# 函数调用
# 格式: 变量名 = 函数名(实参1, 实参2,...)
# ret = hm_len([1, 3, 5])
# print(ret)

# 4种函数的类型
# 无参数无返回值
# 无参数有返回值
# 有参数无返回值
# 有参数有返回值

# 无参数无返回值
# 通过函数打印你好龟叔
# 格式: def 函数名():
#           代码逻辑
# def my_print():
#     print("你好龟叔")
# # 函数的调用
# # 格式: 函数名()
# my_print()


# 无参数有返回值
# 通过调用函数得到一个3.1415926
# 格式: def 函数名():
#           return 返回值
# def get_pi():
#     return 3.1415926
#
# # 格式: 变量名 = 函数名()
# pi = get_pi()
# print(pi)


# 有参数无返回值
# 格式: def 函数名(形参1,...):
#           代码逻辑
# def my_print(s):
#     print("你好%s" % s)
#
# # 格式: 函数名(实参1,...)
# my_print("中华")


# 有参数有返回值
# 格式: def 函数名(形参1,...):
#           return 返回值
def my_print(s):
    ret = "你好" + s
    return ret

# 格式: 变量名 = 函数名(实参1,...)
result = my_print("共产党")
print(result)


# 定义三个函数
def my_func1():
    print("最后结果")


def my_func2():
    print("func2开始")
    my_func1()
    print("func2结束")


def my_func3():
    print("func3开始")
    my_func2()
    print("func3结束")

# 调用my_func3
print("开始-")
my_func3()
print("结束-")
"""
print("开始-")
print("func3开始")
print("func2开始")
print("最后结果")
print("func2结束")
print("func3结束")
print("结束-")
"""

# 特列
# def my_func111():
#
#     def my_func222():
#         print("haha")
#
#     my_func222()
#
#
# my_func111()

# 如果两个函数名相同 那么最后一个函数会覆盖前面的函数
# def aaa():
#     print("小样")
#
# def aaa():
#     print("大洋")
#
# aaa()

num = 10
num = 20




# #  打印一条横线
# def printOneLine():
#     print("-"*30)
#
# # 打印自定义行数的横线
# def printLines(count):
#     for i in range(count):
#         printOneLine()
#
# printLines(10)


# 写一个函数求三个数的和
def add3num(a, b, c):
    return a + b + c

# ret = add3num(10, 11, 12)
# print(ret)

# 写一个函数求三个数的平均值
def average3Number(num1, num2, num3):
    # ret = num1 + num2 + num3
    ret = add3num(10, 11, 12)
    return ret/3

print(average3Number(10, 11, 12))




# 定义一个函数
def add2num(a, b):
    ret = a + b
    print(ret)

# 函数调用之位置参数
# 实参的位置要和形参的位置一一对应
# 如果实参的位置发生改变 那么形参的值也就发生了改变
add2num(10, 11)



# 定义一个函数
def add2num(a, b):
    print(a)
    print(b)
    ret = a + b
    print(ret)

# 函数调用之关键字参数
# 在调用函数的时候找到函数形参的名字 直接赋值
# 关键字参数特点: 不需要考虑当前参数的位置
add2num(b=11, a=10)
