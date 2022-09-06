import requests

url = 'https://raw.githubusercontent.com/edubd/bd/main/paises.csv'

csv = requests.get(url).text
linhas = csv.splitlines()
tot_europa = tot_america = extensao_europa = 0



for lin in linhas:
    colunas = lin.split(",")
    if colunas[2] == 'Europa':
        tot_europa +=1
        extensao_europa += float(colunas[3])
    
    
print(extensao_europa / tot_europa)



