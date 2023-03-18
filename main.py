import argparse
from datetime import datetime
from typing import Tuple

import requests
from bs4 import BeautifulSoup

URL_LINK = "https://www.coindesk.com/price"


def main(ticker: str | None) -> Tuple:
    url = "{0}/{1}".format(URL_LINK, ticker)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    price = soup.find(
        "span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 jIzQOt"}
    )
    medium_change = soup.find(
        "h6", {"class": "typography__StyledTypography-owin6q-0 hZxwDe"}
    )
    return price, medium_change


def display_data(ticker: str, price, medium_change) -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(
        "{}:INFO: ${} = {}, [24 Hour % Change] = {}".format(
            current_time, ticker.upper(), price.text, medium_change.text
        )
    )


if __name__ == "__main__":
    import sys

    ticker = str(sys.argv[1].lower())
    price, medium_change = main(ticker)
    display_data(ticker, price, medium_change)
