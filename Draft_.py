import requests

from bs4 import BeautifulSoup

link = 'https://rabota.ua/cv/12105529'

proxies = {'http': 'http://95.47.122.75:80808'}
link_responce = requests.get(link, proxies=proxies, timeout=5)
link_soup = BeautifulSoup(link_responce.content, 'html.parser')
name = link_soup.find('p', attrs={'class': 'rua-p-t_12'}).get_text()
# name_lst = list(name)
a = []
str = ''
for i in list(name):
    if i.isdigit():
        str += i
digt = int(str)
print(digt)
