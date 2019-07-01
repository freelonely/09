# Date: 2019/6/24

num_A = input("请输入第一个数字：")
num_B = input("请输入第二个数字: ")

if num_A.isdigit() and num_B.isdigit():
    numA = eval(num_A)
    numB = eval(num_B)
    print("%d + %d = %d " % (numA, numB, numA + numB))
else:
    print("您输入的不是数字，请重新输入")

