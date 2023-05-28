import json
import os
import time
import random

verification = {}

clear = lambda: os.system("cls")
def loading():
    global verification
    with open('verification.json') as json_file:
        verification = json.load(json_file)
def vsave():
  global client_info
  with open('verification.json', 'w') as json_file:
    json.dump(verification, json_file)


def zagruzka():
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
  return a


def enterance():
    flag = False
    while flag == False:
        a = input('Vveditye login: ')
        b = input("Vveditye Parol': ")
        if a in verification and b == verification[a]:
            print("Vyi proshlyi avtorizaciyu.")
            flag = True
            zagruzka()
        else:
            print("Vyi ne proshlyi avtorizaciyu.")
            time.sleep(3)
            clear()


def signup():
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
                    vsave()
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
                while flag3 == True:
                    b = input("Vveditye parol', kotoriy vam vyidal computer: ")
                    c = input("Podtverditye parol': ")
                    if b == c == n:
                        verification[a] = b
                        vsave()
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
loading()