from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import json

random.seed(datetime.datetime.now())

#Извлекает список всех внутренних ссылок на указанной странице
def getLinks(articleURL):
    html = urlopen('http://en.wikipedia.org' + articleURL)  #открыть ссылку
    soup = BeautifulSoup(html, 'html.parser')   #приготовить суп из содержимого ссылки
    print(soup.title.get_text())    #Печатаем title ссылки
    return soup.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')) #извлечь из супа

#Ищет содержимое всех ссылок с классом mw-anonuserlink (содержат IP адреса вместо имени пользователя)
def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace('/wiki/','')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title=' + pageUrl + '&action=history' #готовим ссылку
    print('history url is: ' + historyUrl)
    html = urlopen(historyUrl)  #открываем ссылку
    soup = BeautifulSoup(html, 'html.parser')   #готовим суп из содержимого ссылки (страница правок)
    print(soup.title.get_text())    #Печатаем title ссылки

    ipAddresses = soup.find_all('a', {'class':'mw-anonuserlink'})   #находим все адреса с IP вместо юзера
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())   #получаем набор уникальных IP адресов
    return addressList                          #и возварщаем его

def getCountryCity(ipAddress):
    try:
        response = urlopen('http://ip-api.com/json/' + ipAddress).read().decode('utf-8')
    except:
        return None
    responseJson = json.loads(response)
    return [responseJson.get('country'), responseJson.get('city')]

links = getLinks('/wiki/Vladimir_Putin')    #получаем список всех ссылок нас странице

while len(links) > 0:
    for link in links:
        print('-----------------------')
        historyIPs = getHistoryIPs(link.attrs['href'])  #Передаем href в функцию getHistoryIPs, которая возвращает список IP адресов (результат функции)
        for historyIP in historyIPs:                    #Печатаем IP адрес
            country = getCountryCity(historyIP)         #Получаем страну и город
            if country is not None:
                print(historyIP + ' from ' + country[0] + ' ' + country[1])

    newLink = links[random.randint(0, len(links)-1)].attrs['href']  #случайным образом выбираем новую ссылку
    links = getLinks(newLink)                                       #применяем к ней функцию getList - возвращает список, если len(links) > 0- все по новой




