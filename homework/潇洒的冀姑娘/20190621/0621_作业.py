# Date: 2019/6/26
import random

"""
一个学校，3个办公室，8位老师，请编写下列程序：
    办公室1的人数为：4
    ABCE
    办公室2的人数为：3
    DGH
    办公室3的人数为：1
    F
"""

# 定义8位老师
teacher_list = ["红老师", "黄老师", "白老师", "绿老师", "青老师", "蓝老师", "紫老师", "黑老师"]

# 定义3个办公室的人数
office_list = [[], [], []]

for name in teacher_list:
        index = random.randint(0, 2)
        if index == 0:
            if len(office_list[index]) < 4:
                office_list[index].append(name)
        elif index == 1:
             if len(office_list[index]) < 3:
                 office_list[index].append(name)
        else:
            if len(office_list[index]) < 1:
                 office_list[index].append(name)
print(office_list)

