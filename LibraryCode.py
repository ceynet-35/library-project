#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Импорты
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import csv # сделаем логику а потом уже добавим работу с csv файлами
from datetime import datetime, timedelta # это для работы с временим
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
        
    def show_fines(self):# показываем штраф человека
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
        person.rentals[item.item_id] = rental # кладём rental в словарь человека
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
        
    def show_popular(self):# топ 10 популярных объектов
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
            
    def save_to_csv(self): # сохраняем все данные библиотеки в CSV файлы
        # 1. сохраняем объекты
        with open(f"{self.name}_items.csv", "w", newline="", encoding="utf-8") as f: # newline="" чтобы не было лишних пустых строк # encoding="utf-8" чтобы русские буквы работали 
            writer=csv.DictWriter(f, fieldnames=["type", "item_id", "title", "amount", "available", "popularity", "day_rent", "fine_per_day"]) # f — в какой файл пишем # fieldnames — названия колонок
            writer.writeheader() # writeheader пишет первую строку с названиями колонок
            for item in self.items.values(): # определяем тип объекта
                 if isinstance(item, Book):
                     item_type="Book"
                 elif isinstance(item, DVD):
                     item_type="DVD"
                 else:
                     item_type="Tarkvara"
                 writer.writerow({"type": item_type, "item_id": item.item_id, "title": item.title, "amount": item.amount, "available": item.available, "popularity": item.popularity, "day_rent": getattr(item, "day_rent", ""), "fine_per_day": getattr(item, "fine_per_day", "")})   # getattr объект, "поле", "если нет"  # у Book и DVD есть day_rent запишет 14 или 7  у Tarkvara нет day_rent → запишет ""  
        print(f"Объекты сохранены в {self.name}_items.csv")
        
        # 2. сохраняем историю выдач
        with open(f"{self.name}_rentals.csv", "w", newline="", encoding="utf-8") as f:
            writer=csv.DictWriter(f, fieldnames=["person", "item_id", "title", "date_taken", "due_date"])
            writer.writeheader()
            for rental in self.all_rentals:
                writer.writerow(rental)
            print(f"Выдачи сохранены в {self.name}_rentals.csv")
        
        # 3. сохраняем штрафы
        with open(f"{self.name}_fines.csv", "w", newline="", encoding="utf-8") as f:
            writer=csv.DictWriter(f, fieldnames=["person", "item_id", "title", "days_late", "fine"])
            writer.writeheader()
            for fine in self.all_fines:
                writer.writerow(fine)
        print(f"Штрафы сохранены в {self.name}_fines.csv")
        
    def load_from_csv(self): # загружаем данные из CSV файлов
        # 1. загружаем объекты
        filename = f"{self.name}_items.csv" # просто сохраняем название файла в переменную
        if os.path.exists(filename): # проверяем существует ли файл на компьютере, файла нет пропускаем, файл есть загружаем
            with open(filename, "r", encoding="utf-8") as f: # открываем файл и читаем
                reader = csv.DictReader(f) # DictReader читает CSV файл каждую строку возвращает как словарь
                for row in reader: # перебираем каждую строку в файле
                    if row["type"] == "Book": # если тип Book создаем объект Book
                        item = Book(row["item_id"], row["title"], int(row["amount"]), int(row["day_rent"]))
                    elif row["type"] == "DVD": # если тип DVD создаем объект DVD
                        item = DVD(row["item_id"], row["title"], int(row["amount"]), int(row["day_rent"]))
                    else: # иначе создаем объект Tarkvara
                        item = Tarkvara(row["item_id"], row["title"])
                        
                    item.popularity = int(row["popularity"]) # восстанавливаем популярность из CSV и int() потому что в CSV это строка "5" а не число 5
                    item.available = int(row["available"]) # восстанавливаем сколько доступно
                    self.items[item.item_id] = item # кладем объект в словарь библиотеки
            print(f"Объекты загружены из {filename}") # сообщаем что загрузка прошла успешно
            
            # 2. загружаем историю выдач
            filename = f"{self.name}_rentals.csv"
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.all_rentals.append(row)
                    print(f"Выдачи загружены из {filename}")
            
            # 3. загружаем штрафы
            filename = f"{self.name}_fines.csv"
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.all_fines.append(row)
                print(f"Штрафы загружены из {filename}")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#ФУНКЦИИ ДЛЯ ЛЮДЕЙ CSV
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# save_people, load_people, save_libraries, load_libraries это обычные функции не методы класса потому что они работают со всеми библиотеками и людьми сразу, а не с одной конкретной

def save_people(people):
    # сохраняем всех людей в CSV
    with open("people.csv", "w", newline="", encoding="utf-8") as f:# открываем файл для записи
        writer = csv.DictWriter(f, fieldnames=["name", "fines", "libraries"])  # создаём запись с колонками
        writer.writeheader()  # записываем заголовки
        for person in people.values():  # перебираем всех людей
            writer.writerow({  # записываем одну строку
                "name": person.name,  # имя человека
                "fines": person.fines,  # сумма штрафа
                "libraries": ",".join(person.libraries.keys())  # список библиотек в строку
                # join склеивает список в строку через запятую
                # ["Центральная", "Районная"] → "Центральная,Районная"
            })
    print("Люди сохранены в people.csv")  # сообщение об успешном сохранении

