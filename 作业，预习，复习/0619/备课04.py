# tab ====> 四个空格
# 回退一个tab键====> shift tab
# (取消)注释的快捷键====> ctrl + ?
# 写错时回退 ctrl + z
# ctrl + a  =====  全选

# for-else
# # 当for循环循环完成以后 然后会执行else中的代码
# for i in range(5):
#     print(i)
# else:
#     print("进入else")

# 当for循环中执行了break 那么else中的代码将不会执行
# for i in range(5):
#     print(i)
#     if i == 2:
#         break
# else:
#     print("进入else")


# while-else
# while-else 的结论可以完全参考for-else结论
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1
else:
    print("执行了else")

# 字符串就是一个有序的字符序列(保存字符的)
# 输入引导的文字
# name = "名字"
# input("请输入您的%s" % name)

# 输入一段文字 我爱您中国
# result = "中国"
# 我爱您中国
# result1 = "我爱您%s" % result
# print(result1)


# 字符串的定义
# 01:格式
# my_str1 = "hello world"
# my_str2 = 'hello world'
# # 在python中 '' 和""意义是一样
# if my_str1 == my_str2:
#     print("等价的")

# 02 如果想保留文本内容格式
# 如果保留文本的格式 可以使用 """""" 或者 ''''''
# my_str = """你好
# 中国
# 你好
# 龟叔"""
# print(my_str)


# 03 空字符串(一个字符都没有而且有"" 或者 '')
# 定义了一个空的字符串
my_str1 = ""
my_str2 = '111222'
# 类名创建一个空字符串
my_str3 = str()

# python内置函数(python直接提供的函数 服务于程序员)
# len函数 是来计算字符串中字符(元素)的个数
l = len(my_str2)
print(l)


# 字符串其实就是一个有序的字符序列(保存字符的)(字符串中最小单元就是字符)

my_str = "hello"
# 打印其my_str中e
# 下标索引 或者是 下标 或者 索引
# python中下标索引是从0开始的(顺序是从左到右)
# ret1 = my_str[1]
# print(ret1)
# 也可以通过从右到左获取e这个字符(从右到左是从-1开始)
# ret2 = my_str[-4]
# print(ret2)


# 依次的打印字符串中每个字符
# -for循环
# for c in my_str:
#     print(c)

# -while循环
# 定义一个变量
i = 0
# 计算下字符串的字符个数
l = len(my_str)
while i < l:
    # 通过下标获取对应的字符
    ret = my_str[i]
    print(ret)
    i += 1
	

# 切片的语法：[起始:结束:步长]

# python中的切片 其实可以理解为字符串的截取(得到字符串中的某个字符或者一个字符片段)
# >>> a = "abcdef"
#  'abc'
#  'ace'
#  'bd'
#  'fdb'
#  'fd'
# python中字符串是不可变(当执行切片的操作时候 其本身不会发生改变)

# 定义一个字符串
a = "abcdef"
#  'abc'
# 默认情况下 步长不写就是为1的
# ret1 = a[0:3]
# 简写
# ret1 = a[:3]
# print(ret1)

#  'ace'
# ret2 = a[:5:2]
# print(ret2)

#  'bd'
# ret3 = a[1:4:2]
# print(ret3)

#  'fdb'
# 倒序
# ret4 = a[::-2]
# print(ret4)

#  'fd'
# ret5 = a[-1:-4:-2]
# print(ret5)


# 条条大路通罗马

# 内置函数前面什么都没有 只有一个函数名而已
# 字符串中的使用的都是方法 方法前面是字符串
# len()

# 定义一个字符串
a = "abcdcecf"
# <1>find
# 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
# index = a.find("1")
# print(index)

# <2>index
# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
# index = a.index("q")
# print(index)

# <3>count
# 返回 str在start和end之间 在 mystr里面出现的次数
# count = a.count("1")
# print(count)

# <4>replace
# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# ret1 = a.replace("c", "q", 1)
# print(ret1)

# <5>split
# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
# ret = a.split("c")
# # ['ab', 'd', 'e', 'f']
# print(ret)



# 定义一个字符串
a = "AbCD"
# <6>capitalize
# 把字符串的第一个字符大写
# ret1 = a.capitalize()
# print(ret1)

# <7>title
# 把字符串的每个单词首字母大写
# ret2 = a.title()
# print(ret2)

# <8>startswith
# 检查字符串是否是以 hello 开头, 是则返回 True，否则返回 False
# flag = a.startswith("1ab")
# print(flag)

