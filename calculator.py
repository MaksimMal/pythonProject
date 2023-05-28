a = float(input('Введите 1 число: '))
b = float(input('Введите 2 число: '))
c = input('Введите арифметический знак(+, -, *. /): ')
if c == '+':
    d = a + b
    print(str(d))
elif c == '-':
    d = a - b
    print(str(d))
elif c == '*':
    d = a * b
    print(str(d))
elif c == '/':
    d = a / b
    print(str(d))
else:
    print('Вы ввели неверный арифметический знак!')