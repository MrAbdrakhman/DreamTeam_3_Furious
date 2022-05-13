# # 1
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
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб:
# 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь,
# список названий мебели.


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return'Мебель:% s Занятая площадь:% .2f '% (self.name, self.area)

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.furniture_list = []

    def __str__(self):
        return'Тип дома % s площадь % .2f остаточная площадь% .2f список мебели% s '\
               %(self.house_type,self.area,self.free_area,self.furniture_list)

    def add_furniture(self,Furniture):
        print('Добавить мебель % s площадь: % .2f '% (Furniture.name, Furniture.area))
        self.furniture_list.append(Furniture.name)
        self.free_area -= Furniture.area



bed = Furniture('Спальня',4)
table = Furniture('Стол',1.5)
closet = Furniture('Гардеробная',2)


my_house = House('Особняк', 200)

my_house.add_furniture(bed)
my_house.add_furniture(table)
my_house.add_furniture(closet)

print (my_house)
