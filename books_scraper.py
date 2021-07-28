import requests
from bs4 import BeautifulSoup
import json

headers = {
    #'authority': 'books.toscrape.com',
    #'method': 'GET',
    #'path': '/index.html',
    #'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    #'dnt': '1',
    #'if-modified-since': 'Thu, 25 Mar 2021 13:59:05 GMT',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

page = 1
while True:
    request = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html', headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'html.parser')
        livros_html = soup.find_all('article', {'class': 'product_pod'})

        # LIVROS
        for item in livros_html:
            h3 = item.find('h3')
            titulo = h3.find('a').get('title')
            preco = item.find('p', {'class': 'price_color'}).text
            
            livro = {
                'titulo': titulo,
                'preco': preco[2:]
            }

            print(json.dumps(livro))

        page = page + 1

    else:
        break