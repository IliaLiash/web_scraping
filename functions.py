from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

print('---------------START--------------------------')
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
#print(html.read()) #html.read() - получает код страницы

soup = BeautifulSoup(html.read(), 'html.parser')
print(soup.h1)

#Аналогичные результат с доступом через вложенны теги
print(soup.html.body.h1)
print(soup.body.h1)
print(soup.html.h1)
print('---------------------------------------------------')
'''
Есть две основные ошибки, которые могут возникнуть здесь:
• страница не найдена на сервере (или есть какая-то ошибка при
ее получении);
• сервер не найден.
Во всех этих случаях функция urlopen генерирует общее исключение «HTTPError»
'''
print('---------------TRY-EXCEPT--------------------------')

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
soup = BeautifulSoup(html.read(), 'html.parser')
try:
    badContent = soup.nonExistentTag.someTag
except:
    print('Some problems...')
else:
    if badContent == None:
        print('Tag is not found')
    else:
        print(badContent)
print('---------------------------------------------------')

print('---------------TRY-EXCEPT-2--------------------------')
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        soup = BeautifulSoup(html.read(), 'html.parser')
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title

#title = getTitle(input('Введите url: ',))
title = getTitle('http://bit.ly/1Ge96Rw')
if title == None:
    print("Title could not be found")
else:
    print(title)
print('---------------------------------------------------')

print('---------------SOUP.FINDALL, GET_TEXT()--------------------------')
html = urlopen('http://bit.ly/1Ge96Rw')
soup = BeautifulSoup(html.read(), 'html.parser')

namelist = soup.find_all('span', {'class':'green'}) #Ищет так: <span class='green'>...</span>
for name in namelist:
    print(name.get_text())  #get_text() для получения текста

princecount = soup.find_all(text='the prince')
print("'the prince':", len(princecount))
print('---------------------------------------------------')

print('---------------CHILD, SIBLINGS--------------------------')
html = urlopen('http://bit.ly/1KGe2Qk')
soup = BeautifulSoup(html.read(), 'html.parser')

for child in soup.find('table',{'id':'giftList'}).children: #поиск потомков
    print(child)

html = urlopen('http://bit.ly/1KGe2Qk')
soup = BeautifulSoup(html.read(), 'html.parser')
for sibling in soup.find('table',{'id':'giftList'}).tr.next_siblings:   #следующие одноуровневые элементы
    print(sibling)
print('---------------------------------------------------')

print('---------------RE, ATTRS--------------------------')
html = urlopen('http://bit.ly/1KGe2Qk')
soup = BeautifulSoup(html.read(), 'html.parser')
images = soup.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})    #атрибуты-словарь для тега
for image in images:
    print(image.attrs)
    print(image['src']) #доступ по ключу
print('---------------------------------------------------')

print('---------------LAMBDA--------------------------')
html = urlopen('http://bit.ly/1KGe2Qk')
soup = BeautifulSoup(html.read(), 'html.parser')
tags = soup.find_all(lambda tag: len(tag.attrs) == 2)   #все теги у которых один атрибут (href, src - это атрибуты)
print(tags)

'''
Eсли вы отбираете что-то более конкретное, попробуйте find
а если вы отбираете что-то более общее из <a> или <span> , возможно, попробуйте find_all.'''