# <9>endswith
# 检查字符串是否以obj结束，如果是返回True,否则返回 False.
# flag = a.endswith(".mp4")
# print(flag)

# <10>lower
# 转换 mystr 中所有大写字符为小写Afre -> AFRE
# ret = a.lower()
# print(ret)

# <11>upper
# 转换 mystr 中的小写字母为大写
# ret = a.upper()
# print(ret)


# 定义一个字符串
a = "ppooabcdiii"
# <12>ljust
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# ret = a.ljust(6, "x")
# print(ret, end="-")

# <13>rjust
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# ret = a.rjust(6, "x")
# print(ret)

# <14>center
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
# ret = a.center(6, "x")
# print(ret)

# <15>lstrip
# 删除 mystr 左边的空白字符
# ret = a.lstrip("pob")
# print(ret)

# <16>rstrip
# 删除 mystr 字符串末尾的空白字符
# ret = a.rstrip("i")
# print(ret)

# <17>strip
# 删除mystr字符串两端的空白字符
# ret = a.strip("pio")
# print(ret)

# <18>rfind
# 类似于 find()函数，不过是从右边开始查找.

# <19>rindex
# 类似于 index()，不过是从右边开始.

a = "    "
# <20>partition
# 把mystr以str分割成三部分,str前，str和str后
# ret = a.partition("cd")
# print(ret)

# <21>rpartition
# 类似于 partition()函数,不过是从右边开始.
# ret = a.rpartition("f")
# print(ret)

# 22>splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
# ret = a.splitlines()
# print(ret)

# <23>isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
# flag = a.isalpha()
# print(flag)

# <24>isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False.
# flag = a.isdigit()
# print(flag)

# <25>isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
# flag = a.isalnum()
# print(flag)

# <26>isspace
# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
# flag = a.isspace()
# print(flag)


# <27>join -> 列表 -> 字符串
# 定义一个列表
# my_list = ["ab", "cd", "ef"]
# # 最终打印一个结果abxcdxef
# ret = "".join(my_list)
# print(ret)


# 技巧
a = "hello"
# str 数据类型
print(type(a))
# 内置函数(帮助查询某个类中的方法文档)
# 查看所有
help(str)
# 查看某一个
help(str.count)



# 列表中可以承载任意的数据类型
# 列表其实就是一个容器类型(承载数据是有序的) -> 支持下标索引
# 格式: 列表名 = [元素1, 元素2,...]
# my_list = [1, 3.14, True, "hello"]

# print(my_list)
# 打印3.14
# result = my_list[1]
# print(result)



# 定义一个字符串的标识符号 ""
# 定义一个列表的标识符号 就是一个[]

# 定义一个特殊的列表 -> 空列表 (列表中没有一个元素)
my_list1 = []
# <class 'list'>
print(type(my_list1))
# 计算列表中有多少个元素
# l = len(my_list1)
# print(l)
my_list2 = list()
print(len(my_list2))



# 定义一个列表

# my_list = ["a", "b", "c", "d"]

# 简写
my_list = list("abcd")
# print(my_list)


# 循环遍历

# -for循环
# for value in my_list:
#     print(value)

# -while
i = 0
while i < len(my_list):
    # 通过下标获取元素
    # value = my_list[i]
    # print(value)
    print(my_list[i])
    i += 1
	
	

# 列表是可变的 改变其本身

# 定义一个列表
my_list = ["a", "b"]


# append 是添加元素是一个整体 可以是任意类型
# my_list.append(["c", "d"])
#
# print(my_list)


# extend 一般添加的是 字符串 或者是 列表
# my_list.extend([1, 2, 3])
# print(my_list)


# insert 插入数据
my_list.insert(1, "hello")
print(my_list)


# 定义一个列表
my_list = ["1", "张三", "李四", "张三"]


# 修改元素
# 把张三改成双击666
# my_list[1] = "双击666"
# print(my_list)


# 查找元素
# in
# 判断一个元素是否存在一个列表中
# if "张三" in my_list:
#     print("张三是列表的元素")

# not in
# if "张三1" not in my_list:
#     print("张三1不再列表中")

# index
# 判断一个元素在列表中的位置(下标索引)
# index = my_list.index("李四1")
# print(index)

# 先判断李四1是否存在
# if "李四" in my_list:
#     # 如果存在
#     index = my_list.index("李四")
#     print(index)
# else:
#     print("李四不存在")


# count
count = my_list.count("张三1")
print(count)