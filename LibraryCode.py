#import
import csv # сделаем логику а потом уже добавим работу с csv файлами
from datetime import datetime #



class Item: #КЛАСС ITEM ГОТОВЫЙ ЕГО НЕ ТРОГАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def __init__(self, item_id, title, amount=1):
        self.item_id=item_id # уникальный айди объекта(книги,двд,тарквара)
        self.title=title     # название объекта
        self.popularity=0    # популярность объекта (будет увиличиваться когда предмед будут брать пример 7.5./10)
        self.amount=amount         # сколько всего экземпляров в библеотеке
        self.available=amount #чуть ниже рассписанноdw
        # тут
        # сколько доступно прямо сейчас — меняется
        # когда берут: available -= 1
        # когда возвращают: available += 1

class Book(Item):
    def __init__(self, item_id, title, amount=1, day_rent=14):
        super().__init__(item_id, title, amount) # передаём данные в Item
        self.day_arent = day_arent    # сколько дней можно держать книгу
        self.trahv_paevast=0.06       # штраф за каждый просроченный день

class DVD(Item):
    def __init__(self, item_id, title, amount=1, day_rent=7):
        super().__init__(item_id, title, amount)
        self.day_arent = day_arent   # сколько дней можно держать диск
        self.trahv_paevast=0.06      # штраф за каждый просроченный день

class Tarkvara(Item):
    def __init__(self, item_id, title): 
        super().__init__(item_id, title) # ПО — нет срока и штрафов, можно выдавать сколько угодно раз


class Person:
    def __init__(self,name,person_id): # КОНСТРУКТОР ГОТОВЫЙ ЕГО НЕ ТРОГАТЬ!!!
        self.person_id = person_id # айди человека
        self.name=name   #имя человека
        self.libraries={} # в каких библиотеках зареган
        self.rentals={}   # текуцие выдачи ()
        self.fines=0      # общий штраф
        
    # РЕГИСТРАЦИЯ ГОТОВА ЕЕ НЕ ТРОГАТЬ!!!!
    def register(self,library): # регистрируемся в библиотеке 
        # тут проверяеться зарегана ли библиотека среди других библиотек
        if library.name in self.libraries:  # library.name - название библиотеки которой хотим зарегаться.  self.libraries - список библиотек в которых зареган
            print(f"{self.name} уже зарегистрирован в  {library.name}")
            return # else не используем потому что ретурн уже останавливает метод
        self.libraries[library.name]=library # например Вася записывает библиотеку в свой список библиотек -> self.libraries = {"Центральная": lib1} КОРОТКО: прощее говоря мы кладём объект в словарь.
        library.members[self.name]=self #Библиотека записывает Васю в свой список читателей -> # library.members = {"Вася": vasya} КОРОТКО: прощее говоря мы кладём объект в словарь.
        print(f"{self.name} зарегистрирован в {library.name}")
        
     def borrow(self, library, item): # Matvei это функция выдает предмет 
         if library.name not in self.libraries: # проверям есть ли назавние библиотеки среди библиотек васи
             print(f"{self.name} не зарегистрирован в {library.name}") # если нету то получаеться вася не зареган и пишем это
             return # else не используем потому что ретурн уже останавливает метод
        library.give_item(self, item) # если зареган то просим библиотеку выдать предмет self - это вася item - что хотим взять
         
    def return_item(self, library, item):  # Egor
        pass
        
    def show_rentals(self): # Egor
        pass
        
     def show_fines(self): # Egor
        print(f"Штраф {self.name}: {self.fines:.2f} €")

