import requests
from bs4 import BeautifulSoup

URL = 'https://time.is'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'
}

def get_html(url, params=''):                                # to get global HTML
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):                                       # to get the exact elements
    soup = BeautifulSoup(html, 'html.parser')
    clock = soup.find('div', id='clock0_bg')
    return clock.find('time', id='clock').get_text()




html = get_html(URL)
print(get_content(html.text))