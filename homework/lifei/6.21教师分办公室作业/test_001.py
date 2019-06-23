#   Date: 2019/6/20 0020
#   Name: life
#  _*_ coding:UTF-8  _*_

#最大星星
# bigstar=5
#
# row_chu=1
#
# while row_chu<=bigstar*2:
#     line=1
#     if row_chu<=bigstar:
#         while line<=row_chu:
#             print("*",end="")
#             line +=1
#     else:
#         while line<=(bigstar*2 - row_chu):
#             print("*", end="")
#             line += 1
#     print( )
#     row_chu +=1

teacher=list("ABCDEFGH")
office=[[],[],[]]
for name in teacher:
    if name in("ABCE"):
        office[0].append(name)
    elif name in ("DGH"):
        office[1].append(name)
    else:
        office[2].append(name)
num=0
#办公室号
officenum=1
while num<=2:
    print("办公室%d的人数为：%d" % (officenum, len(office[num])))
    for a in office[num]:
        print(a,end="")
    officenum +=1
    print( )
    print("- -"*20)
    num +=1