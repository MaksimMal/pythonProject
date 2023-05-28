# a = float(input('Введите первое число: '))
# b = float(input('Введите второе число: '))
# if a > b:
#     print('Наиболшее число = ', a)
# elif b > a:
#     print('Наиболшее число = ', b)
# else:
#     print('Оба этих числа равны ', a)


# a = float(input('Введите первое число: '))
# b = float(input('Введите второе число: '))
# c = float(input('Введите третье число: '))
# cnt = 0
# if a < 0:
#     cnt += 1
# if b < 0:
#     cnt += 1
# if c < 0:
#     cnt += 1
# print(cnt)


# a = float(input('Введите число: '))
# if a % 2 == 0:
#     print('Число чётное, поэтому выводим 1')
# else:
#     print('Число чётное, поэтому выводим 0')


# a = 100
# b = 100
# if int(a) == str(b):
#     print(1)
# else:
#     print(0)

# a = input('Введите пин-код ')
# if len(a) == 4 and str(0000) <= a <= str(9999):
#     print(1)
# else:
#     print(0)


# a = 10
# b = 10.0
# if a == b:
#     print(1)
# elif int(a) == int(b):
#     print(2)
# else:
#     print(3)


# a = 5
# b = 5
# c = 3
# if not a > b > c:
#     if a > b:
#         print(1)
#     else:
#         print(2)
# else:
#     if a > b:
#         print(3)

# a = input()
# if len(a) == 4 and a.isdigit():
#     print(1)
# else:
#     print(0)


# a = 'Hello world!'
# b = '1234'
# c = '12ab'
# print(a.isdigit())
# print(b.isdigit())
# print(c.isdigit())


# a = 'Hello world!'
# b = a[::-3]
# print(b)

# Дано целое трёхзначное число aa. Выведи количество чётных цифр в данном числе.
# a = int(input())
# cnt = 0
# if (a // 1) % 2 == 0:
#     cnt += 1
# if (a // 10) % 2 == 0:
#     cnt += 1
# if (a // 100) % 2 == 0:
#     cnt += 1
# print(cnt)

# Даны 44 числа aa, bb, cc и dd. Одно из них отлично от оставшихся, равных друг другу. Необходимо вывести данное число.
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a == b and a == c:
#     print(d)
# elif b == c and b == d:
#     print(a)
# elif c == a and c == d:
#     print(b)
# elif a == b and b == d:
#     print(c)


# Даны две различные клетки шахматного поля, каждая из которых задаётся двумя числами, — координата по xx, координата по yy. Выведи 11, если шахматный король сможет перейти с первой клетки на вторую одним ходом, иначе выведи 00.
# x1 = int(input('x1 = '))
# y1 = int(input('y1 = '))
# x2 = int(input('x2 = '))
# y2 = int(input('y2 = '))
#
# if (x1 < 0 or x1 > 8) or (x2 < 0 or x2 > 8) or (y1 < 0 or y1 > 8) or (y2 < 0 or y2 > 8):
#     print(0)
# elif (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
#     print(1)
# elif (x1 - 1 == x2 or x1 + 1 == x2) and y1 == y2:
#     print(1)
# elif (y1 - 1 == y2 or y1 + 1 == y2) and x1 == x2:
#     print(1)
# else:
#     print(0)


# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and c + b > a:
#     print('yes')
# else:
#     print('no')


# Дано 4-ех значное целое число num. Возведи каждую цифру этого числа в квадрат и соедини результаты в одно число.
# num = int(input())
# a = num // 1000
# b = num // 100 % 10
# c = num // 10 % 100 % 10
# d = num // 1 % 1000 % 100 % 10
# a = a ** 2
# b = b ** 2
# c = c ** 2
# d = d ** 2
# print(str(a) + str(b) + str(c) + str(d))

# dodelat'
# a = input()
# for i in range(len(a)):
#     if a[i].islower():
#         for e in range(len(a)):
#             if a[e].isupper():
#                 print(1)
# else:
#     print(0)


# for i in range(10):
#     print('hello')
#     i = i + 1
#

# a = int(input('vvedite pervoye chislo: '))
# b = int(input('vvedite vtoroye chislo: '))
# for i in range(a, b + 1):
#     print(i, end = ' ')


# n = int(input('vvedite chislo: '))
# cnt = 0
# for i in range(1, n + 1, 2):
#     cnt += i ** i
# for i in range(2, n + 1, 2):
#     cnt -= i ** i
# print('itog: ', cnt)


