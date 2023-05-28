import os
import random

clear = lambda: os.system('cls')

print('Привет! Я загадал словоб твоя задача - угадать его по буквам.')
input('*Нажми Enter, чтобы продолжить*')
clear()
print('Поехали!')

words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True

    print(letters)
    for symb in word:

            if symb in letters:
                print(symb, end=' ')
            else:
                print('*', end=' ')
                isWin = False

    print()

    if isWin:
        print('Ну ладно, верно.')
        break

    letter = input('Введите букву: ')

    if letter not in letters:
        letters.append(letter)
        if letter not in word:
            hp -= 1
            print('Осталось попыток:', hp)
    else:
        print('Вы уже вводили данную букву')
    clear()


if hp == 0:
    print('Урааааааааааа! Ты проиграл! Наконец-то!')

