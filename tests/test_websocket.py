import asyncio
import logging
from unittest.mock import AsyncMock

import pytest

from kucoin_futures_lib.handlers import HandlerABC
from kucoin_futures_lib.websocket import KucoinFuturesWebsocket

logger = logging.getLogger(__name__)

module = "kucoin_futures_lib.websocket"


@pytest.mark.asyncio
async def test_subscribe_success(mock_ws_client):
    # Arrange
    mock_handler = AsyncMock(spec=HandlerABC)
    future = asyncio.Future()
    future.set_result(None)
    mock_handler.done.wait.return_value = future

    websocket = KucoinFuturesWebsocket(token=AsyncMock())

    # Act
    await websocket.subscribe(mock_handler)

    # Assert
    mock_ws_client.create.assert_called_once_with(
        loop=None,
        client=websocket.token,
        callback=mock_handler.handle,
        private=mock_handler.private,
    )
    mock_ws_client.subscribe.assert_called_once_with(mock_handler.topic)
    mock_ws_client.unsubscribe.assert_called_once_with(mock_handler.topic)


@pytest.mark.asyncio
async def test_subscribe_timeout(mock_ws_client):
    # Arrange
    mock_handler = AsyncMock(spec=HandlerABC)
    future = asyncio.Future()
    # future.set_result(None)
    mock_handler.done.wait.return_value = future

    websocket = KucoinFuturesWebsocket(token=AsyncMock())

    # Act
    with pytest.raises(asyncio.TimeoutError, match="Timeout reached for"):
        await websocket.subscribe(mock_handler, timeout=0.001)

    # Assert
    mock_ws_client.create.assert_called_once_with(
        loop=None,
        client=websocket.token,
        callback=mock_handler.handle,
        private=mock_handler.private,
    )
    mock_ws_client.subscribe.assert_called_once_with(mock_handler.topic)
    mock_ws_client.unsubscribe.assert_called_once_with(mock_handler.topic)


@pytest.mark.asyncio
async def test_tp_sl_cancel(mock_oco_handler, mock_ws_client, test_kucoinf):
    instrument = "XBTUSDTM"
    tp_order_id = "tp987654321"
    sl_order_id = "sl123456789"

    await test_kucoinf.websocket.tp_sl_cancel(
        instrument=instrument,
        tp_order_id=tp_order_id,
        sl_order_id=sl_order_id,
        cancel_order=test_kucoinf.trade.cancel_order,
    )
    mock_oco_handler.assert_called_once_with(
        instrument=instrument,
        limit_order_id=tp_order_id,
        market_order_id=sl_order_id,
        cancel_order=test_kucoinf.trade.cancel_order,
    )
    mock_ws_client.subscribe.assert_called_once_with(mock_oco_handler.topic)
    mock_ws_client.unsubscribe.assert_called_once_with(mock_oco_handler.topic)


@pytest.mark.asyncio
async def test_listen_for_entry(mock_entry_range_handler, mock_ws_client, test_kucoinf):
    entry_high = 50000
    entry_low = 40000
    instrument = "XBTUSDTM"

    await test_kucoinf.websocket.listen_for_entry(
        instrument=instrument, entry_high=entry_high, entry_low=entry_low, timeout=0.2
    )
    mock_entry_range_handler.assert_called_once_with(
        instrument=instrument, entry_high=entry_high, entry_low=entry_low
    )
    mock_ws_client.subscribe.assert_called_once_with(mock_entry_range_handler.topic)
    mock_ws_client.unsubscribe.assert_called_once_with(mock_entry_range_handler.topic)
