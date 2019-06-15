from typing import Optional

import re
from bs4 import BeautifulSoup

from http_connection import HttpConnection
from model.car_model import Car


class PageParser:
    @staticmethod
    def findCarProperties(ResultSet):
        filteredData = {}

        for elem in ResultSet:
            if elem['alt'] and elem['alt'] != "Телефон" and elem['alt'] != "затвори":
                car_info_key = elem['alt']
                car_info_data = elem.find_parent('tr').contents[3].text
                filteredData[car_info_key] = car_info_data
        return filteredData

    @staticmethod
    def hasCyrillic(text):
        return bool(re.search('[\u0400-\u04FF]', text))
    @property
    def findProperty(ResultSet, propertyToSearch:str) -> Optional:

        filteredData = {}
        for elem in ResultSet:
            if elem['alt'] and elem['alt'] != "Телефон":
                car_info_key = elem['alt']
                print(elem)
                #car_info_data = elem.find_parent('tr').contents[3].text
               # filteredData[car_info_key] = car_info_data
        return filteredData

    def parsePage(self, httpConnection:HttpConnection, url:str) -> Optional[Car]:

        r = httpConnection.requestSession.get(url)

        src = r.text

        myCar = Car()

        if r.headers.get('Set-Cookie') is None:
            print("code is 302")
            return None

        soup = BeautifulSoup(src, isHTML=1)

        all_images_with_alt_tag = soup.find_all("img", alt=True)
        name_and_price_table = soup.find("table", class_="ver13black")
        name_and_price = name_and_price_table.find_all("strong")

        if len(name_and_price) < 2:
            return None

        myCar.car_data = self.findCarProperties(all_images_with_alt_tag)
        myCar.id = r.url.split("/")[4]
        myCar.name = name_and_price[0].text
        myCar.price = int(name_and_price[1].text.replace(",", ""))
        extraInfo = {}
        security = soup.find("b", text="Сигурност:")
        comfort = soup.find("b", text="Комфорт:")
        other = soup.find("b", text="Друго:")
        eurostandart = soup.find("b", text="Евростандарт:")
        textDescrp =  soup.find("b", text="Допълнителна информация")

        if security:
            extraInfo["Сигурност"] = security.find_parent().find_parent().contents[3].text.strip()
        if comfort:
            extraInfo["Комфорт"] = comfort.find_parent().find_parent().contents[3].text.strip()
        if other:
            extraInfo["Друго"] = other.find_parent().find_parent().contents[3].text.strip()
        if eurostandart:
            extraInfo["Евростандарт"] = eurostandart.find_parent().find_parent().contents[3].text.strip()
        else:
            extraInfo["Евростандарт"] = 0
        if textDescrp:
            extraInfo["Описание"] = textDescrp.find_parent().find_parent().find_parent().contents[5].text.strip()

        carContact = soup.find("div", id="contacts_seller_conteiner")
        boldElinCar = carContact.find_all("b")
        l = set()
        for el23 in boldElinCar:
            if el23.text != 'Затвори':
                l.add(el23.text)

        if carContact.find(text="Частно лице"):
            extraInfo["частно_лице"] = True
            extraInfo["град"] = l.pop()
        else:
            extraInfo["частно_лице"] = False
            tr1 = l.pop()
            if self.hasCyrillic(tr1):
                extraInfo["град"] = tr1
            else:
                extraInfo["град"] = l.pop()

        myCar.car_extra_data = extraInfo
        return myCar
