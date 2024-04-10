from unittest.mock import AsyncMock

import pytest

from kucoin_futures_lib.handlers import OcoHandler


@pytest.mark.asyncio
async def test_handle_cancels_market_when_limit_is_done():
    # Arrange
    instrument = "XBTUSDTM"
    tp_order_id = "tp1234567890"
    sl_order_id = "sl1234567890"
    cancel_order_mock = AsyncMock()
    handler = OcoHandler(tp_order_id, sl_order_id, instrument, cancel_order_mock)

    # Act
    await handler.handle(
        {
            "data": {
                "orderId": tp_order_id,
                "status": "done",
            }
        }
    )

    # Assert
    cancel_order_mock.assert_called_once_with(sl_order_id)
    assert handler.done.is_set() is True


@pytest.mark.asyncio
async def test_handle_stops_when_market_order_is_filled():
    # Arrange
    instrument = "XBTUSDTM"
    tp_order_id = "tp1234567890"
    sl_order_id = "sl1234567890"
    cancel_order_mock = AsyncMock()
    handler = OcoHandler(tp_order_id, sl_order_id, instrument, cancel_order_mock)

    # Act
    await handler.handle(
        {
            "data": {
                "orderId": sl_order_id,
                "status": "done",
            }
        }
    )

    # Assert
    cancel_order_mock.assert_not_called()
    assert handler.done.is_set() is True
