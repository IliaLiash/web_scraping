from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#Извлекает список всех внутренних ссылок на странице
def getInternalLinks(soup, includeURL):
    internalLinks = []
    #Находит все сслыку, которые начинаются с '/' текущего адреса
    for link in soup.find_all('a', href=re.compile('^(/|.*'+includeURL+')')):
        try:
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in internalLinks:
                    internalLinks.append(link.attrs['href'])
        except:
            pass
    return internalLinks

#Извлекает список внешних внутренних ссылок на странице
def getExternalLinks(soup, excludeUrl):
    externalLinks = []
    #Находит все ссылки, начинающиеся с https или www, не включая текущего URL
    for link in soup.find_all('a', href=re.compile('^(https|www)((?!'+excludeUrl+').)*$')):
        try:
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in externalLinks:
                    externalLinks.append(link.attrs['href'])
        except:
            pass
    return externalLinks


def splitAddress(address):
    addressParts = address.replace('https://', '').split('/')
    return addressParts

#Получить случайную внешнюю ссылку
def getRandomExternalLink(stratingPage):
    html = urlopen(stratingPage)
    soup = BeautifulSoup(html, 'html.parser')
    externakLinks = getExternalLinks(soup, splitAddress(stratingPage)[0])
    if len(externakLinks) == 0:
        internalLinks = getExternalLinks(soup, stratingPage)
        getExternalLinks(soup, internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externakLinks[random.randint(0, len(externakLinks)-1)]

#Функция старта
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: ' + externalLink)
    try:
        followExternalOnly(externalLink)
    except:
        pass

followExternalOnly(input())