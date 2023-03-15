import requests
from bs4 import BeautifulSoup
import time
import os

try:
    os.remove("url_downloading.txt")
except:
    pass

with open('urls.txt', 'r') as file:
    for row in file:
        url = row.strip()
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.findAll('a',{ 'class': 'ca1link'}):
                print(link['href'])
                with open('url_downloading.txt', 'a') as  file:
                    file.write(link['href'] + '\n')