class Library: #библиотека
    def __init__(self,name): #сикс севен
        self.name=name # название библиотеки
        self.items={} # словарь всех объектов в библиотеке # например # {"b1": book1, "d1": dvd1, "s1": soft1}
        self.members={} # cловарь всех читателей библиотеки # например {"Вася": vasya, "Петя": petya}
        self.all_rentals=[] # список всех выдач # список потому что могут быть повторы
        self.all_finels=[]  # список всех штрафов # список потому что могут быть повторы
        
    def add_item(self, item): #Egor
        self.items[item.item_id] = item
        print(f"Добавлен: {item.title}")
        
    def give_item(self, person, item): #Nikita #функция выдачи предметов человеку
        if item.item_id not in self.items: #проверка присутствует предмет в библиотеке или нет
            print(f"{item.title} нет в библиотеке {self.name}")
            return
        if isinstance(item,Tarkvara):   #проверка, взял ли пользователь уже этот предмет 
            if item.item_id in person.rentals:
                print(f"{person.name} уже взял {item.title}")
                return
            item.popularity += 1
            rental = {"item": item,"date_taken": datetime.now().date(), "due_date": None}
            person.rentals[item.item_id] = rental #объект выдан человеку
            self.all_rentals.append({"person": person.name, "item_id": item.item_id, "title": item.title, "date_taken": datetime.now().date(), "due_date": None}) #добавление записи о выдаче предмета(кто взял, что и когда)
            print(f"{person.name} взял ПО: {item.title}")
            return
        if item.available <=0: #проверка, есть ли экземпляры в библиотеке
            print(f"{item.title} - выданы все экземпляры")
            return
        item.available -= 1 
        item.popularity += 1 
        due_date = datetime.now().date() + timedelta(days = item.day_rent)
        rental = {"item": item, "date_taken": datetime.now().date(), "due_date": due_date}
        person.rentals[items.item_id] = rental
        self.all_rentals.append({"person": person.name, "item_id": item.item_id, "title": item.title, "date_taken": datetime.now().date(), "due_date": due_date}) #добавление записи о выдаче предмета
        print(f"{person.name} взял: {item.title}, вернуть до:  {due_date}")
        
    def take_back(self, person, item, rental): #Egor
        today = datetime.now().date()
        due_date = rental["due_date"]
        if today > due_date:
            days_late = (today - due_date).days
            fine = days_late * item.fine_per_day
            person.fines += fine
            self.all_fines.append({
                "person": person.name,
                "item_id": item.item_id,
                "title": item.title,
                "days_late": days_late,
                "fine": fine
            })
            print(f"Просрочка {days_late} дней! Штраф: {fine:.2f} €")
        else:
            print(f"{item.title} возвращён вовремя!")
        item.available += 1
        
    def show_popular(self): # Egor
         sorted_items = sorted(self.items.values(), key=lambda x: x.popularity, reverse=True)
        print(f"--- Топ популярных в {self.name} ---")
        for i, item in enumerate(sorted_items[:10]):
            print(f"  {i+1}. {item.title} | популярность: {item.popularity}")
        
    def show_all_fines(self): #Nikita
        pass








#test будем делать через функцию 
while True: #возможно поменяем меню
    print("1-Lisa raamatukogu")
    print("0-lopetab too")
    tegevus=int(input("sissesta tegevuse number nr: "))
    if tegevus==0:
        break
    else:
        if tegevus==1:
            raamatu=input("Kirjuta raamatukogu nimi: ")
            while True: #потом доработаем и сделаем грамотно
                print("!!!Raamatukogu!!!")
                print("1-Регистрируем Человека")
                print("2-Вернуть предмед")
                print("3-Выдать предмед")
                print("4-Добавить предмед в библеотеку")
                print("5-люди регистрируются как читатели")
                print("6-")
                print("7-данные")
                print("8-")
                print("9-проверяется регистрация одного человека в нескольких библиотеках")
                print("10-отображаются самые популярные объекты библиотек")
                print("11-Lisa raamatukogu")
                print("0-lopetab too")
                tegevus=int(input("sissesta tegevuse number nr: "))
                if tegevus==0:
                    break
                else:
                    if tegevus==1:
                        pass
                    elif tegevus==2:
                        while True:
                            print("1-Raamat")
                            print("2-Tarkvara")
                            print("3-DVD")
                            print("0-lopetab too")
                            tegevus=int(input("sissesta tegevuse number nr: "))
                            if tegevus==0:
                                break
                            else:
                                if tegevus==1: #выдаем книгу
                                    pass
                                elif tegevus==2: #выдаем по
                                    pass
                                elif tegevus==3: #выдаем двд
                                    pass
                    elif tegevus==3:
                        while True:
                            print("1-Raamat")
                            print("2-Tarkvara")
                            print("3-DVD")
                            print("0-lopetab too")
                            tegevus=int(input("sissesta tegevuse number nr: "))
                            if tegevus==0:
                                break
                            else:
                                if tegevus==1: #выдаем книгу
                                    pass
                                elif tegevus==2: #выдаем по
                                    pass
                                elif tegevus==3: #выдаем двд
                                    pass
                    elif tegevus==4:
                        while True:
                            print("1-Raamat")
                            print("2-Tarkvara")
                            print("3-DVD")
                            print("0-lopetab too")
                            tegevus=int(input("sissesta tegevuse number nr: "))
                            if tegevus==0:
                                break
                            else:
                                if tegevus==1: #добавление книги
                                    pass
                                elif tegevus==2: #добавление по
                                    pass
                                elif tegevus==3: #добавление двд
                                    pass
                    elif tegevus==5:
                        pass
                    elif tegevus==6:
                        pass
                    elif tegevus==7:
                        while True:
                            print("1-все книги в наличии")
                            print("2-читатели в библиотеке на данный момент")
                            print("3-показать профиль пользователей")
                            print("4-штрафы")
                            print("0-lopetab too")
                            tegevus=int(input("sissesta tegevuse number nr: "))
                            if tegevus==0:
                                break
                            else:
                                if tegevus==1: #csv файле все
                                    pass
                                elif tegevus==2: #добавление по
                                    pass
                                elif tegevus==3: #добавление двд
                                    pass
                    elif tegevus==8:
                        pass
                    else:
                        print("viga! tegevus 0..8")
