import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XVLMZHH/ref=sr_1_1_sspa?crid=5PT2FDKBKLCF&dchild=1&keywords=iphone+11+pro+max+512gb&qid=1595686772&sprefix=iphone%2Caps%2C357&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVVBDQ0dZRDNRM0dHJmVuY3J5cHRlZElkPUEwNjA2ODU1Mk8yUzRFTE0wRjdKTSZlbmNyeXB0ZWRBZElkPUEwODU2OTc1M0pQWkZWS0lDUVg0TSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = (price[0:7])
print(title.strip())
print(price)