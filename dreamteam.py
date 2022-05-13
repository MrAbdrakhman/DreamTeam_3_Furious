# #
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.



# # 2 
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.



# # 3 
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>
class Student_room(object):
    name = ""
    age = 0
    major = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    def list_values(self):
        print(f"Name: {self.name}")
        print (f"Age: {self.age}")
        print (f"Major: {self.major}")

def make_student(name, age, major):
    student = Student_room(name, age, major)
    return student

print("A list of students.")
Steve = make_student("Steven Schultz",23,"English")
Johnny = make_student("Jonathan Rosenberg",24,"Biology")
Penny = make_student("Penelope Meramveliotakis",21,"Physics")
Steve.list_values()
Johnny.list_values()
Penny.list_values()



# # 4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:
# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

def dollarize(value):

    value = str(value).split('.')
    money = ''
    count = 1

    for digit in value[0][::-1]:
        if count != 3:
            money += digit
            count += 1
        else:
            money += f'{digit},'
            count = 1

    if len(value) == 1:
        money = ('$' + money[::-1]).replace('$-','-$')
    else:
        money = ('$' + money[::-1] + '.' + value[1]).replace('$-','-$')
    return money

print(dollarize(int(input("Enter a float: "))))

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

from decimal import Decimal

def moneyfmt(value, places=2, curr='', sep=',', dp='.',
             pos='', neg='-', trailneggg=''):

    q = Decimal(10) ** -places
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = list(map(str, digits))
    build, nex = result.append, digits.pop
    if sign:
        build(trailneggg)
    for i in range(places):
        build(nex() if digits else '0')
    if places:
        build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(nex())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))

d = Decimal(12345678.021)

print(moneyfmt(d, curr='$'))
print(moneyfmt(d, places=0, sep='.', dp='', neg='', trailneggg='-'))
print(moneyfmt(d, curr='$', neg='(', trailneggg=')'))
print(moneyfmt(Decimal(1234567.021), sep=' '))
print(moneyfmt(Decimal('-0.03'), neg='<', trailneggg='>'))
# $12,345,678.02
# 12.345.678
# $12,345,678.02
# 1 234 567.02
# <0.03>

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

# # 5  
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
# from random import shuffle

class Card:
    suits = ["червы", "бубны", "трефы", "пики"]
    ranks = ["narf", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return (self.ranks[self.rank] + " из " + self.suits[self.suit])

    def __cmp__(self, other):
        # check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # ranks are the same... it's a tie
        return 0
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + "" * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return (len(self.cards) == 0)

deck=Deck()
print(deck)
deck.shuffle()
deck.print_deck()



# # 6 
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название 
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

# Данные отдать в csv

