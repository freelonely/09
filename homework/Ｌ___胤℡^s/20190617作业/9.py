

i = 1

while i <= 5:
    j = 1
    while j <= i:
        print("* ", end="")
        j += 1
    print()
    i += 1
# i执行完上面时值为：6
while i > 2:
    j = 2
    while j < i-1:
        print("* ", end="")
        j += 1
    print("*")
    i -= 1
