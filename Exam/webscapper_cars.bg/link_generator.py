import random

import requests
from bs4 import BeautifulSoup
from time import sleep

from http_connection import HttpConnection


class LinkGenerator:

    def generateLinks(self, httpConnection: HttpConnection, fileNameToSave:str):
        numTry = 3350
        breaker = True
        lastId = 66981
        while breaker:
            url = 'https://www.cars.bg/?go=cars&search=1&fromhomeu=1&currencyId=1&autotype=1&stateId=1&offersFor4=1&offersFor1=1&filterOrderBy=1&page=' + str(
                numTry) + '&cref=95869'
            r = httpConnection.requestSession.get(url)

            print("checking url {}".format(url))

            src = r.text

            soup = BeautifulSoup(src, isHTML=1)

            pagination = soup.find("a", class_="pager", text="Следваща")
            if pagination:
                print("there is a next_page")
            else:
                breaker = False

            links = soup.find_all("a", class_="ver15black")

            with open(fileNameToSave, 'a', encoding='utf-8') as f:
                for item in links:
                    f.write("{0}, https://www.cars.bg/{1}, {2} \n".format(lastId, item['href'], item.text, encoding='utf-8'))
                    lastId += 1

            numTry += 1
            print("next page is number {}".format(numTry))
            sleepTime = random.randrange(24, 55)
            print("sleeping for {} sec".format(sleepTime))
            sleep(30)
