
import requests
from bs4 import BeautifulSoup
import time
import os

try:
    os.remove("urls.txt")
except:
    pass

url  = 'https://assettoland.wixsite.com/assettoland/cars'

response = requests.get(url)

if response.ok:
    print(response)
    time.sleep(1)
    links =[]
    soup = BeautifulSoup(response.text, 'html.parser')
    i = 0
    for link in soup.findAll('a',{ 'class': 'style-jjz9hyh02imageItemlink'}):
        print(link['href'])
        with open('urls.txt', 'a') as  file:
            file.write(link['href'] + '\n')
        i = i + 1
    print('Nombre de lien:' + str(i))

else:
    print('Erreur')
    print(response)

exec(open("./assetto2.py").read())


    

