from bank import *
from client2 import *
from plot import *
from verification import *
import os
if __name__ == "__main__":
    load()
    command = ""
    j = False
    while j == False:
        p = input('Добро пожаловать!\n'
              '1 - войти\n'
              '2 - зарегестрироваться\n')
        if p == '2' or p == 'зарегестрироваться':
            signup()
            clear()
            j = True
        elif p == '1' or p =='войти':
            enterance()
            clear()
            j = True
        else:
            print('Попробуйте ещё раз')
            clear()

    while command != "10":
        os.system("cls")
        print("Доступные действия:")
        print("1 - посмотреть предложения банка")
        print("2 - отправить жалобу")
        print("3 - информация о счетах")
        print("4 - посмотреть прогноз доходов и расходов на следующий месяц")
        print("5 - добавить транзакцию")
        print("6 - посмотреть график доллара к рублю")
        print("7 - посмотреть график доллара к биткоину")
        print("8 - посмотреть график доллара к йене")
        print("10 - выйти")
        command = input("Выберите действие: ")
        if command == "1":
            suggestions()
            clear()
        elif command == "2":
            complain()
            clear()
        elif command == "3":
            show_info()
            clear()
        elif command == "4":
            predict()
            clear()
        elif command == "5":
            make_transaction()
            clear()
        elif command == "6":
            plot_rub_usd()
            clear()
        elif command == "7":
            plot_usd_btc()
            clear()
        elif command == "8":
            plot_usd_yen()
            clear()
        elif command == "10":
            print("Coхранение изменений...")
            save()
            print("До свидания.")
        else:
            print("Действие не распознано. Попробуйте ещё раз. ")