import requests


r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = r.json()
valute = data['Valute']['AMD']
print(valute)



