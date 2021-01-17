"""Test codes."""

import requests
from bs4 import BeautifulSoup

from crawler.global_stock import (get_current_price, get_market_and_currency,
                                  get_stock_info)

VALID_TICKERS = ["005930.KS", "T", "035760.KQ", "INTC"]
VALID_MARKETS = ["KSE", "NYSE", "KOSDAQ", "NasdaqGS"]
VALID_CURRENCY = ["KRW", "USD", "KRW", "USD"]


class TestGlobalCrwaler:
    """Test global_stock.py module"""

    def setup_class(self):
        """"""
        self.urls = list()
        self.html_txts = list()
        for code in VALID_TICKERS:
            url = f"https://finance.yahoo.com/quote/{code}?p={code}&.tsrc=fin-srch"
            self.urls.append(url)
            self.html_txts.append(
                BeautifulSoup(requests.get(url).content, "html.parser")
            )

    def test_get_current_price(self):
        """Check the module get the current price of the stock.

        Notes:
            - The current price of the stock change almost everytime. So It
            just check the data type.
        """
        for html_txt in self.html_txts:
            cur_price = get_current_price(html_txt)
            assert isinstance(cur_price, float)
            assert cur_price > 0.0

    def test_get_market_and_currency(self):
        """Check the module get the exact market name and currency."""
        for idx, html_txt in enumerate(self.html_txts):
            market, currency = get_market_and_currency(html_txt)
            assert market == VALID_MARKETS[idx]
            assert currency == VALID_CURRENCY[idx]
