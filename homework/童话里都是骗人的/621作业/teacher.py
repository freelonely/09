
'''八个教师，3个教室，随机分配老师所在办公室，并打印出来'''

import random

station = [[] ,[] ,[]]
teacher = list("ABCDEFGH")

for name in teacher:
    index = random.randint(0 ,2)
    station[index].append(name)

i = 0
while i< len(station):
    print("第%d个教师有%d个老师，分别是：" % (i + 1, len(station[i])))
    for item in station[i]:
        print(item, end=' ')
    print()
    i += 1
