from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.facebook.com/events/777016493046448/')
html = driver.page_source   #для использования далее в BS

soup = BeautifulSoup(html, 'html.parser')
result = soup.find('div', class_=['2ycp', '_5xhk'])
print(result.text)
driver.close()