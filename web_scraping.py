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

link_list = []
for item in soup.find_all('a'):
    href = urljoin(url, item.get('href'))
    if href.endswith(('.doc','.docx','.zip','lzh','.7z','rar','html')):
        link_list.append(href)

print(link_list)
