import requests

url = 'https://raw.githubusercontent.com/edubd/bd/main/paises.csv'

csv = requests.get(url).text
print(csv)
