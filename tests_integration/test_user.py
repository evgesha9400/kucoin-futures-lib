import json
import logging

logger = logging.getLogger(__name__)


def test_get_account_overview(kucoinf_real):
    account_overview = kucoinf_real.user.user.get_account_overview()
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
    }
    """
