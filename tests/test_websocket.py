import asyncio
import logging
from unittest.mock import AsyncMock, patch

import pytest

from kucoin_futures_lib.handlers import HandlerABC
from kucoin_futures_lib.websocket import KucoinFuturesWebsocket

logger = logging.getLogger(__name__)

module = "kucoin_futures_lib.websocket"


@pytest.mark.asyncio
@patch(f"{module}.KucoinFuturesWsClient.create")
async def test_subscribe_success(mock_create):
    # Arrange
    mock_handler = AsyncMock(spec=HandlerABC)
    future = asyncio.Future()
    future.set_result(None)
    mock_handler.done.wait.return_value = future

    mock_ws_client = AsyncMock()
    mock_create.return_value = mock_ws_client
    websocket = KucoinFuturesWebsocket(token=AsyncMock())

    # Act
    await websocket.subscribe(mock_handler)

    # Assert
    mock_create.assert_called_once_with(
        loop=None,
        client=websocket.token,
        callback=mock_handler.handle,
        private=mock_handler.private,
    )
    mock_ws_client.subscribe.assert_called_once_with(mock_handler.topic)
    mock_ws_client.unsubscribe.assert_called_once_with(mock_handler.topic)


@pytest.mark.asyncio
@patch(f"{module}.KucoinFuturesWsClient.create")
async def test_subscribe_timeout(mock_create):
    # Arrange
    mock_handler = AsyncMock(spec=HandlerABC)
    future = asyncio.Future()
    # future.set_result(None)
    mock_handler.done.wait.return_value = future

    mock_ws_client = AsyncMock()
    mock_create.return_value = mock_ws_client
    websocket = KucoinFuturesWebsocket(token=AsyncMock())

    # Act
    with pytest.raises(asyncio.TimeoutError, match="Timeout reached for"):
        await websocket.subscribe(mock_handler, timeout=0.001)

    # Assert
    mock_create.assert_called_once_with(
        loop=None,
        client=websocket.token,
        callback=mock_handler.handle,
        private=mock_handler.private,
    )
    mock_ws_client.subscribe.assert_called_once_with(mock_handler.topic)
    mock_ws_client.unsubscribe.assert_called_once_with(mock_handler.topic)


@pytest.mark.asyncio
@patch(f"{module}.OcoHandler", autospec=True)
@patch(f"{module}.KucoinFuturesWebsocket.subscribe", new_callable=AsyncMock)
async def test_tp_sl_cancel(mock_subscribe, mock_oco_handler, test_kucoinf):
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
    mock_subscribe.assert_called_once_with(mock_oco_handler.return_value, None)


@pytest.mark.asyncio
@patch(f"{module}.EntryRangeHandler", autospec=True)
@patch(f"{module}.KucoinFuturesWebsocket.subscribe", new_callable=AsyncMock)
async def test_listen_for_entry(mock_subscribe, mock_entry_handler, test_kucoinf):
    entry_high = 50000
    entry_low = 40000
    instrument = "XBTUSDTM"

    await test_kucoinf.websocket.listen_for_entry(
        instrument=instrument, entry_high=entry_high, entry_low=entry_low, timeout=0.2
    )
    mock_entry_handler.assert_called_once_with(
        instrument=instrument, entry_high=entry_high, entry_low=entry_low
    )
    mock_subscribe.assert_called_once_with(mock_entry_handler.return_value, 0.2)
