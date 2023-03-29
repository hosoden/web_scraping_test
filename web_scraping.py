import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin

# スクレイピング対象のWebページのURLを指定
url = 'https://www.yahoo.co.jp'

# WebページのHTMLデータを取得
res = requests.get(url)

# BeautifulSoupを使用してHTMLデータを解析
soup = BeautifulSoup(res.text, 'html.parser')

for item in soup.find_all('a'):
    print(urljoin(url,item.get('href')))
