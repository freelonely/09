

# 打印媳妇儿我错了5次

# 定义一个变量
i = 0
# while循环
while i < 5:
    print("媳妇儿我错了! - 第%d次" % (i + 1))
    i += 1

print("测试")
# i = 0
# print("媳妇儿我错了! - 第%d次" % (i + 1))
#
# i += 1
# print("媳妇儿我错了! - 第%d次" % (i + 1))
#
# i += 1
# print("媳妇儿我错了! - 第%d次" % (i + 1))
#
# i += 1
# print("媳妇儿我错了! - 第%d次" % (i + 1))

# i += 1
# print("媳妇儿我错了! - 第%d次" % (i + 1))


# 计算1~100的累积和（包含1和100）

#如果一个循环没有停止的条件 我们称之为死循环
# 定义一个变量
num = 1
# 定义一个变量 记录(1~100的和)
my_sum = 0

while num <= 100:
    # print(num)
    my_sum += num
    num += 1

print("计算1~100的累积和:%d" % my_sum)


# 计算1~100之间偶数的累积和（包含1和100）

# 定义一个变量
num = 1
# 定义一个变脸保存求和
my_sum = 0

while num <= 100:
    # 判断num是否是偶数(被2整除)
    if num % 2 == 0:
        # print(num)
        my_sum += num

    num += 1

print("计算1~100之间偶数的累积和:%d" % my_sum)

"""
*
**
***
****
*****
"""

# 考虑行数
# i = 1
# while i <= 5:
#     print("*")
#     i += 1

# 考虑列数
# j = 1
# while j <= 5:
#     print("*", end="")
#     j += 1

# 整合
# 控制行数
i = 1
while i <= 5:
    # 控制列数
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    # 换行
    print()
    i += 1



# 行数
# i = 1
# while i <= 9:
#     print(i)
#     i += 1

# 列数
# j = 1
# while j <= 3:
#     print(j, end="")
#     j += 1


# 整合
i = 1
while i <= 9:
    # 列数
    j = 1
    while j <= i:
        print("%d * %d = %2d " % (j, i, (i * j)), end="")
        j += 1
    # 换行
    print()
    i += 1




# 字符串就是一个有序的字符序列

# for循环

# 特殊用法
# 定义一个字符串
# name = "itheima"
#
# for x in name:
#     print(x)

# - 0 1 2 3 4
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# 等价于for循环
# 如果使用range(x) [0,x)
# for i in range(5):
#     print(i)

# 5 6 7 8 9 10
# i = 5
# while i <= 10:
#     print(i)
#     i += 1
# range(a, b) [a, b)
# for i in range(5, 11):
#     print(i)


# 直接定义一个死循环
# while True:
#     pass


# break和continue(肯定需要和循环配合使用)

# break

# while-break
# 在一个循环中如果某个条件成立后 执行了break 那么这个循环将停止(跳出循环)
# 而且在break后面的代码将不再执行

# i = 1
# while i <= 5:
#     print(i)
#     # 如果i=2 执行下break
#     if i == 2:
#         break
#         print("哈哈")
#     i += 1
#
# print("测试")

# while-continue
# 在一个循环中如果某个条件成立后 执行了continue 那么提前结束本次勋魂
# 而且在continue后面的代码将不再执行
# i = 1
# while i <= 5:
#     i += 1
#     # 如果i=2 执行下continue
#     if i == 3:
#         continue
#         print("哈哈")
#     print(i)
#
#
# print("测试")


# for-break
# 结论和while-break 一样的
# for i in range(5):
#     print(i)
#     if i == 2:
#         break


# for-continue
# 结论和while-break 一样的
for i in range(5):

    if i == 2:
        continue
    print(i)
