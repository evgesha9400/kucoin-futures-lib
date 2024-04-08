import json
import logging

logger = logging.getLogger(__name__)


def test_get_account_overview(kucoinf_real):
    account_overview = kucoinf_real.user.client.get_account_overview("USDT")
    logger.info(f"account_overview:\n{json.dumps(account_overview, indent=4)}")
    """
    {
        "accountEquity": 0,
        "unrealisedPNL": 0,
        "marginBalance": 0,
        "positionMargin": 0,
        "orderMargin": 0,
        "frozenFunds": 0,
        "availableBalance": 0,
        "currency": "XBT"
    },    
    {
        "accountEquity": 123.0260554198,
        "unrealisedPNL": -0.2773,
        "marginBalance": 123.3033554198,
        "positionMargin": 71.7774747,
        "orderMargin": 0.0,
        "frozenFunds": 0.0,
        "availableBalance": 51.2485807198,
        "currency": "USDT"
    }
    """
