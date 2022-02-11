from bs4 import BeautifulSoup as bs
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125',
    'accept': '*/*',
}
url = 'https://sportmaster.com/ru-kz/product/22116250299/'
html =  requests.get(url, headers=HEADERS)
soup = bs(html.text, 'html.parser')

item = soup.find_all('div', class_='cb-item-price-new')
print(item[0].span.text)