def load_people():
    # загружаем людей из CSV
    people = {}  # создаём пустой словарь
    if os.path.exists("people.csv"):  # проверяем существует ли файл
        with open("people.csv", "r", encoding="utf-8") as f:  # открываем файл для чтения
            reader = csv.DictReader(f)  # читаем файл как словари
            for row in reader:  # перебираем строки
                person = Person(row["name"])  # создаём объект человекаvc
                person.fines = float(row["fines"])  # восстанавливаем штраф
                # float превращает строку "0.12" в число 0.12
                people[person.name] = person  # добавляем в словарь
        print("Люди загружены из people.csv")  # сообщение об успешной загрузке
    return people  # возвращаем словарь людей

def load_libraries():
    # загружаем список библиотек из CSV
    libraries = {}  # создаём пустой словарь
    if os.path.exists("libraries.csv"):  # проверяем существует ли файл
        with open("libraries.csv", "r", encoding="utf-8") as f:  # открываем файл
            reader = csv.DictReader(f)  # читаем строки как словари
            for row in reader:  # перебираем строки
                lib = Library(row["name"])  # создаём библиотеку
                lib.load_from_csv()  # загружаем её данные
                # загружаем объекты, выдачи и штрафы этой библиотеки
                libraries[lib.name] = lib  # добавляем в словарь
        print("Библиотеки загружены!")  # сообщение об успешной загрузке
    return libraries  # возвращаем словарь библиотек

def save_libraries(libraries):
    # сохраняем список библиотек в CSV
    with open("libraries.csv", "w", newline="", encoding="utf-8") as f:# открываем файл для записи
        writer = csv.DictWriter(f, fieldnames=["name"])  # задаём колонку name
        writer.writeheader()  # записываем заголовок
        for lib in libraries.values():  # перебираем библиотеки
            writer.writerow({"name": lib.name})  # записываем название
            lib.save_to_csv()  # сохраняем данные библиотеки
            # сохраняем объекты, выдачи и штрафы каждой библиотеки
    print("Библиотеки сохранены!")  # сообщение об успешном сохранении
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#МЕНЮ
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
libraries = load_libraries()
people = load_people()

def menu_dobavit_predmet(library):
    # меню добавления объекта в библиотеку
    while True:
        print("\n  1 - Книга")
        print("  2 - ПО (Tarkvara)")
        print("  3 - DVD")
        print("  0 - Назад")
        vybor = input("  Выбери тип объекта: ")

        if vybor == "0":
            break
        elif vybor == "1":
            item_id = input("  ID книги: ")
            title = input("  Название книги: ")
            amount = int(input("  Сколько экземпляров: "))
            day_rent = int(input("  Сколько дней можно держать (по умолчанию 14): ") or 14)
            book = Book(item_id, title, amount, day_rent)
            library.add_item(book)
        elif vybor == "2":
            item_id = input("  ID ПО: ")
            title = input("  Название ПО: ")
            soft = Tarkvara(item_id, title)
            library.add_item(soft)
        elif vybor == "3":
            item_id = input("  ID DVD: ")
            title = input("  Название DVD: ")
            amount = int(input("  Сколько экземпляров: "))
            dvd = DVD(item_id, title, amount)
            library.add_item(dvd)
        else:
            print("  Ошибка! Выбери 0-3")

def menu_vzyat_predmet(library):
    # меню выдачи объекта читателю
    if len(people) == 0:
        print("  Нет людей!")
        return

    print("\n  Люди:")
    for name in people:
        print(f"    - {name}")
    name = input("  Имя человека: ")

    if name not in people:
        print(f"  Человек {name} не найден!")
        return
    person = people[name]
    # достаём объект человека из словаря people

    if len(library.items) == 0:
        print("  В библиотеке нет объектов!")
        return

    print("\n  Объекты в библиотеке:")
    for item_id, item in library.items.items():
        if isinstance(item, Tarkvara):
            print(f"    {item_id} - {item.title} | ПО | безлимит")
        else:
            print(f"    {item_id} - {item.title} | доступно: {item.available}/{item.amount}")

    item_id = input("  ID объекта: ")
    if item_id not in library.items:
        print(f"  Объект {item_id} не найден!")
        return

    item = library.items[item_id]
    # достаём объект из словаря библиотеки

    person.borrow(library, item)

def menu_vernut_predmet(library):
    # меню возврата объекта
    if len(people) == 0:
        print("  Нет людей!")
        return

    print("\n  Люди:")
    for name in people:
        print(f"    - {name}")
    name = input("  Имя человека: ")

    if name not in people:
        print(f"  Человек {name} не найден!")
        return
    person = people[name]

    if len(person.rentals) == 0:
        print(f"  У {name} ничего нет на руках!")
        return

    print(f"\n  На руках у {name}:")
    for item_id, rental in person.rentals.items():
        item = rental["item"]
        print(f"    {item_id} - {item.title}")

    item_id = input("  ID объекта для возврата: ")
    if item_id not in person.rentals:
        print(f"  Объект {item_id} не найден у {name}!")
        return

    item = person.rentals[item_id]["item"]
    person.return_item(library, item)

