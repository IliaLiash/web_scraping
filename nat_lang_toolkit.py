import nltk
from nltk import FreqDist, bigrams, trigrams, word_tokenize, pos_tag, Text
#tokens = word_tokenize('Здесь располагается текст для анализа')
#text = Text(tokens)

with open('peskov.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fdist = FreqDist(text.split())  #frequency distribution - наиболее части встречающиеся слова
print(fdist.most_common(10))

bigrams = bigrams(text.split())
bigramsDist = FreqDist(bigrams)     #создание объекта биграмм. Есть также 3-граммы и n-граммы.
for element in bigramsDist:         #перебор элементов, проверка на наличие
    if 'Путин' in element:
        print(element)

trigrams = trigrams(text.split())
trigramsDist = FreqDist(trigrams)
for element in bigramsDist:         #перебор элементов, проверка на наличие
    if 'Кремль' in element:
        print(element)

