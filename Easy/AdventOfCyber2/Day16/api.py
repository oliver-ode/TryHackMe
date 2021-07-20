import requests
from bs4 import BeautifulSoup as bs

# 57 @ Winter Wonderland, Hyde Park, London.
for i in range(1, 100, 2):
    html = requests.get(f'http://10.10.21.105/api/{i}')
    print(i, html.text)