#   Date: 2019/6/27 0027
#   Name: life
#  _*_ coding:UTF-8  _*_

"""
python3.x版本中，系统默认的编码方式就是Unicode编码方案中的utf-8。
python2.x中，系统默认的编码方式是ASCII
"""

#将"hello_new_world"按"_"f符进行切割
# str = "hello_new_world"
# info = str.split("_")
# print(info)

#将数字1以"0001"的格式输出到屏幕
# num=1
# print("%04d" % num)

#字典a={1: 1}正确
# a = {1: 1}
# print(type(a))

#请合并列表a=[1,2,3,4]和列表b=[5,6,7,8]
# a=[1,2,3,4]
# b=[5,6,7,8]
# a.extend(b)
# print(a)

#列表a,请写出实现正序排列，倒序排列，逆序排列的内置方法
# a=[3,4,2,5,4,5,5]
#正序排列
# a.sort()
# print(a)
# #降序排列
# a.sort(reverse=True)
# print(a)
#逆序排列
# a.reverse()
# print(a)

#字典d={"k":1,"V":2}请写出d.items()的结果:dict_items([('k', 1), ('V', 2)])
# d={"k":1,"V":2}
# print(d.items())

#复杂列表[{"k":1,"V":2},{"k":12,"V":22},{"k":13,"V":32}],请用内置方法写出K倒序的排列的代码
a=[{"k":1,"V":2},{"k":13,"V":32},{"k":12,"V":22}]
# num=[]
# for c in a :
#     num.append(c["k"])
# num.sort(reverse = True)
# print(num)
# a.sort(key=lambda x:x["k"],reverse=True)
# print(a)

#集合s=set([1,2,3,4]),d=set([2,4,9,0,3]),请用内置方法写出他们的并集、交集，对称差
# s=set([1,2,3,4])
# d=set([2,4,9,0,3])
# #交集
# print(s&d)
# #并集
# print(s|d)
# #对称差
# sys=s.symmetric_difference(d)
# print(sys)
#如何把列表a=["a","b"]里的各项，转为字符串并用逗号‘，’连接
# a=["a","b"]
# b=",".join(a)
# print(b)
# print(type(b))

#一个list对象：a=[1,2,4,3,2,2,4],需要去掉里面的重复值
# a=[1,2,4,3,2,2,4]
# a=set(a)
# a=list(a)
# print(a)

#一行代码求1到100之和
print(sum(range(1,101)))

#使用random.random方法实现随机输出范围在（25,60）的浮点数
'''函数随机生成一个[a,b]范围内的浮点数：random.uniform(a, b)'''
import random
# print(random.uniform(25,60))

import  random
booll = True
while booll:
    num = random.random()
    print(num)
    # new_num = num * 100
    # if 28 <= new_num < 60:
    #     print(new_num)
    #     booll = False
    # else:
    #     booll = True
"""
1、错（键必须是不可变数据类型：元组、int、bool,str）字典：具有键值映射关系，无序，字典的键是可以重复的任意数据类型且被后边值覆盖前边值
2、错（不可变数据类型，但是有序可以切片）元组：不能修改，有序，可以索引切片，当元组中只有一个元素时，需要在元素的后面加逗号。
3、错（列表可以反向索引）列表：元素是可以重复，有序，不可以方向索引，元素可以是任意类型。
4、错（无序，不能索引，a={}为空字典）集合：元素不可以重复，不可以索引，必须a=set()这样声明空集合。
"""
