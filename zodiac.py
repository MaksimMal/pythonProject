a = int(input('Введите месяц (число): '))
b = int(input('Введите день (число): '))
if a == 1 and 20 <= b <= 31 or a == 2 and 1 <= b <= 19:
    print('Ваш знак зодиака - Водолей')
elif a == 2 and 20 <= b <= 29 or a == 3 and 1 <= b <= 20:
    print('Ваш знак зодиака - Рыбы')
elif a == 3 and 21 <= b <= 31 or a == 4 and 1 <= b <= 19:
    print('Ваш знак зодиака - Овен')
elif a == 4 and 20 <= b <= 30 or a == 5 and 1 <= b <= 20:
    print('Ваш знак зодиака - Телец')
elif a == 5 and 21 <= b <= 31 or a == 6 and 1 <= b <= 20:
    print('Ваш знак зодиака - Близнецы')
elif a == 6 and 21 <= b <= 30 or a == 7 and 1 <= b <= 22:
    print('Ваш знак зодиака - Рак')
elif a == 7 and 23 <= b <= 31 or a == 8 and 1 <= b <= 22:
    print('Ваш знак зодиака - Лев')
elif a == 8 and 23 <= b <= 31 or a == 9 and 1 <= b <= 22:
    print('Ваш знак зодиака - Дева')
elif a == 9 and 23 <= b <= 30 or a == 10 and 1 <= b <= 23:
    print('Ваш знак зодиака - Весы')
elif a == 10 and 24 <= b <= 31 or a == 11 and 1 <= b <= 22:
    print('Ваш знак зодиака - Скорпион')
elif a == 11 and 23 <= b <= 30 or a == 12 and 1 <= b <= 21:
    print('Ваш знак зодиака - Стрелец')
elif a == 12 and 22 <= b <= 31 or a == 1 and 1 <= b <= 19:
    print('Ваш знак зодиака - Козерог')
else:
    print('Вы ввели неверную дату')
