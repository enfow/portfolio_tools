"""Get exchange rate information.

Author: kyeongmin.woo
Email: wgm0601@gmail.com

Notes:
    - this module request data to yahoo finance. If Yahoo's policy is
    changed, it may not work.
"""
import requests
from bs4 import BeautifulSoup


def exchange_from_usd_rate(code: str) -> float:
    """Get current exchange rate.

    Returns:
        - current exchange rate(float)
    """
    url = f"https://finance.yahoo.com/quote/{code}=X?p={code}=X&.tsrc=fin-srch"
    html_txt = BeautifulSoup(requests.get(url).content, "html.parser")
    shell = html_txt.find("div", {"id": "mrt-node-Lead-3-QuoteHeader"})
    shell = shell.find("span", {"data-reactid": "32"})
    rate = float(shell.text.replace(",", ""))

    return rate


if __name__ == "__main__":
    cur_exchange = exchange_from_usd_rate("KRW")
    print(cur_exchange)
