import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'https://arv.co.il'

def getAbsoluteUrl(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://' + source[11:]
    elif source.startswith('https://') or source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        source = source[4:]
        url = 'http://' + source
    else:
        url = baseUrl + '/' + source

    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen('https://arv.co.il')
soup = BeautifulSoup(html, 'html.parser')
downloadList = soup.find_all(src=True)

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
    try:
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
    except:
        pass