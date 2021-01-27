from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

print('-----------KEVIN BACON WIKI------------')
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile("^(/wiki/)((?!:).)*S")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
print('----------------------------------------')

print('-----------KEVIN BACON GETLINKS "WHILE LINKS"------------')
random.seed(datetime.datetime.now())
def getLinks(articleURL):
    html = urlopen('http://en.wikipedia.org' + articleURL)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile("^(/wiki/)((?!:).)*S"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

'''
1) getLinks берет адрес из Вики и добавляет в него извлеченные из bs4 newArticle
2) getLinks будет вызываться до тех пор, пока на выданной из bs4 странице не будет ни одной ссылки
'''