from urllib.request import urlretrieve
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'H:\Tesseract\tesseract.exe'
img = 'https://s0.rbk.ru/v6_top_pics/resized/590xH/media/img/9/26/755989776726269.jpg'
urlretrieve(img, 'img.jpg') #скачиваем файл
p = pytesseract.image_to_string('img.jpg', lang='rus')  #разпознаем
print(p)
with open('text_1.txt', 'w', encoding='utf-8') as f:    #записываем в файл
    f.write(p)