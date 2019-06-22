import random


def FangFa1():
    teachers = list("ABCDEFGH")
    print(teachers)
    rooms = [[], [], []]
    for teacher in teachers:
        index = random.randint(0, 2)
        if index == 2:
            if len(rooms[index]) < 1:
                rooms[index].append(teacher)
            elif len(rooms[index-1]) < 3:
                rooms[index-1].append(teacher)
            else:
                rooms[index-2].append(teacher)
        elif index == 1:
            if len(rooms[index]) < 3:
                rooms[index].append(teacher)
            elif len(rooms[index + 1]) < 1:
                rooms[index + 1].append(teacher)
            else:
                rooms[index - 1].append(teacher)
        else:
            if len(rooms[index]) < 4:
                rooms[index].append(teacher)
            elif len(rooms[index + 1]) < 3:
                rooms[index + 1].append(teacher)
            else:
                rooms[index + 2].append(teacher)

    print(rooms)

def FangFa2():
    teachers = list("ABCDEFGH")
    print(teachers)
    rooms = [[], [], []]
    room_teacher = [4, 3, 1]
    nums_list = []
    for teacher in teachers:
        index = random.randint(0, 2)
        index_room_teacher = room_teacher[index]
        index_room = rooms[index]
        if index == 0: #第一个教室，应该有4个老师
            if len(index_room) < index_room_teacher:
                index_room.append(teacher)
            else:
                nums_list.append(teacher)
        elif index == 1: #第二个教室，应该有3个老师
            if len(index_room) < index_room_teacher:
                index_room.append(teacher)
            else:
                nums_list.append(teacher)
        elif index == 2:#第3个教室，应该只有1个老师
            if len(index_room) < index_room_teacher:
                index_room.append(teacher)
            else:
                nums_list.append(teacher)
    while len(nums_list) != 0:
        for nums in nums_list:
            index = random.randint(0, 2)
            if index == 0:
                if len(rooms[index]) < room_teacher[index]:
                    rooms[index].append(nums_list.pop())
                else:
                    continue
            if index == 1:
                if len(rooms[index]) < room_teacher[index]:
                    rooms[index].append(nums_list.pop())
                else:
                    continue
            if index == 2:
                if len(rooms[index]) < room_teacher[index]:
                    rooms[index].append(nums_list.pop())
                else:
                    continue
    print(rooms)
    print(nums_list)


def FangFa3():
    bool_1 = True
    while bool_1:
        teachers = list("ABCDEFGH")
        rooms = [[], [], []]
        room_teacher = [4, 3, 1]
        for teacher in teachers:
            index = random.randint(0, 2)
            index_room_teacher = room_teacher[index]
            index_room = rooms[index]
            if index == 0:  # 第一个教室，应该有4个老师
                if len(index_room) < index_room_teacher:
                    index_room.append(teacher)
            elif index == 1:  # 第二个教室，应该有3个老师
                if len(index_room) < index_room_teacher:
                    index_room.append(teacher)
            elif index == 2:  # 第3个教室，应该只有1个老师
                if len(index_room) < index_room_teacher:
                    index_room.append(teacher)
        if len(rooms[0]) == 4 and len(rooms[1]) == 3 and len(rooms[2]) == 1:
            bool_1 = False
            print(rooms)

FangFa1()
print("----------------------")
FangFa2()
print("----------------------")
FangFa3()
