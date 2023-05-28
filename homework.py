# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         print(f'Его зовут {self.name}!')
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#         self.get_name()
#
# class Lion(Cat):
#     def __init__(self, name):
#         Cat.__init__(self, name)
#     def play_game(self):
#         print(f"{self.name} играет с едой.")
# lev1 = Lion(input('Введите имя: '))
# lev1.play_game()
# Вот тебе код для экспериментов


# class Kettle:
#     def turn_on(self):
#         print('Чайник включился')
#         self.__boil()
#         self.__check_t()
#         self.__beep()
#         self._turn_off()
#
#     def __boil(self):
#         print('Вода греется, пузырьки мутятся')
#
#     def __check_t(self):
#         print('Проверяется температура')
#
#     def __beep(self):
#         print('Вода нагрелась, издает звук')
#
#     def _turn_off(self):
#         print('Чайник выключился')
#
#
#
# chaynik = Kettle()
# chaynik.turn_on()
# chaynik._turn_off()
# chaynik._turn_off()33


# class Transport:
#     def __init__(self, speed, color):
#         self.speed = speed
#         self.color = color
#
#
# class Airplane(Transport):
#     def __init__(self, speed, color):
#         Transport.__init__(self, speed, color)
#
#     def fly(self):
#         print(f"{self.color} самолет летит со скорость {self.speed} км/ч")
# plane = Airplane(input("vveditye skorost'"), input("vveditye tsvyet'"))
# plane.fly()

# class Inventory:
#     def __init(self, *items):
#         self.__items = list(items)
#
#     # Сортирует инвентарь по алфавиту
#     def sort_iventory(self, items):
#         self.__items = sorted(self.__items)
#
#     # Добавляет предмет в инвентарь
#     def add_item(self, item):
#         self.__items.append(item)
#         print(f"Добавил {self.__item} в инвентарь")
#
#     # Удаляет предмет из инвентаря
#     def removeItem(self, item):
#         self.__items.remove(item)
#         print(f"Вынул {self.__item} из инвентаря")
#
#     # Показывает весь инвентарь
#     def show_items(self, items):
#         print(f'В инвентаре такие предметы: ')
#         for i in range(len(self.__items)):
#             print(f"{i}. {self.__items[i]}")
# Inv1 = Inventory()

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __hellllllllllo(self):
#         if 5 <= self.age <= 20 or (len(str(self.age)) >= 2 and self.age % 10 > 4):
#             print(f"Привет! Меня зовут {self.name} и мне {self.age} лет.")
#         else:
#             print(f"Привет! Меня зовут {self.name} и мне {self.age} года.")
#
#     def __voiiiiiiiiiiiice(self):
#         pass
#
# class Dog(Animal):
#     def __voiiiiiiiiiiiice(self):
#         print('ГАААААААААААААВ!')
#
#     def _what_does_the_animal_like_to_do(self):
#         print('Я люблю играть с палкой и грызть косточку.')
#
#
# class Cat(Animal):
#     def __voiiiiiiiiiiiice(self):
#         print('МЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯУ!')
#
#     def _what_does_the_animal_like_to_do(self):
#         print('Я люблю лежать на кровати и смотреть в окно.')
#
#
# sobaka = Dog(input('Введите имя: '), int(input('Введите возраст: ')))
# sobaka.hellllllllllo()
# sobaka.voiiiiiiiiiiiice()
# sobaka.what_does_the_dog_like_to_do()
#
# koshka = Cat(input('Введите имя: '), int(input('Введите возраст: ')))
# koshka.hellllllllllo()
# koshka.voiiiiiiiiiiiice()
# koshka.what_does_the_cat_like_to_do()
#
# for i in [sobaka, koshka]:
#     i.__hellllllllllo()
#     i.__voiiiiiiiiiiiice()
#     i._what_does_the_animal_like_to_do()



# def my_first_decorator(function):
#     def wrapper():
#         f = function()
#         up = f.upper()
#         return up
#     return wrapper
#
# @my_first_decorator
# def hellooooooooooooooooooooooooooooooooooo():
#     return "Hello, world!"
# print(hellooooooooooooooooooooooooooooooooooo())

# import time
#
# def  my_second_decorator(function):
#     def wrapper(*args, **kwargs):
#         x = time.time()
#         f = function(*args, **kwargs)
#         y = time.time()
#         print('Время выполнения:', y - x)
#         return f
#     return wrapper
#
#
# @my_second_decorator
# def factorial(n):
#     cnt = 1
#
#     for i in range(1, n + 1):
#         cnt *= i
#     return cnt
# n = int(input())
# print(factorial(n))