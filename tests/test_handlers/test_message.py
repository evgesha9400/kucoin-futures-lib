from unittest.mock import AsyncMock

import pytest

from kucoin_futures_lib.handlers import MessageHandler


@pytest.mark.asyncio
async def test_handle_message_received():
    order_id = "1234567890"
    handler = MessageHandler(order_id=order_id, message_type=["filled", "canceled"])
    await handler.handle(
        {
            "data": {
                "orderId": order_id,
                "type": "filled",
            }
        }
    )
    assert handler.done.is_set() is True
    assert handler.received_message == "filled"


@pytest.mark.asyncio
async def test_handle_not_received():
    order_id = "1234567890"
    mock_callback = AsyncMock()
    handler = MessageHandler(order_id=order_id, message_type=["filled", "canceled"])
    await handler.handle(
        {
            "data": {
                "orderId": order_id,
                "type": "match",
            }
        }
    )
    assert handler.done.is_set() is False
    mock_callback.assert_not_called()
    assert handler.received_message is None
