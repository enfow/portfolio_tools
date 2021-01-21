"""Test codes for tangible assets.

Tangible assets:
    - Korea Gold
"""

import requests
from bs4 import BeautifulSoup

from crawler.tangible_asset import get_korea_gold_price


class TestTangibleAssetCrwaler:
    """Test tangible_asset.py module"""

    def test_get_korea_gold_price(self):
        """Check tangible_asset.get_korea_gold_price() is work correctly."""
        cur_price = get_korea_gold_price()
        assert isinstance(cur_price, float)
        assert cur_price > 0.0
