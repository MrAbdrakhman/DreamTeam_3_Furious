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

from bs4 import BeautifulSoup
import requests
import csv
from pprint import pprint
CSV = 'lalafo.csv'
URL = 'https://lalafo.kg/kyrgyzstan/kvartiry/arenda-kvartir/posutochnaya-arenda-kvartir/q-%D0%B0%D1%80%D0%B5%D0%BD%D0%B4%D0%B0-%D0%BF%D0%BE%D1%81%D1%83%D1%82%D0%BE%D1%87%D0%BD%D0%BE'

r = requests.get(URL, verify=True)

soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find_all('div', class_='row')
    for item in items:
        apartment_cost = item.find('p', class_='tem-topic_cost topics-item-td')
        # if apartment_cost is None:
        #     apartment_cost = item.find('td', class_='topics-item-topic_cost topics-item-td som')

        list_appart.append({
            'Стоимость квартиры': apartment_cost
            # 'Количество комнат': item.find(
            #     'td', class_='topics-item-td topics-item-topic_rooms').get_text(strip=True),
            # 'Площадь': item.find(
            #     'td', class_='topics-item-topic_area topics-item-td').get_text(strip=True),
            # 'Серия': item.find(
            #     'td', class_='topics-item-topic_series topics-item-td').get_text(strip=True),
            # 'Описание': item.find(
            #     'td', class_='topics-item-topic_name topics-item-td').get_text(strip=True)
            })
    print(f'Страница номер {i} готова')

##def save()
with open('appart.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Стоимость квартиры', 'Количество комнат', 'Площадь', 'Серия', 'Описание'])
    for item in list_appart:
        writer.writerow([item['Стоимость квартиры'], item['Количество комнат'], item['Площадь'],item['Серия'],item['Описание']])


if __name__ == '__main__': '''