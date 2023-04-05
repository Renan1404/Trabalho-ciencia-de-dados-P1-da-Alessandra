import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://exame.com/brasil/as-50-melhores-escolas-de-cada-estado-do-brasil-no-enem/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')

data = []
for row in table.find_all('tr')[1:6]:
    cells = row.find_all('td')
    posicao = cells[0].get_text().strip()
    nome_escola = cells[1].get_text().strip()
    nota_media = cells[2].get_text().strip()
    uf = cells[3].get_text().strip()
    data.append([posicao, nome_escola, nota_media, uf])

df = pd.DataFrame(data, columns=['Posicao', 'Nome da escola', 'Nota media', 'UF'])

print(df)

