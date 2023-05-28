import json
def make_transaction():
    global client_info
    print("Доступные счета:")
    i = 1
    for account in client_info["accounts"]:
        print(i, "-", account["name"], "-", account["number"])
        i += 1

    account_num = input("Введите счёт: ")

    try:
        account_num = int(account_num)
    except:
        print("Ошибка ввода. Прерываю транзакцию...")
        return

    for i in range(len(client_info["accounts"])):
        if i + 1 == account_num:
            account = client_info["accounts"][i]["number"]
            break
    else:
        print("Такого счёта не существует. Прерываю транзакцию...")
        return

    print("Типы транзакций:")
    print("1 - списание")
    print("2 - зачисление")
    transaction_type = input("Выберите тип транзакции: ")
    if transaction_type == "1":
        transaction_type = "списание"
    elif transaction_type == "2":
        transaction_type = "зачисление"
    else:
        print("Такого типа не существует. Прерываю транзакцию...")
        return

    print("Дата транзакции")
    year = input("Введите год: ")
    month = input("Введите месяц: ")

    if int(year) > 2022 or int(month) > 12 or int(month) < 1:
        print("Неверная дата. Прерываю транзакцию...")
        return

    try:
        amount = int(input("Введите сумму: "))
    except:
        print("Ошибка ввода. Прерываю транзакцию...")
        return
    if amount < 1:
        print("Сумма не может быть меньше 1. Прерываю транзакцию...")
        return

    new_data = {"account": account,
                "type": transaction_type,
                "date": {"year": year, "month": month},
                "amount": amount}

    if transaction_type == "1":
        client_info["accounts"][account_num - 1]["balance"] -= amount
    elif transaction_type == "2":
        client_info["accounts"][account_num - 1]["balance"] += amount

    client_info["transactions"].append({"account": account,
                                        "type": transaction_type,
                                        "date": {"year": year, "month": month},
                                        "amount": amount})

    print(client_info['transactions'][-1])
    print("Транзакция записана. Текущий баланс на счёте:", client_info["accounts"][account_num - 1]["balance"])

client_info = {}

def load():
  global client_info
  with open('client_info.json') as json_file:
    client_info = json.load(json_file)

def show_info():
    print("Информация о счетах")
    print("----------------------------------")
    for account in client_info['accounts']:
      print('Имя:', account['name'])
      print('Платёжная система:', account['system'])
      print('Номер:', account['number'])
      print('Тип:', account['type'])
      print('Баланс:', account['balance'])
      print('Срок действия:', account["validity period"])
      print("----------------------------------")
def save():
  global client_info
  with open('client_info.json', 'w') as json_file2:
    json.dump(client_info, json_file2)


def predict():
    global client_info
    cnt1 = 0
    cnt2 = 0
    cntm = 0
    months = []
    for transaction in client_info['transactions']:
        if transaction['date'] not in months:
            months.append(transaction['date'])
        if transaction['type'] == 'зачисление':
            cnt1 += int(transaction['amount'])
        if transaction['type'] == 'списание':
            cnt2 += int(transaction['amount'])
    for month in months:
        cntm += 1
    spisaniya = cnt2 / cntm
    pribyil = cnt1 / cntm
    print('Предполагаемые расходы в следующем месяце:', spisaniya)
    print('Предполагаемые доходы в следующем месяце:', pribyil)

