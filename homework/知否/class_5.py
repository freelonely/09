# Date：2019/6/23
# Name: TONGQIANG
# -*- coding:utf-8 -*-

import random

'''
一个学校，有3个办公室，现在有8位老师等待工位的分配，
请编写程序，完成随机的分配
'''
# 有八位老师
teacher_list = ["A", "B", "C", "D", "E", "F", "G", "H"]

# 有三个教室
school_list = [[], [], []]

for Name in teacher_list:
    # 随机产生0,1,2三个办公室的索引
    index = random.randint(0,2)
    # 把元素往随机产生的办公室下表中添加
    school_list[index].append(Name)
i = 1
# 循环取出每个办公室包含的老师人数
for Fnamme in school_list:
    print("办公室%i的人数:%s人" % (i, len(Fnamme)))
    print("该办公室的老师姓名:")
    i += 1
    # 循环取出列表中包含的老师姓名
    for Names in Fnamme:
        print(Names, "老师 ", end="")
    print("\n")
    print("-"*50)

print(school_list)