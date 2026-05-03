#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Импорты
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import csv # сделаем логику а потом уже добавим работу с csv файлами
from datetime import datetime # это для работы с временим
import os

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Предметы
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Item:  # базовый шаблон для всех объектов библиотеки  #КЛАСС ITEM ГОТОВЫЙ ЕГО НЕ ТРОГАТЬ!!!
    def __init__(self, item_id, title, amount=1):
        self.item_id=item_id # уникальный айди объекта(книги,двд,тарквара)
        self.title=title     # название объекта
        self.popularity=0    # популярность объекта (будет увиличиваться когда предмед будут брать пример 7.5./10)
        self.amount=amount         # сколько всего экземпляров в библеотеке
        self.available=amount #чуть ниже рассписанно
        # тут рассписанно
        # сколько доступно прямо сейчас — меняется
        # когда берут: available -= 1
        # когда возвращают: available += 1

class Book(Item): # книга наследует от Item
    def __init__(self, item_id, title, amount=1, day_rent=14):
        super().__init__(item_id, title, amount) # передаём данные в Item
        self.day_rent = day_rent    # сколько дней можно держать книгу
        self.fine_per_day=0.06      # штраф за каждый просроченный день

class DVD(Item): # двд то же самое что книга только срок 7 дней
    def __init__(self, item_id, title, amount=1, day_rent=7):
        super().__init__(item_id, title, amount)
        self.day_rent = day_rent   # сколько дней можно держать диск
        self.fine_per_day=0.06      # штраф за каждый просроченный день

