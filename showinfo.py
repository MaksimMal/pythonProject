import json

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