import requests
from bs4 import BeautifulSoup
from selenium import webdriver

session = requests.Session()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
           "Accept":'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}   #передав headers можно настроить региональные настройки, язык и т.д.
url = 'https://developers.whatismybrowser.com/'
req = session.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.find(id='id_user_agent'))

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.facebook.com/events/777016493046448/')
driver.implicitly_wait(1)
print(driver.get_cookies()) #также есть delete_cookie(), add_cookie(), delete_all_cookies()