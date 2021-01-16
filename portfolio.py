"""Define portfolio class.

Author: kyeongmin.woo
Email: wgm0601@gmail.com
"""

from typing import Any, Dict, List, Tuple

from crawler.global_stock import get_stock_info


class Portfolio:
    """Portfolio."""

    def __init__(self) -> None:
        """Initialize."""
        self.stock: List[Dict[str, Any]] = []

    def add_stock(
        self, name: str, code: str, nation: str, purchase_price: int, num: int
    ) -> None:
        """Add single stock.

        Params:
            - name: stock name
            - code: stock code
            - nation: currency, (korea, usa)
            - purchase_price: purchase price
            - num: number of stocks
        """
        cur_price = get_stock_info(code)
        self.stock.append(
            dict(
                name=name,
                code=code,
                nation=nation,
                purchase_price=purchase_price,
                current_price=cur_price,
                num=num,
            )
        )


if __name__ == "__main__":
    portfolio = Portfolio()
    asset_list: List[Tuple[str, str, str, int, int]] = [
        ("삼성전자", "005930.KS", "korea", 42800, 10),
        ("AT&T", "T", "us", 29, 10)
    ]
    for asset in asset_list:
        portfolio.add_stock(*asset)
    print(portfolio.stock)
