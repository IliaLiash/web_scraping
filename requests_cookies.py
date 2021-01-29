import requests

params = {'username': 'Peskov', 'password': 'password'}
r = requests.post('https://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookies:')
print(r.cookies.get_dict())
print('Переходим на страницу профиля...')
r = requests.get('https://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)
print('-----------------------------')