# n = int(input('vvedite chislo: '))
# cnt = 0
# for i in range(1, n + 1):
#     cnt += (i-1) * i
# print('itog: ', cnt)


# a = int(input())
# b = int(input())
# while a <= b:
#     print(a)
#     a += 1

# a = 0
# n = int(input())
# i = 0
# while a <= n - 1:
#     i += a + 1
#     a += 1
# print(i)


# a = int(input())
# b = int(input())
# while a >= b:
#     a -= b
# print(a)


# a = int(input())
# b = int(input())
# cnt = 0
# while a >= b:
#     a -= b
#     cnt += 1
# print(cnt)
# print(a)


# a = int(input())
# cnt = 0
# x = 1
# for i in range(1, a + 1):
#     x = i * x
#     if i % 2 == 0:
#         cnt -= x
#     elif i % 2 == 1:
#         cnt += x
# print(cnt)


# n = int(input())
# while n != 0:
#     x = n % 10
#     print(x, end = '')
#     n //= 10


# n = int(input('vvedite chislo: '))
# cnt = 0
# for i in range(1, n + 1):
#     cnt += (i-1) * i
# print('itog: ', cnt)


# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n
#
#
# x = int(input())
# n = int(input())
# res = 1
#
# for i in range(0, n + 1):
#     res += (x ** i) / factorial(i)
#     i += 1
# print(res)


# phib1 = 1
# phib2 = 1
# n = int(input())
# x = n
# i = 0
# print(phib1)
# print(phib2)
# while x > phib2 - 1:
#     summa = phib1 + phib2
#     phib1 = phib2
#     phib2 = summa
#     i = i + 1
#     print(phib2)

# Дано натуральное число NN. Используя операции //// и \%%, следует перевернуть данное число.
# n1 = int(input())
# while n1 != 0:
#     x = n1 % 10
#     n1 = n1 // 10
#     print(x, end = '')

# Даны целые положительные числа A и B. Найди сумму:
# 1^B + 2^B + ... + A^B
# a = int(input())
# b = int(input())
# res = 0
# for i in range(1, a + 1):
#     res += i ** b
#     i += 1
# print(res)

# a = [input(), input(), input()]
# print(a[0], a[-1])

# x = int(input())
# a = []
# for i in range(1, 2 * x + 1, 2):
#     a.append(i)
# print(a)


# a = [int(input()), int(input()), int(input()), int(input())]
# print((a[0] + a[1] + a[2] + a[3]) / 4)


# n = int(input())
# x = [int(input('vvedite chislo: '))] * n
# print(max(x))


# maximum = -9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# x = []
# n = int(input())
# for a in range(n):
#     x.append(int(input()))
# for y in x:
#     if y > maximum:
#         maximum = y
# print(maximum)


# min = 999999999999999999999
# x = []
# b = []
# n = int(input())
# for a in range(n):
#     x.append(int(input()))
# for y in x:
#     if y % 2 == 1:
#         b.append(y)
# for c in b:
#     if c < min:
#         min = c
# if min == 999999999999999999999:
#     print(0)
# else:
#     print(min)


# a = []
# c = int(input())
# for b in range(c):
#     a.append(input())
# for x in a:
#     print(x)


# deals = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
# ]
# # Напиши решение тут
# x = 1
# while x:
#     x = input()
#     if x:
#         x = int(x)
#         if (0 - len(deals)) <= x < len(deals):
#             del deals[x]
#
# print(deals)


# Пусть число, где все соседние цифры в нём отличаются на 1, называется прыгающим. Программа получает на вход целое положительное число N, если оно является прыгающим, то выведи 1, иначе 0.

# a = input()
# cnt = 0
# for x in range(len(a) - 1):
#     if int(a[x]) - int(a[x + 1]) == 1 or int(a[x]) - int(a[x + 1]) == -1:
#         cnt += 1
# if len(a) - 1 == cnt:
#     print(1)
# else:
#     print(0)


# a1 = list(input().split())
# a2 = list(input().split())
# a3 = []
# for x in a1:
#     for i in a2:
#         if x in a2 and x not in a3:
#             a3.append(x)
# print(a3)


# a = input()
# if len(a) % 2 == 1:
#     x = a[int(a[0]):int(len(a)) // 2 + 1]
#     y = a[int(len(a)) // 2 + 2:]
#     if sum(x) == sum(y):
#         print(1)
#     else:
#         print(0)
# else:
#     x = a[int(a[0]):int(len(a)) // 2 + 1]
#     y = a[int(len(a)) // 2 + 1:]
#     if sum(x) == sum(y):
#         print(1)
#     else:
#         print(0)


