import requests
from bs4 import BeautifulSoup as bs

html = requests.get('http://10.10.21.105/static/index.html')
soup = bs(html.text, 'lxml')

# /api/
for a in soup.find_all('a'):
    print(a)