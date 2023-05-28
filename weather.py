from pyowm import OWM

owm = OWM('cf609aee920e4457f4e2b701b073a426')
mgr = owm.weather_manager()

x = input('Введите название города(на английском) ')
observation = mgr.weather_at_place(x)
w = observation.weather
temp = w.temperature('celsius')['temp']
if -10 <= temp <= 0:
    print('Температура в городе = ', temp)
    print('Стоит одеться потеплее')
elif 0 < temp <= 10:
    print('Температура в городе = ', temp)
    print('Одевай пальто и не переживай')
elif 10 < temp <= 15:
    print('Температура в городе = ', temp)
    print('Прохладно, но можно не одеваться слишком тепло')
elif 15 < temp <= 40:
    print('Температура в городе = ', temp)
    print('Тепло, одевайся как хочешь')
elif temp < -10:
    print('Температура в городе = ', temp)
    print('Оочень холодно, одевайся как можно теплее')
elif temp > 40:
    print('Температура в городе = ', temp)
    print('Ты где вообще? На солнце, чтоли? ')