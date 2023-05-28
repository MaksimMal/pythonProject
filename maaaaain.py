import json
import os
import time
import random
import colorama

verification = {}

clear = lambda: os.system("cls")
red = colorama.Fore.RED
green = colorama.Fore.GREEN
blue = colorama.Fore.BLUE
magenta = colorama.Fore.MAGENTA
cl = colorama.Style.RESET_ALL


def load_verification():
    global verification
    with open('verification2.json') as json_file:
        verification = json.load(json_file)
def save_verification():
  global verification
  with open('verification2.json', 'w') as json_file:
    json.dump(verification, json_file)

def is_valid(a):
    if len(a) >= 8 and not a.isupper() and not a.islover() and not a.isalpha() and not a.isdigit():
        x = 'OK'
    else:
        x = 'Not_OK'
    return x

def zagruzochka():
    for x in range(3):
        print("Загрузка.")
        time.sleep(0.5)
        clear()
        print("Загрузка..")
        time.sleep(0.5)
        clear()
        print("Загрузка...")
        time.sleep(0.5)
        clear()


def generate_password(n = 8):
  a = ''
  for i in range(n):
    a += (random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))
  if is_valid(a) == 'OK':
      return a
  else:
      return generate_password()


def enterance_notes():
    flag = False
    while flag == False:
        a = input('Vveditye login: ')
        b = input("Vveditye Parol': ")
        if a in verification and b == verification[a] and is_valid(b) == 'OK':
            print("Vyi proshlyi avtorizaciyu.")
            flag = True
            zagruzochka()
        else:
            print("Vyi ne proshlyi avtorizaciyu.\n Dlina parol'ya ne meneye 8 simwolov\n dolzhna soderzhat' zaglavniye i strochniye bykvyi, a takzhe cifryi")
            time.sleep(3)
            clear()


def signup_notes():
    global verification
    flag = False
    while flag == False:
        a = input('Pribumayte login: ')
        flag2 = False
        while flag2 == False:
            d = input('1 - придумать пароль самому\n'
                  '2 - если вы ленивый\n')
            if d == '1':
                b = input("Pridymayte parol': ")
                c = input("Podtverditye parol': ")
                if b == c:
                    verification[a] = b
                    save_verification()
                    print('Vyi voshli v sistemy.')
                    flag = True
                    clear()
                else:
                    print('Poprobyite eshyo raz.')
                    time.sleep(2)
                    clear()
            elif d == '2':
                n = generate_password()
                print(n)
                flag3 = False
                while flag3 == False:
                    b = input("Vveditye parol', kotoriy vam vyidal computer: ")
                    c = input("Podtverditye parol': ")
                    if b == c == n:
                        verification[a] = b
                        save_verification()
                        print('Vyi voshli v sistemy.')
                        flag3 = True
                        clear()
                    else:
                        print('Poprobyite eshyo raz.')
                        time.sleep(2)
                        clear()
                        flag3 = True
                flag2 = True
            else:
                print('Poprobuite eshyo raz')
load_verification()







notes = {}


def load_notes():
    global notes
    with open('notes.json') as zam:
        notes = json.load(zam)


def save_notes():
    global notes
    with open('notes.json', 'w') as zam:
        json.dump(notes, zam)


def add_notes():
    global notes
    x = input(red + 'Введите название заметки: ' + cl)
    y = input(red + 'Введите текст: ' + cl)
    notes[x] = y
    save_notes()
    print(magenta, 'Заметка была успешно добавлена.', cl)


def del_notes():
    global notes
    print(blue, *notes, cl)
    x = input(magenta + 'Введите название заметки, которую хотели бы удалить: ' + cl)
    notes.pop(x)
    save_notes()
    print(green, 'Заметка была успешно удалена.', cl)


def show_notes():
    global notes
    for x in notes:
        print(magenta, notes[x], cl)


def find_notes():
    x = input(blue + 'Введите слово в составе заметки, которую вы хотите удалить: ' + cl)
    for y in notes:
        if x in notes[y]:
            print(green, notes[y], cl)


load_notes()
j = False
while j == False:
    p = input(magenta + 'Добро пожаловать!\n'
              '1 - войти\n'
              '2 - зарегестрироваться\n' + cl)
    if p == '2' or p == 'зарегестрироваться':
        signup_notes()
        clear()
        j = True
    elif p == '1' or p == 'войти':
        enterance_notes()
        clear()
        j = True
    else:

            print(blue, 'Попробуйте ещё раз', cl)
            clear()
print(red, 'Добро пожаловать!', cl)
print(blue, 'Доступные действия:', cl)
print(green, '1 - добавление заметки', cl)
print(green, '2 - удаление заметки', cl)
print(green, '3 - посмотреть все заметки', cl)
print(green, '4 - поиск по заметкам', cl)
print(red, '5 - выйти', cl)
command = ""
while command != "5":
    command = input(blue + 'Выберите действие: ' + cl)
    if command == '1':
        add_notes()
        clear()
    elif command == '2':
        del_notes()
        clear()
    elif command == '3':
        show_notes()
        clear()
    elif command == '4':
        find_notes()
        clear()
    elif command == '5':
        print(green, "Coхранение изменений...", cl)
        save_notes()
        print(blue, 'До свидания!', cl)
    else:
        print(red, 'Вы выбрали неверную функцию.', cl)
