import requests

url = 'https://raw.githubusercontent.com/edubd/bd/main/paises.csv'

csv = requests.get(url).text
linhas = csv.splitlines()
tot_europa = tot_america = 0


for lin in linhas:
    colunas = lin.split(",")
    if colunas[2] == 'Europa': tot_europa +=1
    elif colunas[2] == 'América': tot_america +=1
    
print(tot_europa, tot_america)


