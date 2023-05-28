# import json
#
# client_info = {}
#
#
# def load():
#     global client_info
#     with open('client_info.json') as json_file:
#         client_info = json.load(json_file)
#
#
# def make_transaction():
#     global client_info
#     print("Доступные счета:")
#
#
#
#     i = 1
#     for account in client_info["accounts"]:
#         print(i, "-", account["name"], "-", account["number"])
#         i += 1
#
#     account_num = input("Введите счёт: ")
#
#     try:
#         account_num = int(account_num)
#     except:
#         print("Ошибка ввода. Прерываю транзакцию...")
#         return
#
#     for i in range(len(client_info["accounts"])):
#         if i + 1 == account_num:
#             account = client_info["accounts"][i]["number"]
#             break
#     else:
#         print("Такого счёта не существует. Прерываю транзакцию...")
#         return
#     print("Типы транзакций:")
#     print("1 - списание")
#     print("2 - зачисление")
#     transaction_type = input("Выберите тип транзакции: ")
#     if transaction_type == "1":
#         transaction_type = "списание"
#     elif transaction_type == "2":
#         transaction_type = "зачисление"
#     else:
#         print("Такого типа не существует. Прерываю транзакцию...")
#         return
#
#     print("Дата транзакции")
#     year = input("Введите год: ")
#     month = input("Введите месяц: ")
#
#     if int(year) > 2022 or int(month) > 12 or int(month) < 1:
#         print("Неверная дата. Прерываю транзакцию...")
#         return
#
#     try:
#         amount = int(input("Введите сумму: "))
#     except:
#         print("Ошибка ввода. Прерываю транзакцию...")
#         return
#     if amount < 1:
#         print("Сумма не может быть меньше 1. Прерываю транзакцию...")
#         return
#
#     new_data = {"account": account,
#                 "type": transaction_type,
#                 "date": {"year": year, "month": month},
#                 "amount": amount}
#     print(new_data)