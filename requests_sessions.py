import requests
#Через сессии (отслеживает cookies, заголовки, протоколы)
session = requests.Session()
params = {'username': 'username', 'password': 'password'}
s = session.post('https://pythonscraping.com/pages/cookies/welcome.php', params)    #welcome.php
print('Cookies:')
print(s.cookies.get_dict())
print('Переходим на страницу профиля...')
s = session.get('https://pythonscraping.com/pages/cookies/profile.php')     #тут уже не указваются cookies. profile.php
print(s.text)