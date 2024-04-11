import pytest

from kucoin_futures_lib.handlers.fill import FillHandler


@pytest.mark.asyncio
async def test_handle_fill_success():
    order_id = "1234567890"
    handler = FillHandler(order_id=order_id)
    await handler.handle(
        {
            "data": {
                "orderId": order_id,
                "type": "filled",
            }
        }
    )
    assert handler.done.is_set() is True


@pytest.mark.asyncio
async def test_handle_not_filled():
    order_id = "1234567890"
    handler = FillHandler(order_id=order_id)
    await handler.handle(
        {
            "data": {
                "orderId": order_id,
                "type": "not_filled",
            }
        }
    )
    assert handler.done.is_set() is False