class Tarkvara(Item): # ПО — нет срока и штрафов, можно выдавать сколько угодно раз
    def __init__(self, item_id, title): 
        super().__init__(item_id, title)
        
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Класс человека
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Person:
    def __init__(self, name): # КОНСТРУКТОР ГОТОВЫЙ ЕГО НЕ ТРОГАТЬ!!!
        self.name=name    # имя человека
        self.libraries={} # в каких библиотеках зареган
        self.rentals={}   # текуцие выдачи (#пример {"b1": {"item": book1, ...}})
        self.fines=0      # общий штраф
        
    def register(self,library): # регистрируемся в библиотеке 
        # тут проверяеться зарегана ли библиотека среди других библиотек
        if library.name in self.libraries:  # library.name - название библиотеки которой хотим зарегаться.  self.libraries - список библиотек в которых зареган
            print(f"{self.name} уже зарегистрирован в  {library.name}")
            return # else не используем потому что ретурн уже останавливает метод
        self.libraries[library.name]=library # например Вася записывает библиотеку в свой список библиотек -> self.libraries = {"Центральная": lib1} КОРОТКО: прощее говоря мы кладём объект в словарь.
        library.members[self.name]=self #Библиотека записывает Васю в свой список читателей -> # library.members = {"Вася": vasya} КОРОТКО: прощее говоря мы кладём объект в словарь.
        print(f"{self.name} зарегистрирован в {library.name}")
        
     def borrow(self, library, item): # это функция выдает предмет человеку
         if library.name not in self.libraries: # проверям есть ли назавние библиотеки среди библиотек васи
             print(f"{self.name} не зарегистрирован в {library.name}") # если нету то получаеться вася не зареган и пишем это
             return # else не используем потому что ретурн уже останавливает метод
        library.give_item(self, item) # если зареган то просим библиотеку выдать предмет self - это вася item - что хотим взять
         
    def return_item(self, library, item):  # возвращаем объект в библиотеку
        if isinstance(item, Tarkvara): # у ПО другая логика
            print(f"ПО возвращать не нужно!")
            return
        if item.item_id not in self.rentals: # проверям есть ли вообще предмет у человека
            print(f"{self.name} не брал {item.title}")
            return
        rental = self.rentals[item.item_id] 
        library.take_back(self, item, rental)
        del self.rentals[item.item_id] # удаляем из словаря васи
        
    def show_rentals(self):
        if len(self.rentals) == 0:
            print(f"У {self.name} ничего нет на руках")
            return
        print(f"Объекты у {self.name}")
        for item_id, rental in self.rentals.items():
            item = rental["item"] # достаём объект книги из словаря rental и rental находится в Library в def give_item
            print(f"  {item.title} | взял: {rental['date_taken']} | вернуть до: {rental['due_date']}")
        
     def show_fines(self): # показываем штраф человека
        print(f"Штраф {self.name}: {self.fines:.2f} €")

         
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#библиотека
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Library: 
    def __init__(self,name): 
        self.name=name # название библиотеки
        self.items={} # словарь всех объектов в библиотеке # например # {"b1": book1, "d1": dvd1, "s1": soft1}
        self.members={} # cловарь всех читателей библиотеки # например {"Вася": vasya, "Петя": petya}
        self.all_rentals=[] # список всех выдач # список потому что могут быть повторы
        self.all_fines=[]  # список всех штрафов # список потому что могут быть повторы
        
    def add_item(self, item): # добавляем объект в библиотеку
        self.items[item.item_id] = item
        print(f"Добавлен: {item.title}")
        
    def give_item(self, person, item): # функция выдачи предметов человеку
        if item.item_id not in self.items: #проверка присутствует предмет в библиотеке или нет
            print(f"{item.title} нет в библиотеке {self.name}")
            return
        if isinstance(item,Tarkvara):   #проверка, взял ли пользователь уже этот предмет 
            if item.item_id in person.rentals:
                print(f"{person.name} уже взял {item.title}")
                return
            item.popularity += 1
            rental = {"item": item, "date_taken": datetime.now().date(), "due_date": None}
            person.rentals[item.item_id] = rental #объект выдан человеку
            self.all_rentals.append({"person": person.name, "item_id": item.item_id, "title": item.title, "date_taken": datetime.now().date(), "due_date": None}) #добавление записи о выдаче предмета(кто взял, что и когда)
            print(f"{person.name} взял ПО: {item.title}")
            return
        if item.available <=0: #проверка, есть ли экземпляры в библиотеке
            print(f"{item.title} - выданы все экземпляры")
            return
        item.available -= 1   # уменьшаем доступных на 1
        item.popularity += 1  # увеличиваем популярность
        due_date = datetime.now().date() + timedelta(days = item.day_rent) # считаем дату возврата сегодня + дни аренды
        rental = {"item": item, "date_taken": datetime.now().date(), "due_date": due_date}
        person.rentals[items.item_id] = rental # кладём rental в словарь человека
        self.all_rentals.append({"person": person.name, "item_id": item.item_id, "title": item.title, "date_taken": datetime.now().date(), "due_date": due_date}) #добавление записи о выдаче предмета
        print(f"{person.name} взял: {item.title}, вернуть до:  {due_date}")
        
    def take_back(self, person, item, rental): # принимаем объект обратно
        today = datetime.now().date()
        due_date = rental["due_date"]
        if today > due_date: # просрочка!
            days_late = (today - due_date).days # сколько дней просрочки
            fine = days_late * item.fine_per_day # штраф = дни * 0.06€
            person.fines += fine
            self.all_fines.append({"person": person.name, "item_id": item.item_id, "title": item.title, "days_late": days_late, "fine": fine})
            print(f"Просрочка {days_late} дней! Штраф: {fine:.2f} €")
        else:
            print(f"{item.title} возвращён вовремя!")
        item.available += 1 # возвращаем экземпляр
        
    def show_popular(self): # топ 10 популярных объектов
         sorted_items = sorted(self.items.values(), key=lambda x: x.popularity, reverse=True)
        print(f"--- Топ популярных в {self.name} ---")
        for i, item in enumerate(sorted_items[:10]):
            print(f"  {i+1}. {item.title} | популярность: {item.popularity}")
        
    def show_all_fines(self): # все штрафы библиотеки
        if len(self.all_fines) == 0:
            print("штрафов нет")
            return
        print(f"штрафы в {self.name}")
        for f in self.all_fines:
            print(f" {f['person']}, {f['title']}, {f['days_late']} дней, {f['fine']:.2f} евро")


















