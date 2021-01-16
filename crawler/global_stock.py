"""Get global stock information.

Author: kyeongmin.woo
Email: wgm0601@gmail.com

Notes:
    - this module request data to yahoo finance. If Yahoo's policy is
    changed, it may not work.
"""

from typing import Tuple

import requests
from bs4 import BeautifulSoup


def get_stock_info(code: str) -> Tuple[float, str, str]:
    """Get stock information from naver.

    Returns:
        - current price(str)
        - market(str) - NYSE, KOSPI etc
        - currency(str) - USD, KRW
    """
    url = f"https://finance.yahoo.com/quote/{code}?p={code}&.tsrc=fin-srch"
    html_txt = BeautifulSoup(requests.get(url).content, "html.parser")
    cur_price = get_current_price(html_txt)
    market, currency = get_market_and_currency(html_txt)

    return cur_price, market, currency


def get_current_price(html_txt: BeautifulSoup) -> float:
    """Get current price.

    Returns:
        - current price(str)
    """
    shell = html_txt.find("div", {"id": "mrt-node-Lead-3-QuoteHeader"})
    shell = shell.find("span", {"data-reactid": "32"})
    cur_price = float(shell.text.replace(",", ""))
    return cur_price


def get_market_and_currency(html_txt: BeautifulSoup) -> Tuple[str, str]:
    """Get current price.

    Returns:
        - market name(str)
        - currency price(str)
    """
    shell = html_txt.find("div", {"id": "mrt-node-Lead-3-QuoteHeader"})
    shell = shell.find("span", {"data-reactid": "9"})
    shell_words = shell.text.split(" ")
    market, currency = shell_words[0], shell_words[-1]
    return market, currency


if __name__ == "__main__":
    result = get_stock_info(code="005930.KS")
    print(result)
    result = get_stock_info(code="T")
    print(result)
