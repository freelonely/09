# Date: 2019/6/26

# 现有字符串： str1 = '1234567890'，根据题目要求，将截取后的新字符串赋值给str2
str1 = '1234567890'

# 1.	截取字符串的第一位到第三位的字符
str2 = str1[0:3]
print(str2)

# 2.	截取字符串最后三位的字符
str2 = str1[7:10]
print(str2)

# 3.	截取字符串的全部字符
str2 = str1
print(str2)

# 4.	截取字符串的第七个字符到结尾
str2 = str1[6:]
print(str2)

# 5.	截取字符串的第一位到倒数第三位之间的字符
str2 = str1[:-2]
print(str2)

# 6.	截取字符串的第三个字符
str2 = str1[2]
print(str2)

# 7.	截取字符串的倒数第一个字符
str2 = str1[-1]
print(str2)

# 8.	截取与原字符串顺序相反的字符串
str2 = str1[::-1]
print(str2)

# 9.	截取字符串倒数第三位与倒数第一位之间的字符
str2 = str1[-3:10]
print(str2)

# 10.	截取字符串的第一位字符到最后一位字符之间的字符，每隔一个字符截取一次。
str2 = str1[0:10:2]        # str2 = str1[::2]
print(str2)