# recipe = []
# while '' not in recipe:
#     recipe.append(input())
# for x in recipe:
#     if 'лук' in x:
#         recipe.remove(x)
# recipe.pop(-1)
# # for x in recipe:
# # print(x,end = ' ')
# print(*recipe)


# prices = {
#     'milk': {
#         'price': 100,
#         'weight': 900
#     },
#     'eggs':{
#         'price': 90,
#         'amount': 10,
#         'weight': 800
#     }
# }
# for val in prices.items():
#     if val[1]['price'] < 100:
#         print(val[0])


# n = int(input())
# a = int(input())
# cnt = 0
# x = list(str(n))
# for y in x:
#     if y == '0':
#         cnt += 1
#     else:
#         cnt += 0
# if cnt == 0:
#     print('NO')
# else:
#     print('YES')


# warrior = {'здоровье': 100, 'атака': 30, 'защита': 25, 'навыки': {'щит': 10}}
# archer = {'здоровье': 50, 'атака': 40, 'защита': 20, 'навыки': {'убежать': 10}, 'инвентарь': ['стрелы', 'меч', 'еда']}
# wizard = {'здоровье': 30, 'атака': 50, 'защита': 15, 'навыки': {'магический щит': 10, 'лечение': 5}}
#
#
# def print_dict(charecter):
#     for ability in charecter:
#         print(ability, ':', charecter[ability])
#
#
#
# for item in [warrior, archer, wizard]:
#     print_dict(item)


# def sum_nums(a, b):
#     c = a + b
#     return c
#
#
# def sub_nums(a, b):
#     c = a - b
#     return c
#
#
# def multiply_nums(a, b):
#     c = a * b
#     return c
#
#
# def divide_nums(a, b):
#     c = a / b
#     return c


# print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление')
# choice = input('Введите номер действия: ')
#
# a = float(input())
# b = float(input())
#
# if choice == 1:
#     print(a + b)
# elif choice == 2:
#     print(a - b)
# elif choice == 3:
#     print(a * b)
# elif choice == 4:
#     print(a / b)


# def divide_nums(a, b):
#     c = a / b
#     return c
#
#
# a = float(input())
# b = float(input())
# print(divide_nums(a, b))
# try:
#     a / b
# except ValueError:
#     print("Функция сложения работает только с числами.")
#     print(0)

# def sum_nums(a, b):
#     c = 0
#     try:
#         c = float(a) + float(b)
#     except ValueError:
#         print('Функция сложения работает только с числами.')
#     finally:
#         return c
#
# def sub_nums(a, b):
#     c = 0
#     try:
#         c = float(a) - float(b)
#     except ValueError:
#         print('Функция вычитания работает только с числами.')
#     finally:
#         return c
#
#
# def multiply_nums(a, b):
#     c = 0
#     try:
#         c = float(a) * float(b)
#     except ValueError:
#         print('Функция умножения работает только с числами.')
#     finally:
#         return c
#
#
#
# def divide_nums(a, b):
#     c = 0
#     try:
#         c = float(a) / float(b)
#     except ValueError:
#         print('Функция деления работает только с числами.')
#     finally:
#         return c
#
# print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление')
# choice = input('Введите номер действия: ')
#
# a = input()
# b = input()
#
# if choice == '1':
#     print(sum_nums(a, b))
# elif choice == '2':
#     print(sub_nums(a, b))
# elif choice == '3':
#     print(multiply_nums(a, b))
# elif choice == '4':
#     print(divide_nums(a, b))
# else:
#     print('Такого действия нет.')


# def vstavka(n, b):
#     for i in range(1, n):
#         temp = b[i]
#         j = i-1
#         while j > -1 and b[j] > temp:
#             b[j+1] = b[j]
#             j -= 1
#         if j+1 != i:
#             b[j+1] = temp
#             print(*b)
#
#
#
#
# n = int(input())
# b = list(map(int,input().split()))
# vstavka(n,b)


# with open("Maksimkinyi_rasskazyi.txt", "a", encoding="utf-8") as f:
#     tovar = (input('napishit nazvaniye tovara: '))
#     try:
#         price = int(input("Vvelitye cenu tovara(so mnoy nelza torgovat'sya) :"))
#         f.write("\n" + tovar + ' - ' + str(price))
#     except:
#         print("Vyi reshili menya obmanyt'?Vsyo, ya obidelsya")

