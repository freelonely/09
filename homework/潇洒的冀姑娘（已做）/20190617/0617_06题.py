# Date: 2019/6/24

"""
==================================
姓名: xxxxx
QQ:xxxxxxx
手机号:131xxxxxx
公司地址:北京市xxxx
==================================

"""
# 编写程序，通过input()获取一个人的信息，然后按照下面格式显示编写程序，通过input()获取一个人的信息，然后按照下面格式显示

name = input("请输入姓名：")
qq = input("请输入QQ号：")
tel = int(input("请输入手机号："))
address = input("请输入地址：")

print("=" * 30)
print("姓名：%s"% name)
print("QQ: %s" % qq)
print("手机号：%d" % tel)
print("公司地址：%s" % address)
print("=" * 30)