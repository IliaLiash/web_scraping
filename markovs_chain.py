#Генерация цепи Маркова
#Что нам скажет Дмитрий Песков?
from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    #Удаляем символы новой строки и кавычки
    text = text.replace('\n',' ').replace('"','')
    punctuation = [',','.',';',':']
    for symbol in punctuation:
        text.replace(symbol, ' ' + symbol + ' ')
    words = text.split(' ')
    #Удаляем пустые слова
    words = [word for word in words if word != '']

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            #Создаем новый словарь для этого слова
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1

    return wordDict

#text = str(urlopen('https://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
with open('peskov.txt', 'r', encoding="utf8") as f:
    text = f.read()

wordDict = buildWordDict(text)

length = 256
chain = ''
currentWord = 'Путин'
for i in range(0, length):
    chain += currentWord + ' '
    try:
        currentWord = retrieveRandomWord(wordDict[currentWord])
    except:
        pass
print(chain)
