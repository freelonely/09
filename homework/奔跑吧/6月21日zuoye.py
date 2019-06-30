
# 导入一个随机变量函数
import random
# 有八名老师
teacher_list = list("ABCEDGHF")
# 有三个办公室
school_list  = [ [],[],[] ]
# 从老师列表中取老师名字
for name in teacher_list:
    # 随机取三个
    index = random.randint(0,2)
    # 从办公室里添加老师名字
    school_list[index].append(name)
# 办公室人数从办公室里边取，老师也是从办公室里边取
print("办公室的人数为{}".format(len(school_list[0])))
print("老师是：{}".format(school_list[0]))
print("---------------")
print("办公室的人数为{}".format(len(school_list[1])))
print("老师是：{}".format(school_list[1]))
print("--------------")
print("办公室的人数为{}".format(len(school_list[2])))
print("老师是：{}".format(school_list[2]))
print("--------------")