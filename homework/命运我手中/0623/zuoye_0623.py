# Date: 2019/6/23
# Name: connor
# _*_ conding:utf-8 _*_
import random
str1 = "a,hello"
a = str1.split(",")
print(a[1])
str2 = "a,b,c,d"
b = str2.split(",")
print(b)
str3 = "笔试题12A"
c = str3.replace("12A", "进行中")
print(c)

# student = input("请输入5名学生名字，用空格隔开")
# student_name = student.split(" ")
# student_list = []
# student_list.extend(student_name)
# for name in student_list:
#     a = name[1]
#     print(a)



random_list = []
for i in range(5):
    ran = random.randint(0, 100)
    if len(random_list) <= 5:
        random_list.append(ran)
random_list.sort(reverse=True)
print(random_list)


# list1 = [1, 3, 4, 5, 7]
# # list2 = [0, 66, 8, 9]
# # list1.extend(list2)
# # list1.sort()
# # print(list1)
# #
# # dict1 = {"school": "lebo", "date": 2018, "address": "beijing"}
# # for items in dict1.items():
# #     print(items[1])
# # # print(a)
# #
# # num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # num_list = num[::-1]
# # num = 0
# # for i in num_list:
# #     if num_list[i] % 2 == 0:
# #         num += i
# # print(num)