# from tkinter import *
# from math import sin, cos, pi
#
#
# def start_draw():
#     f = txt1.get()
#     # читаем в переменную f функцию из окна ввода, тип - строка
#     xmin = txt2.get()  # определяем область построения
#     xmax = txt3.get()  # сделайте чтение из окон
#     ymin = txt4.get()
#     ymax = txt5.get()
#     try:  # обработка исключения:
#         xmin = int(xmin)
#         xmax = int(xmax)
#         ymin = int(ymin)
#         ymax = int(ymax)
#     except ValueError:  # обработка ошибки ValueError - нельзя перевести в int
#         showerror("Error", "Input number")
#         return
#     h = int(cvs["height"])
#     w = int(cvs["width"])
#
#     # вычисляем масштаб по осям для пересчета в экранные координаты
#     mx = w / (xmax - xmin)
#     my = h / (ymax - ymin)
#
#     x0 = -xmin * mx  # центр системы координат в пикселях канвы для произвольного диапазона
#     y0 = ymax * my  # или можно задать как середина холста
#
#     # построение оси OХ
#     cvs.create_line(0, y0, w, y0, fill="brown")
#     for x in range(xmin + 1, xmax):
#         xe = x0 + x * mx
#         cvs.create_line(xe, y0 - 2, xe, y0 + 2, fill="yellow")
#         cvs.create_text(xe + 2, y0 + 10, text=str(x), font="Verdana 12", anchor="w", fill="blue")
#     # Построение оси OY
#     cvs.create_line(x0, 0, x0, h, fill="green")
#     for y in range(ymin + 1, ymax):
#         ye = y0 + y * my
#         cvs.create_line(x0 - 2, ye, x0 + 2, ye, fill="green")
#         cvs.create_text(x0 + 2, ye + 10, text=str(-y), font="Verdana 12", anchor="w", fill="pink")
#         # построение функции
#     x = xmin  # будем перебирать значения х
#     dx = 0.01  # шаг можно также брать из окна ввода
#     while x <= xmax:
#         y = eval(f)  # вычисление значения функции для
#         # прорисовка отрезка или точки...
#         xe = x0 + x * mx
#         ye = y0 - y * my
#         x += dx
#         cvs.create_oval(xe - 0.5, ye + 0.5, xe + 0.5, ye - 0.5, fill="yellow", outline="brown", width=3)
#
#
# root = Tk()
# root.title("Paint")
# root.configure(bg="#d7d7d7")
# root.geometry("1000x1000")
#
# btn1 = Button(root, text="Start", font="Ubuntu, 16", command=start_draw)
# cvs = Canvas(root, width=600, height=400)
#
# label1 = Label(root, text=" f(x) = ", width=10, height=1, font="Ubuntu, 20", bg="yellow")
# label2 = Label(root, text=" xmin = ", width=10, height=1, font="Ubuntu, 20", bg="yellow")
# label3 = Label(root, text=" xmax = ", width=10, height=1, font="Ubuntu, 20", bg="yellow")
# label4 = Label(root, text=" ymin = ", width=10, height=1, font="Ubuntu, 20", bg="yellow")
# label5 = Label(root, text=" ymax = ", width=10, height=1, font="Ubuntu, 20", bg="yellow")
#
# txt1 = Entry(root, width=10, font="Ubuntu, 20", bg="white")
# txt2 = Entry(root, width=10, font="Ubuntu, 20", bg="white")
# txt3 = Entry(root, width=10, font="Ubuntu, 20", bg="white")
# txt4 = Entry(root, width=10, font="Ubuntu, 20", bg="white")
# txt5 = Entry(root, width=10, font="Ubuntu, 20", bg="white")
#
# txt1.insert(END, "x / 2")
# txt2.insert(END, "-5")
# txt3.insert(END, "5")
# txt4.insert(END, "-5")
# txt5.insert(END, "5")
#
# btn1.grid(row=0, column=0, sticky="ew")
# label1.grid(row=0, column=1, sticky="ew")
# txt1.grid(row=0, column=2, sticky="ew")
# label2.grid(row=0, column=3, sticky="ew")
# txt2.grid(row=0, column=4, sticky="ew")
# label3.grid(row=1, column=1, sticky="ew")
# txt3.grid(row=1, column=2, sticky="ew")
# label4.grid(row=1, column=3, sticky="ew")
# txt4.grid(row=1, column=4, sticky="ew")
# label5.grid(row=1, column=5, sticky="ew")
# txt5.grid(row=1, column=6, sticky="ew")
#
# cvs.grid(row=10, columnspan=4)
#
# root.mainloop()



import matplotlib.pyplot as plt