import json
from urllib.request import urlopen

def getCountryCity(ipAddress):
    response = urlopen('http://ip-api.com/json/' + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return [responseJson.get('country'), responseJson.get('city')]

print(getCountryCity(input('Введите IP: ', )))