"""Define portfolio class.

Author: kyeongmin.woo
Email: wgm0601@gmail.com
"""

from typing import Any, Dict, List

from crawler.korea_stock import get_stock_info


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
    portfolio.add_stock(
        name="삼성전자",
        code="005930",
        nation="korea",
        purchase_price=42800,
        num=10,
    )
    print(portfolio.stock)
