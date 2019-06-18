

num_A = input('请输入一个数字：')
num_B = input("请输入第二个数字：")
if num_A.isdigit() and num_B.isdigit():
    print("您输入的%s，%s两个数字的和为：%d" % (num_A, num_B, int(num_A)+int(num_B)))
else:
    print("您输入的不是数字")
