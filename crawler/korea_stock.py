"""Get korea stock information.

Author: kyeongmin.woo
Email: wgm0601@gmail.com

Notes:
    - this module request data to naver finance. If Naver's policy is
    changed, it may not work.
"""

import requests
from bs4 import BeautifulSoup


def get_stock_info(code: str) -> str:
    """Get stock information from naver."""
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html_txt = BeautifulSoup(requests.get(url).content, "html.parser")
    cur_price = get_current_price(html_txt)
    return cur_price


def get_current_price(html_txt: BeautifulSoup) -> str:
    """Get current price."""
    shell = html_txt.find("p", {"class": "no_today"})
    shell = shell.find("span", {"class": "blind"})
    return shell.text


if __name__ == "__main__":
    result = get_stock_info(code="005930")
    print(result)