def menu_dannye(library):
    # меню данных библиотеки
    while True:
        print("\n  1 - Все объекты в библиотеке")
        print("  2 - Все читатели")
        print("  3 - Профиль пользователя")
        print("  4 - Штрафы библиотеки")
        print("  5 - Топ популярных")
        print("  0 - Назад")
        vybor = input("  Выбери: ")

        if vybor == "0":
            break
        elif vybor == "1":
            if len(library.items) == 0:
                print("  В библиотеке нет объектов!")
            else:
                print(f"\n  --- Объекты в {library.name} ---")
                for item_id, item in library.items.items():
                    if isinstance(item, Tarkvara):
                        print(f"  {item_id} | {item.title} | ПО | популярность: {item.popularity}")
                    else:
                        print(f"  {item_id} | {item.title} | доступно: {item.available}/{item.amount} | популярность: {item.popularity}")
        elif vybor == "2":
            if len(library.members) == 0:
                print("  Нет читателей!")
            else:
                print(f"\n  --- Читатели {library.name} ---")
                for name in library.members:
                    print(f"    - {name}")
        elif vybor == "3":
            if len(people) == 0:
                print("  Нет людей!")
                continue
            print("\n  Люди:")
            for name in people:
                print(f"    - {name}")
            name = input("  Имя человека: ")
            if name not in people:
                print(f"  Человек {name} не найден!")
                continue
            person = people[name]
            person.show_rentals()
            person.show_fines()
        elif vybor == "4":
            library.show_all_fines()
        elif vybor == "5":
            library.show_popular()
        else:
            print("  Ошибка! Выбери 0-5")

def menu_biblioteki(library):
    # главное меню одной библиотеки
    while True:
        print(f"\n=== {library.name} ===")
        print("1 - Зарегистрировать человека")
        print("2 - Добавить объект в библиотеку")
        print("3 - Выдать объект")
        print("4 - Вернуть объект")
        print("5 - Данные")
        print("0 - Назад")
        vybor = input("Выбери действие: ")

        if vybor == "0":
            break
        elif vybor == "1":
            if len(people) == 0:
                print("  Сначала создай человека в главном меню!")
                continue
            print("\n  Люди:")
            for name in people:
                print(f"    - {name}")
            name = input("  Имя человека: ")
            if name not in people:
                print(f"  Человек {name} не найден!")
                continue
            people[name].register(library)
        elif vybor == "2":
            menu_dobavit_predmet(library)
        elif vybor == "3":
            menu_vzyat_predmet(library)
        elif vybor == "4":
            menu_vernut_predmet(library)
        elif vybor == "5":
            menu_dannye(library)
        else:
            print("Ошибка! Выбери 0-5")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ГЛАВНОЕ МЕНЮ
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

while True:
    print("\n=============================")
    print("        ГЛАВНОЕ МЕНЮ")
    print("=============================")
    print("1 - Создать библиотеку")
    print("2 - Создать человека")
    print("3 - Войти в библиотеку")
    print("4 - Показать все библиотеки")
    print("5 - Показать всех людей")
    print("0 - Выход")
    vybor = input("Выбери действие: ")

    if vybor == "0":
        # сохраняем всё перед выходом
        save_libraries(libraries)
        save_people(people)
        print("До свидания!")
        break
    elif vybor == "1":
        name = input("Название библиотеки: ")
        if name in libraries:
            print(f"Библиотека {name} уже существует!")
        else:
            libraries[name] = Library(name)
            print(f"Библиотека {name} создана!")
    elif vybor == "2":
        name = input("Имя человека: ")
        if name in people:
            print(f"Человек {name} уже существует!")
        else:
            people[name] = Person(name)
            print(f"Человек {name} создан!")
    elif vybor == "3":
        if len(libraries) == 0:
            print("Нет библиотек! Сначала создай библиотеку.")
            continue
        print("\nБиблиотеки:")
        for name in libraries:
            print(f"  - {name}")
        name = input("Название библиотеки: ")
        if name not in libraries:
            print(f"Библиотека {name} не найдена!")
        else:
            menu_biblioteki(libraries[name])
    elif vybor == "4":
        if len(libraries) == 0:
            print("Нет библиотек!")
        else:
            print("\nВсе библиотеки:")
            for name in libraries:
                print(f"  - {name} | читателей: {len(libraries[name].members)} | объектов: {len(libraries[name].items)}")
    elif vybor == "5":
        if len(people) == 0:
            print("Нет людей!")
        else:
            print("\nВсе люди:")
            for name in people:
                print(f"  - {name} | библиотек: {len(people[name].libraries)}")
    else:
        print("Ошибка! Выбери 0-5")


































    
                
            

            

















