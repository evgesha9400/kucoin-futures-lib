import logging
from unittest.mock import patch

logger = logging.getLogger(__name__)

module = "kucoin_futures_lib.user"
user = f"{module}.User"


@patch(f"{user}.get_account_overview")
def test_get_balance(mock_get_account_overview, test_kucoinf):
    mock_get_account_overview.return_value = {
        "accountEquity": 99.8999305281,
        "unrealisedPNL": 0,
        "marginBalance": 99.8999305281,
        "positionMargin": 0,
        "orderMargin": 0,
        "frozenFunds": 0,
        "availableBalance": 99.8999305281,
        "currency": "USDT",
    }
    balance = test_kucoinf.user.get_balance()
    assert balance == 99.8999305281
