import requests
from bs4 import BeautifulSoup
import pandas


baseurl = "https://www.thewhiskyexchange.com"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' }


# Obter links de cada produto
product_links = []
for page in range(1,6):  
    html = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={page}&psize=24&sort=pasc', headers = headers).text  
    soup = BeautifulSoup(html,'html.parser')  
    product_list = soup.find_all("li",{"class":"product-grid__item"})
 
    for product in product_list:
        link = product.find("a",{"class":"product-card"}).get('href')
        product_links.append(baseurl + link)


# Obter informacoes de cada produto
data = []
for link in product_links:
    p_html= requests.get(link, headers = headers).text
    p_soup = BeautifulSoup(p_html, 'html.parser')

    # ========== PRECO ==========
    try:
        price = p_soup.find('p', {'class': 'product-action__price'}).text.replace('\n', '')
    except:
        price = 'N/A'

    # ========== SOBRE ==========
    try:
        about = p_soup.find('div', {'class': 'product-main__description'}).text.replace('\n', '')
    except:
        about = 'N/A'
    
    # ========== AVALIACAO ==========
    try:
        rating = p_soup.find('div', {'class': 'review-overview'}).text.replace('\n', '')
    except:
        rating = 'N/A'
    
    # ========== NOME ==========
    try:
        name = p_soup.find('h1', {'class': 'product-main__name'}).text.replace('\n', '')
    except:
        name = 'N/A'

    whisky = {'NOME': name, 'PRECO':price, 'AVALIACAO': rating, 'SOBRE': about}
    data.append(whisky)


# Formatacao de dados e criacao de arquivo
result = pandas.DataFrame(data)
tabela_file = open('tabela-whisky.txt', 'a')
tabela_file.write(result.to_string())
tabela_file.close()