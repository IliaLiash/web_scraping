from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

torexe = os.popen(r'G:\Tor Browser\Browser\firefox.exe')
profile = FirefoxProfile(r'G:\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'C:\geckodriver\geckodriver.exe')
driver.get("http://icanhazip.com/")
print(driver.page_source)