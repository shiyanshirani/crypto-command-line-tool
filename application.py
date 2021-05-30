# Dependencies
import argparse
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# Argparse description
parser = argparse.ArgumentParser(description="Enter Ticker To Receive Prices")
parser.add_argument('ticker', type=str)
args = parser.parse_args()
ticker = args.ticker.lower()

# Current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# URL for coindesk
url = 'https://www.coindesk.com/price/{}'.format(ticker)
r = requests.get(url)

# Beautified content
soup = BeautifulSoup(r.content, 'html.parser')

# Variables which needs to be extracted
price = soup.find('div', {'class': 'price-large'})
mediumChange = soup.find('div', {'class': 'percent-change-medium'})
mktCap = soup.find('div', {'class': 'price-medium'})

# Results to be displayed
print(current_time)
print('${} = {}, [24 Hour % Change] = {}, [MarketCap] = {}'.format(ticker.upper(),
                                                                   price.text, mediumChange.text, mktCap.text))
