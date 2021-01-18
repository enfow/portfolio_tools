"""Define portfolio class.

Author: kyeongmin.woo
Email: wgm0601@gmail.com
"""

from typing import Any, Dict, List, Tuple

from crawler.exchange_rate import exchange_from_usd_rate
from crawler.global_stock import get_stock_info

VALID_CURRENCY = {"KRW", "USD"}

class Portfolio:
    """Portfolio."""

    def __init__(self) -> None:
        """Initialize."""

        self.asset: Dict[str, Dict[str, Any]] = dict()
        self.asset_2_krw: Dict[str, float] = dict()
        self.currency_2_krw: Dict[str, float] = dict()
        self.total_krw: float = 0.
        self.exchange_rate: Dict[str, float] = dict()
        self.is_updated = False

        self.reset()

    def reset(self) -> None:
        """Reset all values."""
        self.asset = dict()
        self.asset_2_krw = dict()
        self.currency_2_krw = { currency : 0.0 for currency in VALID_CURRENCY}
        self.total_krw = 0.
        self.exchange_rate: Dict[str, float] = dict(
            KRW=1.0,
            USD=exchange_from_usd_rate("KRW"),
        )
        self.is_updated = False

    def update(self) -> None:
        """Update values for reporting."""
        if self.is_updated:
            print("It updates again without reset")
        self.is_updated = True
        self.total_krw = 0.
        for name, asset in self.asset.items():
            if asset["type"] == "stock":
                krw = self.exchange_to_krw(
                    currency=asset["currency"],
                    price=asset["cur_price"],
                    num=asset["num"],
                )
            elif asset["type"] == "cash":
                krw = self.exchange_to_krw(
                    currency=asset["currency"], 
                    price=1, 
                    num=asset["num"]
                )

            self.asset_2_krw[name] = round(krw, 2)
            self.currency_2_krw[asset["currency"]] += round(krw, 2)
            self.total_krw += krw
        self.totla_krw = round(self.total_krw, 2)

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
        name = "cash_{}".format(currency)
        self.asset[name] = dict(
                type="cash",
                currency=currency,
                num=num,
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
            code=code,
            currency=currency,
            market=market,
            cur_price=cur_price,
            num=num,
        )
        self.asset[name] = stock_info


if __name__ == "__main__":
    portfolio = Portfolio()
    asset_list: List[Tuple[str, str, int]] = [
        ("삼성전자", "005930.KS", 10),
        ("AT&T", "T", 10),
    ]
    for add in asset_list:
        portfolio.add_stock(*add)
    portfolio.update()
    print(portfolio.asset_2_krw)
    print(portfolio.total_krw)
