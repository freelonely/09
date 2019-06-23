# Date：2019/6/19
# Name: 任二二
# -*- coding:utf-8 -*-

import random

office = [[], [], []]

teacher = ["小明", "小红", "小军", "小强", "小小", "大大", "阿西吧", "删库跑路"]

for teacher1 in teacher:
    index = random.randint(0, 2)
    office[index].append(teacher1)

i = 1
for office1 in office:
    ber = len(office1)
    print("%d办公室有%d位老师:" % (i, ber))
    print(office1)
    i += 1





