from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''
Подход: начинаем сканирование со страниц верхнего уровня и находим список всех внутренних ссылок этой страницы
Затем сканируем каждую из этих ссылок и находим для нее свой список и так далее
'''

'''
print('-----------КРАУЛЕР WIKI ОБХОД ССЫЛОК------------')
pages = set()
def getLinks(pageURL):
    global pages
    html = urlopen('http://en.wikipedia.org' + pageURL)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        print(soup.h1.get_text() + ':', end=' ')
    except:
        pass
    for link in soup.find_all('a', href=re.compile('^(/wiki/)')):   #все ссылки, начинающиеся с /wiki/
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)       #рекурсия
getLinks('')
print('----------------------------------------')
'''
print('-----------КРАУЛЕР ОБХОД ССЫЛОК ЛЮБОГО САЙТА------------')
pages = set()
def getLinks(pageURL):
    global pages
    html = urlopen(pageURL)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        print(soup.h1.get_text() + ':', end=' ')
    except:
        pass
    address = pageURL.replace('https://','').split('.')
    for link in soup.find_all('a', href=re.compile('^(/|.*'+address[0]+')')):
        try:
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)       #рекурсия
        except:
            pass
getLinks(input('Введите сайт для скрапинга: ', ))