import logging
from unittest.mock import MagicMock, patch, AsyncMock

import pytest

from kucoin_futures_lib.factory import initialize_kucoinf
from kucoin_futures_lib.kucoinf import (
    KucoinFuturesUser,
    KucoinFuturesTrade,
    KucoinFuturesMarket,
    KucoinFuturesWebsocket,
    KucoinFutures,
)
from kucoin_futures_lib.utils import retriable


logging.basicConfig(level=logging.INFO)


@pytest.fixture
def mock_user_client():
    """Return a mock User client."""
    with patch("kucoin_futures_lib.user.User", autospec=True) as mock_user:
        yield mock_user


@pytest.fixture
def mock_trade_client():
    """Return a mock Trade client."""
    with patch("kucoin_futures_lib.trade.Trade", autospec=True) as mock_trade:
        yield mock_trade


@pytest.fixture
def mock_market_client():
    """Return a mock Market client."""
    with patch("kucoin_futures_lib.market.Market", autospec=True) as mock_market:
        yield mock_market


@pytest.fixture
def mock_ws_client():
    """Return a mock KucoinFuturesWsClient."""
    with patch(
        "kucoin_futures_lib.websocket.KucoinFuturesWsClient", autospec=True
    ) as mock_ws:
        mock_ws.create.return_value = mock_ws
        yield mock_ws


@pytest.fixture
def mock_ws_token():
    """Return a mock WsToken."""
    with patch("kucoin_futures_lib.websocket.WsToken", autospec=True) as mock_ws_token:
        yield mock_ws_token


@pytest.fixture
def mock_oco_handler():
    """Return a mock OCOHandler."""
    with patch("kucoin_futures_lib.websocket.OcoHandler", autospec=True) as mock_oco:
        mock_oco.return_value = mock_oco
        yield mock_oco


@pytest.fixture
def mock_entry_range_handler():
    """Return a mock EntryRangeHandler."""
    with patch(
        "kucoin_futures_lib.websocket.EntryRangeHandler", autospec=True
    ) as mock_entry_range:
        mock_entry_range.return_value = mock_entry_range
        yield mock_entry_range


@pytest.fixture
def mock_message_handler():
    """Return a mock FillHandler."""
    with patch(
        "kucoin_futures_lib.websocket.MessageHandler", autospec=True
    ) as mock_message:
        mock_message.return_value = mock_message
        yield mock_message


@pytest.fixture
def mock_kucoinf():
    """Return a mock KucoinFutures client."""
    return KucoinFutures(
        user=MagicMock(spec=KucoinFuturesUser),
        trade=MagicMock(spec=KucoinFuturesTrade),
        market=MagicMock(spec=KucoinFuturesMarket),
        websocket=MagicMock(spec=KucoinFuturesWebsocket),
    )


@pytest.fixture
def test_kucoinf(
    mock_user_client, mock_trade_client, mock_market_client, mock_ws_token
):
    kucoinf = initialize_kucoinf(
        api_passphrase="test_api_key",
        api_key="test_secret_key",
        api_secret="test_passphrase",
        retriable=retriable(retries=3, exceptions=(Exception,), backoff_base=2.0, initial_backoff=0.01),
    )
    kucoinf.user.client = mock_user_client
    kucoinf.trade.client = mock_trade_client
    kucoinf.market.client = mock_market_client
    kucoinf.websocket.token = mock_ws_token
    return kucoinf
