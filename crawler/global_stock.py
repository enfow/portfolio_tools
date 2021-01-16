"""Get global stock information.

Author: kyeongmin.woo
Email: wgm0601@gmail.com

Notes:
    - this module request data to yahoo finance. If Yahoo's policy is
    changed, it may not work.
"""

import requests
from bs4 import BeautifulSoup


def get_stock_info(code: str) -> str:
    """Get stock information from naver."""
    url = f"https://finance.yahoo.com/quote/{code}?p={code}&.tsrc=fin-srch"
    html_txt = BeautifulSoup(requests.get(url).content, "html.parser")
    cur_price = get_current_price(html_txt)
    return cur_price


def get_current_price(html_txt: BeautifulSoup) -> str:
    """Get current price."""
    shell = html_txt.find("div", {"id": "mrt-node-Lead-3-QuoteHeader"})
    shell = shell.find("span", {
        "class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"
    })
    return shell.text


if __name__ == "__main__":
    result = get_stock_info(code="005930.KS")
    print(result)
    result = get_stock_info(code="T")
    print(result)
