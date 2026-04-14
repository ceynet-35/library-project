#import
import csv

class Item:
    def __init__(self,item_id,title):
        self.item_id=item_id
        self.title=title
        self.popularity=0


class Library: #это как одна библеотека я немного не понимаю как понять несколько библеотек
    def __init__(self,name,items,user): 
        self.name=name
        self.items={}
        self.user={}

    def add_item(self,item):
        pass

    def __str__(self):
        pass
    
    def get_items(self): # вроде так
        pass
    
    def book(self):
        pass
    
    def magazine(self):
        pass
    
    def newspaper(self):
        pass
    
    def registation(self):
        pass

    
class LibraryItem(Library):
    def __init__(self, title):
        self.title = title

class Book(Library):
    def __init__(self, amount, amountA, amountB, amountC):  # не уверен ,что эт так работает, но вообщем идея amountA/B/C в том, что всего есть 3 разных книг и у каждой своё колво, тоесть у первой книги колвоА, у второй колвоВ, типо такое
        self.amount = amount
        self.amountA = a
        self.amountB = b
        self.amountC = c
    
    def harrypotter(self):
        return f"book: {self.amountA}"

    def chototam(self):
        return f"book: {self.amountB}"

    def bebebe(self):
        return f"book: {self.amountC}"         # не уверен .насчёт этого всего, сори, если написал хуйни хывхывхыв  :>

class magazine:
    def __init__(self, amount):
        self.amount = amount
        
class newspaper:
    def __init__(self, amount):
        self.amount = amount

class loan:
    def loan(self, )

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
            while True: 
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

