#import
import csv # сделаем логику а потом уже добавим работу с csv файлами
from datetime import datetime




class Item:
    def __init__(self,item_id,title,amount=1):
        self.countt = [] #список предметов
        self.item_id=item_id # уникальный айди объекта(книги,двд,тарквара)
        self.title=title     # название объекта
        self.popularity=0    # популярность объекта (будет увиличиваться когда предмед будут брать пример 7.5./10)
        self.amount=amount         # сколько всего экземпляров в библеотеке
        self.available=amount
        # сколько доступно прямо сейчас — меняется
        # когда берут: available -= 1
        # когда возвращают: available += 1

class Book(Item):
    def __init__(self, item_id, title, day_arent=14, amount=1):
        super().__init__(item_id, title, amount)
        self.day_arent = day_arent    # сколько дней можно держать книгу
        self.trahv_paevast=0.06       # штраф за каждый просроченный день

class DVD(Item):
    def __init__(self, item_id, title, day_arent=14, amount=1):
        super().__init__(item_id, title, amount)
        self.day_arent = day_arent   # сколько дней можно держать диск
        self.trahv_paevast=0.06      # штраф за каждый просроченный день

class Tarkvara(Item):
    def __init__(self, item_id, title): 
        super().__init__(item_id, title, amount=float("inf")) # по не имеет штрафов и не возвращаеться по этому нам не нужны "self.day_arent" и "self.trahv_paevast"  # "inf" = колво бесконечно, так как по не берут, а скачивают.

class Person:
    def __init__(self,name,person_id):
        self.person_id = person_id # айди человека
        self.name=name   #имя человека
        self.libraries={} # в каких библиотеках зареган
        self.rentals={}   # текуцие выдачи ()
        self.fines=0      # общий штраф
        #дальше тут будут функции
    def register(self,library): # регистрируемся в библиотеке
        # тут проверяеться зарегана ли библиотека среди других библиотек
        if library.name in self.libraries:  # library.name - название библиотеки которой хотим зарегаться.  self.libraries - список библиотек в которых зареган
            print(f"{self.name} уже зарегистрирован в  {library.name}")
            return # else не используем потому что ретурн уже останавливает метод
        self.libraries[library.name]=library # например Вася записывает библиотеку в свой список библиотек -> self.libraries = {"Центральная": lib1} КОРОТКО: прощее говоря мы кладём объект в словарь.
        library.members[self.name]=self #Библиотека записывает Васю в свой список читателей -> # library.members = {"Вася": vasya} КОРОТКО: прощее говоря мы кладём объект в словарь.
        print("зарегистрирован")
        
    def take_item(self, library, item_id):

        if library.name not in self.libraries:    # если предмет не зарегестрирован, то не получится взять предмет (по идеи)
            print("Не зарегестрирован")
            return

        if item_id not in library.items:    # если обьекта нет в списке, то выводится следующее:
            print("такого обьекта нет")
            return
        

        if isinstance(item, Tarkvara) and item_id in self.rentals:   # если по и его айди уже есть в приобретениях, то повторного получить его уже не получится у будет выведено следующее:
            print("ПО уже взято!")
            return
        
        if not isinstance(item, Tarkvara) and item.available <= 0:   #  если предмет больше не доступен в библиотеке, то выдаёт следующее:
            print("Все экземпляры выданы")
            return
        
       
        
        if not isinstance(item, Tarkvara):  # если это НЕ программное обеспечение
            item.available -= 1  # уменьшаем количество доступных экземпляров
            due_date = datetime.now() + timedelta(days=item.day_arent)
            item.popularity += 1  # увеличиваем популярность предмета на 1# считаем дату возврата
        else:  # если это ПО
            due_date = None
            item.popularity += 1  # увеличиваем популярность предмета на 1# у ПО нет срока возврата
        
        self.rentals[item_id] = (item, due_date)  # сохраняем, что пользователь взял предмет
        library.rentals.append((self, item))  # добавляем запись о выдаче в библиотеку
        
        print(f"{self.name} взял {item.title}")  # выводим сообщение о взятии
        
        
        # ВОЗВРАТ
        def return_item(self, library, item_id):  # функция возврата предмета
        
            if item_id not in self.rentals:  # если пользователь не брал этот предмет
                print("Ты не брал это")  # сообщение об ошибке
                return  # выходим из функции
        
            item, due_date = self.rentals[item_id]  # получаем предмет и дату возврата
        
            if isinstance(item, Tarkvara):  # если это ПО
                print("ПО возвращать не нужно")  # сообщаем, что возврат не нужен
                return  # выходим
        
            today = datetime.now()  # получаем текущую дату
        
            if today > due_date:  # если просрочили
                days = (today - due_date).days  # считаем количество дней просрочки
                fine = days * item.trahv_paevast  # считаем штраф
                self.fines += fine  # добавляем штраф пользователю
                library.fines.append(fine)  # записываем штраф в библиотеку
                print(f"Штраф: {fine:.2f} €")  # выводим штраф
        
            item.available += 1  # увеличиваем количество доступных экземпляров
            del self.rentals[item_id]  # удаляем предмет из списка взятых
        
            print(f"{self.name} вернул {item.title}")  # сообщение о возврате

class Library: #библиотека
    def __init__(self,name):
        self.name=name
        self.items={}
        self.user={}

    def add_item(self,item): #добавляет предмет в библиотеку
        self.items[item.item_id] = item
    
    def get_items(self,item): # передать пользователю предмет
        self.rentals[item.item_id] = item
    
    def add_person(self,person): #добавляет пользователя в библиотеку
        self.user[person.person_id] = person 

    def return_item(self,item): #пользователь возвращает  предмет в библиотеку
        if item.id not in person.rentals:
            print("you dont  have this item")
        else:
            item = self.items[item_id]    
        
    
#test
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
