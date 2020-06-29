import csv
import os
import requests
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

ENDPOINT = 'https://www.avito.ru/sankt-peterburg/nedvizhimost'
resp = requests.get(ENDPOINT)

soup = BeautifulSoup(resp.content, features='lxml')

titles = [i.get('title') for i in soup.find_all('a', {'data-marker': 'title'})]

items = soup.find_all('div', {'data-marker': 'bx-recommendations-block-item'})
prices = [it.find('div', {'itemprop': 'price'}).get('content') for it in items]

result = [(titles[k], int(v)) for k, v in enumerate(prices)]

with open('result.csv', 'w', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile, delimiter='|', quotechar='"')
    for item in result:
        writer.writerow(list(item))

plt.scatter(*[list(i) for i in zip(*result)], c=(1, 0, 0))
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([])
plt.show()
