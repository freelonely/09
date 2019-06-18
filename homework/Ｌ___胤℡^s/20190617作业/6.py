name = input("请输入您的姓名：")
qq = input("请输入您的QQ：")
if qq.isdigit():
    phone = input("请输入您的手机号：")
    if phone.isdigit() and len(phone) == 11:
        address = input("请输入您的公司地址：")
        print("==================================")
        print("姓名：" + name)
        print("QQ：" + qq)
        print("手机号：" + phone)
        print("公司地址：" + address)
        print("==================================")
    else:
        print("您输入的手机号不符合规则！")
else:
    print("你的QQ输入的不符合规则！")

