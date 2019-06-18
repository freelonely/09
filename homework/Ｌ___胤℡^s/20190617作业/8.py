import random


while True:
    caiquan = ["石头", "剪刀", "布"]
    computer = random.randint(0, 2)
    people = input("请猜拳：石头（0），剪刀（1），布（2）:")
    if people.isdigit():
        if 0 <= int(people) <= 2:
            if int(people) == computer :
                print("你出的是%s，电脑出的是%s，平局，继续" % (caiquan[int(people)], caiquan[computer]))
            elif (int(people) == 0 and computer == 1) or (int(people) == 1 and computer == 2) or (int(people) == 2
                                                                                                  and computer == 0):
                print("你出的是%s，电脑出的是%s，你赢了！" % (caiquan[int(people)], caiquan[computer]))
                num = 0
                flag = -1
                while num != 1 or num != 2:
                    num = input("是否继续？继续请按1，不继续请按2：")
                    if num.isdigit():
                        if int(num) == 1:
                            break
                        elif int(num) == 2:
                            flag = 1
                            break
                        else:
                            print("请输入1,2数字！")
                    else:
                        print("请输入1,2数字！")
                if flag == 1:
                    break
            else:
                print("你出的是%s，电脑出的是%s，你输了，再来！" % (caiquan[int(people)], caiquan[computer]))
        else:
            print("请输入0,1,2数字！")
    else:
        print("请输入0,1,2数字！")
