# Date：2019/6/25 0025
# Name: 天然卷
# -*- coding:utf-8 -*-

#用任意变成语言循环输出整数0到10
"""
for i in range(11):
    print(i)
"""

#用任意语言实现逆序输出一个字符串
"""
str_1 = "为什么追我，因为你有急支糖浆"
i = len(str_1) - 1
str_list = []
while(i >= 0):
    str_list.append(str_1[i])
    i = i - 1
print("".join(str_list))
"""
#str = "a,hello" 在字符串str中查找hello:
"""
str = "a,hello"
print(str.find("hello"))
"""

#str = "a,b,c,d"用逗号分隔str字符串，并保存到列表
"""
str = "a,b,c,d"
str1 = str.split(",")
print(str1)
"""

#将“笔试题 123A”中123替换为“进行中”
"""
str = "123A"
str1 = str.replace("123","进行中")
print(str1)
"""
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_list = num[::-2]
print(num_list)

sum = 0
for i in num_list:
    sum = sum + i
print(sum)


# num_list = [0,1,2,3,4,5,6,7,8,9]
# new_num_list = list(reversed(num_list))
# numadd = 0
# print(new_num_list)
# for num in new_num_list:
#     index = new_num_list.index(num)
#     if index % 2 == 0:
#         numadd += num
# print(numadd)



