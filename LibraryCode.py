#import
import csv

class Library: #это как одна библеотека я немного не понимаю как понять несколько библеотек
    def __init__(self,name,items,readers): 
        self.name=name
        self.items=items
        self.readers=readers

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
    
    @property #по сути это надо так же написать над функциями товара, но я неуверен
    def user(self):
        pass
    
    def popularity(self):
        pass
    
class LibraryItem:
    def __init__(self, title):
        self.title = title

class book:
    def __init__(self, amount, amountA, amountB, amountC):  # не уверен ,что эт так работает, но вообщем идея amountA/B/C в том, что всего есть 3 разных книг и у каждой своё колво, тоесть у первой книги колвоА, у второй колвоВ, типо такое
        self.amount = amount
        self.amountA = a
        self.amountB = b
        self.amountC = c
    
    def harrypotter(self):
        return self.amountA

    def chototam(self):
        return self.amountB

    def bebebe(self):
        return self.amountC         # не уверен .насчёт этого всего, сори, если написал хуйни хывхывхыв  :>

class magazine:
    def __init__(self, amount):
        self.amount = amount
        
class newspaper:
    def __init__(self, amount):
        self.amount = amount

class loan:
    def loan(self, )

#test
while True:
    print("!!!Raamatukogu!!!")
    print("1-Lisa raamatukogu")
    print("2-Lisa lugeja")
    print("3-Registreeri lugeja raamatukogus")
    print("4-Lisa objekt raamatukokku")
    print("5-Laena objekt")
    print("6-Tagasta objekt")
    print("7- Näita kõiki objekte")
    print("8-Näita 10 populaarsemat objekti")
    print("0-lopetab too")
    tegevus=int(input("sissesta tegevuse number nr: "))
    if tegevus==0:
        break
    else:
        if tegevus==1:
            pass # create library  
        elif tegevus==2:
            pass # add reader
        elif tegevus==3:
            pass #register reader in library
        elif tegevus==4:
            pass # add item
        elif tegevus==5:
            pass #borrow item
        elif tegevus==6:
            pass #return item
        elif tegevus==7:
            pass #show items
        elif tegevus==8:
            pass #top 10 popular
        else:
            print("viga! tegevus 0..8")



libr1 = book(12,5,7)
