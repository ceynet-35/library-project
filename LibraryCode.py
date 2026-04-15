#import
import csv # сделаем логику а потом уже добавим работу с csv файлами
from datetime import datetime




class Item:
    def __init__(self,item_id,title,amount=1):
        self.item_id=item_id
        self.title=title
        self.popularity=0
        self.amount=amount          # всего экземпляров
        self.available=amount       # доступные экземпляры

class Book(Item):
    def __init__(self, item_id, title, day_arent=14):
        super().__init__(item_id, title)
        self.day_arent = day_arent
        self.trahv_paevast=0.06

class DVD(Item):
    def __init__(self, item_id, title, day_arent=14):
        super().__init__(item_id, title)
        self.day_arent = day_arent
        self.trahv_paevast=0.06

class Tarkvara(Item):
    def __init__(self, item_id, title):
        super().__init__(item_id, title)

class Person:
    

class Library: #это как одна библеотека я немного не понимаю как понять несколько библеотек
    def __init__(self,name,items,user): 
        self.name=name
        self.items={}
        self.user={}

    def add_item(self,item):
        pass
    
    def get_items(self): # вроде так
        pass
    
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
            while True: #потом доработаем и сделаем граматно
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

