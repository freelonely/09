
# 删除元素("删"del, pop, remove)
# 定义一个列表
my_list = ["a", "3.14", "hello"]

# del
# 格式: del 列表名[下标索引]
# IndexError: list assignment index out of range 索引越界
# del my_list[10]
# print(my_list)

# pop
# 格式: 列表名.pop(下标索引)
# my_list.pop(11)
# print(my_list)
#如果pop()里面不添加索引 默认删除列表中的最后一个
# my_list.pop()
# my_list.pop()
# print(my_list)

# remove
# 格式: 列表名.remove(元素的值)
# my_list.remove("a")
# print(my_list)

# 如果有元素的值3.14 再通过pop删除
# 判断3.14是否是my_List的元素
# if "3.14" in my_list:
#     index = my_list.index("3.14")
#     my_list.pop(index)


# if my_list.count("3.14"):
#     index = my_list.index("3.14")
#     my_list.pop(index)
#     print(my_list)


# 定义一个列表
my_list = [8, 6, 10, 1, 2]


# 排序(sort, reverse)
# sort 升序(从小到大)
# my_list.sort(reverse=False) 等价于 my_list.sort()
# my_list.sort()
#
# print(my_list)


# 降序(从大到小)
my_list.sort(reverse=True)
print(my_list)


# schoolNames = [['北京大学', '清华大学'], ['南开大学', '天津大学', '天津师范大学'], ['山东大学', '中国海洋大学']]
# # 得到天津大学
# my_list = schoolNames[1]
# # ['南开大学', '天津大学', '天津师范大学']
# # print(my_list)
# # 得到结果
# result = my_list[1]
# print(result)

# print(schoolNames[1][1])
# print(schoolNames[2][0])

# 导入模块
import random

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
school_list = [[], [], []]
# school_list[1].append("A")
# print(school_list)

# 定义8个老师
teacher_list = list("ABCDEFGH")
# print(teacher_list)

#for循环
for name in teacher_list:
    # print(name)
    # 产生随机数(代表的是school_list的下标索引)
    index = random.randint(0, 2)
    # 给随机产生的下标索引获取的元素进行添加数据
    school_list[index].append(name)

# 查看数据
print(school_list)

"""
总结:
    - "" 或者 ''  或者 三"  -> 字符串
    - [] -> 列表
    - () -> 元组
"""
# 元组是不可变的 因为他的元素是不可以修改的(程序员不可以对元组做增删改的操作)

# 定义一个元组
# 格式: 元组名 = (元素1, 元素2, ...)
# my_tuple = (1, 3, 5)
# TypeError: 'tuple' object does not support item assignment
# 测试元组的元素数据不可以修改
# my_tuple[1] = 10

# 定义一个空的元组
# my_tuple = tuple()
#len函数中的o -> object -> 对象
# l = len(my_tuple)
# print(l)
# my_tuple = ()
# <class 'tuple'> 元组的类型
# print(type(my_tuple))

# 定义一个特殊的元组
# 当程序员定义了一个元组 有且只有一个元素 (元素,)
# my_tuple = (3.14,)
# print(type(my_tuple))

# in not index count
my_tuple = (1, 3, 5)

# in 存在
#  if 3 in my_tuple:
#     print("存在")

# not in 不存在
# if 33 not in my_tuple:
#     print("不存在")

# index
# index = my_tuple.index(33)
# print(index)

# count
# count = my_tuple.count(5)
# print(count)

# 得到元组中的3这个值
# value = my_tuple[1]
# print(value)

# 循环
# for循环
# for value in my_tuple:
#     print(value)

# 数据类型转换
# my_tuple = tuple([1, 3, 5])
# print(my_tuple)
# my_list = list(my_tuple)
# print(my_list)
# 分析: 为什么出现了元组这个类型?
# 数据安全


# 字典的的key和value是一一对应的
# 字典中的key是唯一的
# 注意注意注意: 但是这个数据类型必须是不可变的
# (不能作为key的数据类型列表 字典)
# 字典是无序的
# 定义一个字典
#
# my_dict = {"name": "小明", "age": 20, "name": "小红"}
# 查看类型
# <class 'dict'>
# print(type(my_dict))
# "name" -> 键值 key
# "小明" -> 实值 value
# "name": "小明" -> 键值对 -> key-vale -> 元素
# print(my_dict)
# my_dict1 = {1: "哈哈", 3.14: "hello"} 实际开发中用的很少 一般情况下都是使用字符串作为key


# 定义一个空的字典
# my_dict = dict()
# print(type(my_dict))
# my_dict = {}
# print(type(my_dict))

# 通过key获取value (字典是无序的-> 不支持下标索引获取数据)
# my_dict = {"name": "小明", "age": 20}
# # 打印小明
# my_name = my_dict["name"]
# print(my_name)



# 字典是可变
my_dict = {'name':'吴彦祖','age':50}

# <1>查看元素
# 通过key获取value 如果key存在得到对应的value 如果key不存在 将报错
# my_name = my_dict["name1"]
# print(my_name)

# <2>修改元素 -添加元素
# 把age的value改成70
#如果通过key修改字典中的value  如果key存在于字典中 那么直接修改对应的value
# 如果key不存在 那么系统会自动添加一个新的元素(key-value)
# my_dict["age1"] = 70
#
# print(my_dict)

# <4>删除元素
# del
# 格式: del 字典名[key]
# del my_dict["age"]
# print(my_dict)

# clear -> 清空 - 等价于 my_dict = {}
# my_dict.clear()
# print(my_dict)


