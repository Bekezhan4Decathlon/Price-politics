from bs4 import BeautifulSoup as bs
import requests
import random
import json

class Parser:
    def __init__(self, USER_AGENTS):
        self.USER_AGENTS = USER_AGENTS
    
    def get_content(self, url):
        html = requests.get(url)
        return bs(html.text, 'html.parser')

    def get_content_for_kaspi(self, url):
        r=requests.get(f"{url}", headers={
            "Host": "kaspi.kz",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": random.choice(self.USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        })
        return bs(r.text, 'html.parser') 

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

    def get_price_kaspi(self, url):
        soup = self.get_content_for_kaspi(url)
        return json.loads(soup.find('script', type='application/ld+json').text)['offers']['offers'][0]['price']

        

