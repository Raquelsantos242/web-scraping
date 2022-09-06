import urllib3

url = 'https://raw.githubusercontent.com/edubd/bd/main/paises.csv'

http = urllib3.PoolManager()
response = http.request('GET', url)

csv = response.data
print(csv)

s = csv.decode('utf-8')
print(s)