# Date: 2019/6/23
# Name: connor
# _*_ conding:utf-8 _*_

import random
teacher = input("请输入老师名称用空格分割:")
teacherName = teacher.split(" ")
teacher_list = []
teacher_list.extend(teacherName)
# print(teacher_list)
school_list = [[], [], []]
for i in teacher_list:
    index = random.randint(0, 2)
    school_list[index].append(i)
print(school_list)
