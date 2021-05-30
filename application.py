import requests
from datetime import datetime
from bs4 import BeautifulSoup

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

url = 'https://www.coindesk.com/price/bitcoin'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

price = soup.find('div', {'class': 'price-large'})
mediumChange = soup.find('div', {'class': 'percent-change-medium'})
mktCap = soup.find('div', {'class': 'price-medium'})

print(current_time)
print('$BTC = {}, [24 Hour % Change] = {}, [MarketCap] = {}'.format(
    price.text, mediumChange.text, mktCap.text))
