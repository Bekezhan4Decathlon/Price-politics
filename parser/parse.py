from bs4 import BeautifulSoup as bs
import requests
import random

class Parser:
    def __init__(self, HEADERS):
        self.HEADERS = HEADERS
    
    def get_content(self, url):
        html =  requests.get(url, headers=random.choice(self.HEADERS))
        soup = bs(html.text, 'html.parser')
        return soup

    def get_price_sportmaster(self, url):
        soup = self.get_content(url)
        item = soup.find_all('div', class_='cb-item-price-new')
        return item[0].span.text

    def get_price_limpopo(self, url):
        soup = self.get_content(url)
        item = soup.find_all('div', class_='product-price')
        return item[0].text

    def get_price_prosport(self, url):
        soup = self.get_content(url)
        item = soup.find_all('div', class_='h2_block')
        return item[0].text
