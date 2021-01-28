from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

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
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i+n])
    return output

html = urlopen(input('Введите url: ', ))
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', {'id':'mw-content-text'}).get_text() #ищем специфично - find + get_text()
ngrams = ngrams(content, 2)
ngrams = Counter(tuple(item) for item in ngrams)  #сортируем так: подсписок - сколько раз подсписок встречается в списке-результате ngrams

print(ngrams.most_common(10))
