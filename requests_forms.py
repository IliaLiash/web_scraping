import requests

params = {'firstname': 'Dmitriy', 'lastname': 'Peskov'}
r = requests.post('https://pythonscraping.com/files/processing.php', data=params)
print(r.text)

