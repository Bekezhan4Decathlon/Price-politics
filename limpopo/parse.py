from bs4 import BeautifulSoup as bs
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125',
    'accept': '*/*',
}
url = 'https://prosport.kz/slates-for-children-arena-sharm'
html =  requests.get(url, headers=HEADERS)
soup = bs(html.text, 'html.parser')

item = soup.find_all('div', class_='h2_block')
print(item)
print(item[0].text)

# class LimpopoOrProSport:
#     def __init__(self, HEADERS):
#         self.HEADERS = HEADERS

#     def get_content(self, url):
#         html =  requests.get(url, headers=self.HEADERS)
#         soup = bs(html.text, 'html.parser')
#         return soup

#     def get_price_limpopo(self, url):
#         soup = self.get_content(url)
#         item = soup.find_all('div', class_='product-price')
#         return item[0].text
