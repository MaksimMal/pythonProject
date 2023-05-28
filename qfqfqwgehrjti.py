number = 0
x = ""
while x != "выйти":
    x = input()
    y = x.split()
    if y[0] == "добавить":
        number += int(y[1])
    elif y[0] == "убавить":
        number -= int(y[1])
    elif y[0] == "показать":
        print(number)
