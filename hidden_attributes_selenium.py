from selenium import webdriver

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
driver.get('http://pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements_by_tag_name('a')

for link in links:
    if not link.is_displayed():
        print('The link ' + link.get_attribute('href') + ' is a trap')

fields = driver.find_elements_by_tag_name('input')
for field in fields:
    if not field.is_displayed():
        print('Do not change value of ' + field.get_attribute('name'))