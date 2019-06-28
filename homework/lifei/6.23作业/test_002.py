#   Date: 2019/6/24 0024
#   Name: life
#  _*_ coding:UTF-8  _*_

#将制定字符串类型进行反转
#排序一
info="欢乐逛欢迎您"
print (info[::-1])
#排序二
info1=list("欢乐逛欢迎您")
info1.reverse()
print(info1)

#循环0-10的整数
#方法一
for a in range(0,11):
    print(a)
#方法二
num=0
while num<=10:
    print(num)
    num +=1


#第一题，找hello
#方法一
str="a,hello"
if "hello" in str:
    print("存在")
else:
    print("不存在")
#方法二
print(str.find("hello"))
print(str.count("hello"))

#根据逗号分割，并添加到列表
#方法一
str1="a,b,c,d"
str1=["a,b,c,d"]
my_list=[]
my_list.extend(str1)
print(my_list)
print(type(my_list))
#方法二
str2="a,b,c,d"
b="".join(str2)
print(b)
print(type(b))
#方法三
str3=["a,b,c,d"]
d="".join(str3)
print(d)
print(type(d))
#方法四(这个应该是标准答案)
str4="a,b,c,d"
str4=["a,b,c,d"]
e=",".join(str4)
print(e)
print(type(e))

#替换题
strinfo="笔试题 123A"
strinfo2=strinfo.replace("123","进行中")
print(strinfo2)