# 定义一个字典
# my_dict = {"name": "小明", "age": 20, "no": "007"}

# <1>len() -> 计算字典中的键值对的个数
# l = len(my_dict)
# print(l)

# <2>keys
# keys = my_dict.keys()
# dict_keys(['name', 'age', 'no']) 就是一个列表
# 我就想把dict_keys作为列表使用 -> 解决方案 把dict_keys 转成list
# print(list(keys)[0])

# <3>values
# values = my_dict.values()
# print(values)

# <4>items
# items = my_dict.items()
# [('name', '小明'), ('age', 20), ('no', '007')]
# print(items)

my_dict = {"name": "小明", "age": 20, "no": "007"}
## 判断一个key是否存在
# 通过in 判断某个key是否存在于一个字典中
# if "小明" in my_dict:
#     print("哈哈")

# setdefault
# 通过key获取value 如果key存在 那么会返回这个value 而且dict没有任何影响
# ret = my_dict.setdefault("name", "老王")
# print(ret)
# print(my_dict)

# 通过key获取value 如果key不存在 那么会返回设置的默认值(老王) 然后把这个键值对添加到字典中
# ret = my_dict.setdefault("name1", "老王")
# print(ret)
# print(my_dict)

# get
# get 等价于setdefault (name是存在的)
# ret = my_dict.get("name", "老王")
# print(my_dict)
# print(ret)

# 通过key获取value 如果key不存在 那么会返回设置的默认值(老王) 不会对字典做任何操作
# ret = my_dict.get("name1", "老王")
# print(my_dict)
# print(ret)

# get 和setdefault区别是在于这个key不存在然后对字典是否造成影响(是否添加新的键值对)



# 字符串
# my_str = "abed"
#
# for c in my_str:
#     print(c)

# 列表
# my_list = [1, 3, 5, 7]
# for value in my_list:
#     print(value)

# 元组
# my_tuple = (2, 4, 6, 8)
#
# for value in my_tuple:
#     print(value)

# 定义一个字典
my_dict = {"name": "小明", "age": 20, "no": "007"}

# 遍历key
# for value in my_dict.keys():
#     print(value)

# 遍历value
# for value in my_dict.values():
#     print(value)

# 遍历item
# for value in my_dict.items():
#     # print(value)
#     print("key=%s value=%s" % (value[0], value[1]))

# 直接获取到字典中的key 和value
# for key, value in my_dict.items():
#     # print(value)
#     print("key=%s value=%s" % (key, value))

# 列表
my_list = ["小明", "小红", "小刚"]

# for name in my_list:
#     print(name)
#     # 获取对应的下标索引
#     index = my_list.index(name)
#     print(index)

# i = 0
# for name in my_list:
#     print(name)
#     # 获取对应的下标索引
#     print(i)
#     i += 1

# 使用enumerate 可以吧列表中的元素和元素的对应的索引都可以得到
for i, name in enumerate(my_list):
    # 通过,隔开打印对应的变量  会有一个空格
    print(i, name)



# 集合的定义
# 集合是无序的(不可以通过下标获取元素) 而且集合中的元素是不重复的 -> 列表中的元素去重

# 定义一个正常的集合
# my_set = {1, 3, 5, 7, 20}
# 查看数据类型
# <class 'set'>
# print(type(my_set))
# print(my_set)

# 定义一个空的集合
# my_set1 = set()
# 不可以 {} 是空的字典
# my_set2 = {}


# 01 作用 去重使用
# my_list = [1, 3, 5, 3, 5, 7]
# my_set = set(my_list)
# print(my_set)
# my_list = list(my_set)
# print(my_list)


my_set = {1, 3, 5}
# 02 添加元素(add，update)
# my_set.add(10)
# print(my_set)

# 和列表中的extend相似
# my_set.update("abcd")
# print(my_set)


# 删除元素(remove，pop，discard)
# remove
# 格式:集合名.remove(元素值)
# my_set.remove(33)
# print(my_set)

# pop 任意的删除一个(因为集合是无序的)
# my_set.pop()
# print(my_set)

# discard
# 格式: 集合名.discard(元素值) (不同于remove 如果元素值不存在 不会报错)
# my_set.discard(33)
# print(my_set)


# 交集和并集( & 和 | )
# 定义两个列表
my_list1 = [1, 2, 3, 4]
my_list2 = [3, 4, 5, 6]

# 两个列表中相同的元素
my_set1 = set(my_list1)
my_set2 = set(my_list2)

# 得到交集
# new_set1 = my_set1 & my_set2
# ret = list(new_set1)
# # 进行排序
# ret.sort(reverse=True)
# print(ret)


# 得到并集
new_set2 = my_set1 | my_set2
print(new_set2)




# +
list1 = [1, 2]
list2 = [3, 4]

# extend
# list1.extend(list2)
# print(list1)

# 集合
# set1 = set(list1)
# set2 = set(list2)
# ret = set1 | set2
# print(ret)

# +
# ret = list1 + list2
# print(ret)

# ret = """*
# *
# **
# ***
# ****
# *****"""

# for i in range(1, 6):
#     print("*"*i)


my_list = [(2,3),(4,5), ({"name": [1, 33, 5]}, 11)]
# print(my_list)
# my_tuple = my_list[2]
# # ({'name': [1, 33, 5]}, 11)
# print(my_tuple)
# my_dict = my_tuple[0]
# # {'name': [1, 33, 5]}
# print(my_dict)
# value = my_dict["name"]
# # [1, 33, 5]
# print(value)
# ret = value[1]
# print(ret)
# result = my_list[2][0]["name"][1]
# print(result)

