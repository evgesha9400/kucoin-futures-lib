import logging
from unittest.mock import MagicMock

import pytest
from kucoin_futures.ws_client import KucoinFuturesWsClient

from kucoin_futures_lib.factory import initialize_kucoinf
from kucoin_futures_lib.handlers import OcoHandler
from kucoin_futures_lib.kucoinf import (
    KucoinFuturesUser,
    KucoinFuturesTrade,
    KucoinFuturesMarket,
    KucoinFuturesWebsocket,
    KucoinFutures,
)

logging.basicConfig(level=logging.INFO)


@pytest.fixture
def mock_kucoinf_user():
    """Return a mock KucoinFuturesUser."""
    return MagicMock(spec=KucoinFuturesUser)


@pytest.fixture
def mock_kucoinf_market():
    """Return a mock KucoinFuturesMarket."""
    return MagicMock(spec=KucoinFuturesMarket)


@pytest.fixture
def mock_kucoinf_trade():
    """Return a mock KucoinFuturesTrade."""
    return MagicMock(spec=KucoinFuturesTrade)


@pytest.fixture
def mock_kucoinf_websocket():
    """Return a mock KucoinFuturesWebsocket."""
    return MagicMock(spec=KucoinFuturesWebsocket)


@pytest.fixture
def mock_oco_handler():
    """Return a mock OCOHandler."""
    return MagicMock(spec=OcoHandler)


@pytest.fixture
def mock_kucoinf(
    mock_kucoinf_user, mock_kucoinf_trade, mock_kucoinf_market, mock_kucoinf_websocket
):
    """Return a mock KucoinFutures client."""
    return KucoinFutures(
        user=mock_kucoinf_user,
        trade=mock_kucoinf_trade,
        market=mock_kucoinf_market,
        websocket=mock_kucoinf_websocket,
    )


@pytest.fixture
def mock_ws_client():
    """Return a mock KucoinFuturesWsClient."""
    return MagicMock(spec=KucoinFuturesWsClient)



@pytest.fixture
def test_kucoinf():
    return initialize_kucoinf(
        api_passphrase="test_api_key",
        api_key="test_secret_key",
        api_secret="test_passphrase",
    )

