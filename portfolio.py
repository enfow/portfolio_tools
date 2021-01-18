"""Define portfolio class.

Author: kyeongmin.woo
Email: wgm0601@gmail.com
"""

from typing import Any, Dict, List, Tuple

from crawler.exchange_rate import exchange_from_usd_rate
from crawler.global_stock import get_stock_info


class Portfolio:
    """Portfolio."""

    def __init__(self) -> None:
        """Initialize."""
        self.asset: List[Dict[str, Any]] = []
        self.asset_2_krw: Dict[str, float] = dict()
        self.exchange_rate: Dict[str, float] = dict(
            KRW=1.0,
            USD=exchange_from_usd_rate("KRW"),
        )

    def update(self) -> None:
        """Update values for reporting."""
        for asset in self.asset:
            if asset["type"] == "stock":
                krw = self.exchange_to_krw(
                    currency=asset["currency"],
                    price=asset["cur_price"],
                    num=asset["num"],
                )
            elif asset["type"] == "cash":
                krw = self.exchange_to_krw(
                    currency=asset["currency"], price=1, num=asset["num"]
                )

            self.asset_2_krw[asset["name"]] = krw
        print(self.asset_2_krw)

    def exchange_to_krw(
        self,
        currency: str,
        price: float,
        num: float
    ) -> float:
        """Get current valuation of the global assets.

        Note:
            - If the asset type is cash, the price set to 1.
            - if currency is KRW, then get return value with rate 1.
        """
        exchange_rate = self.exchange_rate[currency]
        return round(price * num * exchange_rate, 2)

    def add_cash(self, currency: str, num: float) -> None:
        """Add cash information to self.asset."""
        self.asset.append(
            dict(
                type="cash",
                name="cash_{}".format(currency),
                currency=currency,
                num=num,
            )
        )

    def add_stock(self, name: str, code: str, num: int) -> None:
        """Add stock information to self.asset.

        Params:
            - name: stock name
            - code: stock code
            - num: the number of shares
        """
        cur_price, market, currency = get_stock_info(code)
        stock_info = dict(
            type="stock",
            name=name,
            code=code,
            currency=currency,
            market=market,
            cur_price=cur_price,
            num=num,
        )
        self.asset.append(stock_info)


if __name__ == "__main__":
    portfolio = Portfolio()
    asset_list: List[Tuple[str, str, int]] = [
        ("삼성전자", "005930.KS", 10),
        ("AT&T", "T", 10),
    ]
    for add in asset_list:
        portfolio.add_stock(*add)
    portfolio.update()
