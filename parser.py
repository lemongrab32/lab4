import requests
from bs4 import BeautifulSoup as bs


def parse(currency):
    response = requests.get('https://www.cbr.ru/currency_base/daily/')
    soup = bs(response.text, 'html.parser')

    block = soup.find_all('tr')
    new_block = [
        block[14],
        block[15],
        block[23],
        block[38]
    ]

    currensies = {}

    for i in range(len(new_block)):
        list1 = new_block[i].text.split('\n')
        list1.pop(0)
        list1.pop(5)
        list1[4] = list1[4].replace(',', '.')
        currensies[list1[1]] = float(list1[4])

    return currensies[currency]