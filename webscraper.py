import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site
url = 'https://webscraper.io/test-sites/tables'

# Enviar uma solicitação HTTP para o servidor e receber o conteúdo HTML da página
response = requests.get(url)

# Analisar o HTML com a biblioteca BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

try:
    # Encontrar a tabela que contém as informações
    table = soup.find('table', {'class': 'table table-bordered'})

    # Extrair os dados da tabela e armazená-los em um DataFrame usando a biblioteca pandas
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        if cols:
            data.append(cols)
    df = pd.DataFrame(data, columns=['#', 'First Name', 'Last Name', 'Username'])

    # Imprimir o conjunto de dados resultante
    print(df)
except AttributeError as e:
    print("Erro ao encontrar a tabela:", e)
