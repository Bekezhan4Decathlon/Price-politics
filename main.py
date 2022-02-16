import pandas as pd
import random
import time

from sportmaster.parse import Parser
# from limpopo.parse import LimpopoOrProSport

HEADERS = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125',
        'accept': '*/*',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15',
        'accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
        'accept': '*/*'
    },
    {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'accept': '*/*'
    }
]

parser = Parser(HEADERS)
# limpopo = LimpopoOrProSport(random.choice(HEADERS))

if __name__ == '__main__':
    input_file = pd.read_excel('COP 05718.xlsx')
    for column in input_file.columns:
        if "link" in column.lower():
            for link in input_file[column]:
                print(link)
                try:
                    if "sportmaster" in link.lower():
                        # print(parser.get_price(link))
                        input_file.loc[input_file[column] == link, "Sportmaster price"] = parser.get_price_sportmaster(link)
                        time.sleep(random.randrange(4, 8))
                    elif "kaspi" in link.lower():
                        pass
                    elif "limpopo" in link.lower():
                        input_file.loc[input_file[column] == link, "ProSport/Limpopo price"] = parser.get_price_limpopo(link)
                        time.sleep(random.randrange(4, 8))
                    elif "prosport" in link.lower():
                        input_file.loc[input_file[column] == link, "ProSport/Limpopo price"] = parser.get_price_prosport(link)
                        time.sleep(random.randrange(4, 8))
                except Exception as e:
                    print(e)


input_file.to_excel("test.xlsx")
