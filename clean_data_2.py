from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
    input = input.lower()
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split()
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input) - n + 1):
        ngramTemp = ' '.join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

def isCommon(ngrams):
    commonWords = []
    with open('1-1000.txt', 'r') as f:
        for line in f:
            commonWords.append(str(line).replace('\n',''))
    res = []
    for element in ngrams:
        if element[0].split()[0] and element[0].split()[1] in commonWords:
            continue
        else:
            res.append(element)
    return res

html = urlopen(input('Введите url: ', ))
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', {'id':'mw-content-text'}).get_text() #ищем специфично - find + get_text()
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True) #Сортировка списка кортежей по 1 элементу каждого.
#print('Полный список 2-грамм:\n', sortedNGrams)
print('------------------------------------------------')
print('Список 2-грамм без популярных слов: ', isCommon(sortedNGrams))