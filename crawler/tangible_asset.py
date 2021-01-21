"""Get tangible assets' price information.

Author: kyeongmin.woo
Email: wgm0601@gmail.com

Notes:
    - this module request data to naver finance. If Naver's policy is
    changed, it may not work.
"""
import requests
from bs4 import BeautifulSoup


def get_korea_gold_price() -> float:
    """Get korea current gold price per gram from Naver finance.

    Returns:
        - current korea gold price(float)
    """
    url = "https://finance.naver.com/marketindex/goldDetail.nhn"
    html_txt = BeautifulSoup(requests.get(url).content, "html.parser")
    shell = html_txt.find("table", {"class": "tbl_exchange market"})
    price = float(shell.find("td").text[:-1].replace(",", ""))
    return price

if __name__ == "__main__":
    kr_gold = get_korea_gold_price()
    print(kr_gold)
