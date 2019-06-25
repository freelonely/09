import random

# 8个老师的名字
teacherName = ["a", "b", "c", "d", "e", "f", "g", "h"]

# 3间办公室
officeNo = [[], [], []]

# 将8名老师随机分配到三个办公室
i = 0
for name in teacherName:
    index = random.randint(0, 2)
    officeNo[index].append(name)

# 将名单按照格式列出来
i = 1
for tempName in officeNo:
    print("办公室%d的人数为:%d" %(i, len(tempName)))
    i +=1
    for name in tempName:
        print(name, end="")
    print("\n")
    print("-"*20)



