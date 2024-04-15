import logging

logger = logging.getLogger(__name__)


def test_get_balance(test_kucoinf):
    test_kucoinf.user.client.get_account_overview.return_value = {
        "accountEquity": 199.8999305281,
        "unrealisedPNL": 0,
        "marginBalance": 199.8999305281,
        "positionMargin": 0,
        "orderMargin": 0,
        "frozenFunds": 0,
        "availableBalance": 99.8999305281,
        "currency": "USDT",
    }
    balance = test_kucoinf.user.get_balance()
    assert balance == 99.8999305281
