import requests

url = 'https://raw.githubusercontent.com/edubd/bd/main/paises.csv'

csv = requests.get(url).text
linhas = csv.splitlines()
for lin in linhas:
    colunas = lin.split(",")
print(colunas[1])


