import requests
from bs4 import BeautifulSoup as BS


def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

def get_last_page(soup:BS) -> int:
    last = soup.find('li', {'class':'last'})
    if last is None:
        return 1
    return int(last.text)