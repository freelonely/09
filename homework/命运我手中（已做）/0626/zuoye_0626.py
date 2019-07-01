# Date: 2019/6/27
# Name: connor
# _*_ conding:utf-8 _*_

# 4题
# Python2 中默认把脚步文件使用 ASCII 来处理
# Python2 中字符串除了 str 还有 Unicode，可以用 decode 和 encode 相互转换
# Python3 中默认把脚步文件使用 UTF-8 来处理
# Python3 中文本字符和二进制分别使用 str 和 bytes 进行区分，也是使用 decode 和 encode 进行相互转换

# 5题   以"_"进行分割
str = "hello_new_world"
new_str = str.split("_")
print(new_str)

# 6题  将数字1以"0001"格式输出
for i in range(1, 2):
    m = "%04d" % i
    print(m)

# 1题
# 字典a = {1: 1}是否正确？       正确

# 2题  合并列表
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
new_list = a.extend(b)
print(a)

# 3题   正序、倒序、逆序
lista = [1, 5, 2, 9, 13, 8, 32, 25]
lista.sort()
print(lista)
lista.reverse()
print(lista)
listb = sorted(lista)
print(listb)

# 4题
# d = {"k": 1, "v": 2}  d.items()的结果是
# [("k", 1), ("v", 2)]

# 5题
set_a = {}
print(type(set_a))

# 2题一行代码实现1到100的和
print(sum(range(1, 101)))

import random
ran = random.random()
print(ran)

# 3题 去掉list中的重复值
Alist = [1, 2, 4, 3, 2, 2, 4]
new_Aset = set(Alist)
new_Alist =list(new_Aset)
print(new_Alist)

# 7题 将列表转换成字符串并用","连接
listc = ["a", "b"]
str1 =",".join(listc)
print(str1)
