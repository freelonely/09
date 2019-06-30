# Date：2019/6/27
# Name: TONGQIANG
# -*- coding:utf-8 -*-


'''
1、python 2.x ,3.x 默认的编码格式分别是什么？

 Python 2：Python 2的源码.py文件的默认编码方式为ASCII，
 Python 3：Python 3的源码.py文件的默认编码方式为UTF-8。
 因此，如果要在python2的py文件里面写中文，则必须要添加
 一行声明文件编码的注释，否则python2会默认使用ASCII编码：

'''

'''
2、将“hello_new_word”按“-”符进行切割。
第一种：split()函数
split()函数应该说是分割字符串使用最多的函数
用法：
str.split('分割符')
通过该分割操作后，会返回一个列表。
注：当然如果你的字符串含有一个或者多个空格就直接 str.split() 就可以了
例如：
>>> a = "hello,python,Good Night"
>>> a.split(',')
['hello', 'python', 'Good Night']
'''
# A = 'hello_new_word'
# print(A.split("_"))

'''
3、将数字1以"0001"的格式输出到屏幕
'''
# for i in range(1, 2):
#     m = "%04d" % i
#     print(m)
# a = 1
# b = "%04d" % a
# print(b)

'''
1、字典a = {1: 1},是否正确？
   答案：对
'''
# a = {1: 1}
# print(type(a))
# print(a)

'''
2、请合并列表a=[1,2,3,4]和列表b=[5,6,7,8]
'''
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
#
# print(a + b)

'''
3、列表a ,请写出实现正序排列，倒序排列，逆序排列的内置方法
'''

# a = [1, 8, 9, 10, 15, 50, 4]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# b = [1, 8, 9, 10, 15, 50, 4]
# b.reverse()
# print(b)

'''
4、字典 d = {"k":1, "v":2},请写出d.items()结果
dict_items([('k', 1), ('v', 2)])
'''
# d = {"k": 1, "v": 2}
# print(d.items())

'''
5、复杂列表[{"k": 1, "v": 2}, {"k": 12, "v": 22}, {"k": 13, "v": 32}]
请用内置方法写出按k倒序排列的代码
'''
# li = [{"k": 1, "v": 2}, {"k": 12, "v": 22}, {"k": 13, "v": 32}]
# newlist = sorted(li, key=lambda k: k['k'], reverse=True)
# print(newlist)
'''
6、集合 s = set([1, 2, 3, 4]),d = set([2, 4, 9, 0, 3]),请用内置方法
写出他们的并集，交集，对称差
'''
# s = set([1, 2, 3, 4])
#
# d = set([2, 4, 9, 0, 3])
#
# bj = list(s | d)  #并
# print(bj)
# inter = list(s & d) # 交
# print(inter)
# sys = list(s ^ d)
# print(sys)  # 对称差
# diff = list(s-d)
# print(diff)      # 差


'''
7、如何把列表 a = ["a","b"]里的各项，转化为字符串并用逗号“，”连接
'''

# a = ["a", "b"]
# print(",".join(a))

'''
1、 一行代码实现求1到100的和
'''
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)

'''
2、按下面要求写出完整代码：
使用random.random 方法实现随机输出范围在[25,60）中的浮点数。
'''
# import random
#
# lis = random.uniform(25, 60)
# print(lis)

'''
2、 一个list 对象 a = [1, 2, 4, 3, 2, 2, 4],需要去掉里面的重复值

'''
# a = [1, 2, 4, 3, 2, 2, 4]
# new_a = list(set(a))
# print(new_a)
