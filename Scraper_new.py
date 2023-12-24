# включення необхідних бібліотек
import bs4
import requests

# Створення перемінної з данними сайту
url = 'https://webscraper.io'
website = (url+'/test-sites/e-commerce/static/computers/laptops')
site_cod = requests.get(website)
site_cod.raise_for_status()
clear_cod = bs4.BeautifulSoup(site_cod.text, 'html.parser')

#Створюеться скрапер на першу сторінку
mashines = clear_cod.find_all('div', class_ ='col-md-4 col-xl-4 col-lg-4')
for mashine in mashines:
    name1 = mashine.find('a', class_='title')
    description = mashine.find('p', class_='description card-text')
    print(name1.text,"\n",description.text)

#Інший метод перебору сторінок

#пошук елемента з посиланням на наступну сторінку
next_page_element = clear_cod.find('a', {'rel': 'next'})
#Якщо такие елемент є, то створюється скрпер з посиланням на наступну сторінку
while next_page_element is not None:
    next_page_link = next_page_element.get('href')
    page = (url + next_page_link)
    #Витягується дані із сторінки
    site_cod = requests.get(page)
    site_cod.raise_for_status()
    clear_cod = bs4.BeautifulSoup(site_cod.text, 'html.parser')
    #Створення перемінної, в якій зберігаються необхідні шматки коду
    mashines = clear_cod.find_all('div', class_ ='col-md-4 col-xl-4 col-lg-4')
    #Створення циклу, який перебирає кожен шматок коду і повертає необхідні дані
    for mashine in mashines:
        name1 = mashine.find('a', class_='title')
        description = mashine.find('p', class_='description card-text')
        print(name1.text,"\n",description.text)
        #Повернення даних про наявність наступної сторінки у перемінну
        next_page_element = clear_cod.find('a', {'rel': 'next'})


