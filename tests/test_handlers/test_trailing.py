from unittest.mock import AsyncMock, MagicMock

import pytest

from kucoin_futures_lib.handlers import TrailingHandler


@pytest.mark.parametrize(
    "sl_price, mark_price, expected",
    [
        (100.0, 110.0, 10.0),
        (110.0, 90.0, 20.0),
        (110.0, 110.0, 0.0),
    ],
)
def test_calculate_distance(sl_price, mark_price, expected, mock_oco_handler):
    handler = TrailingHandler(
        instrument="XBTUSDTM",
        direction="buy",
        sl_order_id="sl1234567890",
        sl_order_price=sl_price,
        trailing_distance=10.0,
        update_order=AsyncMock(),
        trailing_step=1.0,
        oco_handler=mock_oco_handler,
    )
    assert handler._calculate_distance(mark_price=mark_price) == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "direction, sl_price, trailing_distance, mark_price, trailing_step, expected",
    [
        ("buy", 100.0, 10.0, 111.0, 0.0, 101.0),
        ("buy", 100.0, 10.0, 115.0, 1.0, 106.0),
        ("buy", 100.0, 10.0, 120.0, 5.0, 115.0),
        ("sell", 100.0, 10.0, 89.0, 0.0, 99.0),
        ("sell", 100.0, 10.0, 85.0, 1.0, 94.0),
        ("sell", 100.0, 10.0, 80.0, 5.0, 85.0),
    ],
)
async def test_handle_when_distance_is_greater_than_trailing_distance(
    direction,
    sl_price,
    trailing_distance,
    mark_price,
    trailing_step,
    expected,
    mock_oco_handler,
):
    update_order_mock = AsyncMock()
    mock_oco_handler.done.is_set.return_value = False

    handler = TrailingHandler(
        instrument="XBTUSDTM",
        direction=direction,
        sl_order_id="sl1234567890",
        sl_order_price=sl_price,
        trailing_distance=trailing_distance,
        update_order=update_order_mock,
        trailing_step=trailing_step,
        oco_handler=mock_oco_handler,
    )

    await handler.handle(
        {"subject": "mark.index.price", "data": {"markPrice": mark_price}}
    )
    update_order_mock.assert_called_once_with(expected)
    assert handler.sl_order_price == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "direction, sl_price, trailing_distance, mark_price, trailing_step",
    [
        ("buy", 100.0, 10.0, 109.0, 0.0),
        ("buy", 100.0, 10.0, 110.0, 0.0),
        ("sell", 100.0, 10.0, 91.0, 0.0),
        ("sell", 100.0, 10.0, 90.0, 0.0),
    ],
)
async def test_handle_when_distance_is_less_than_trailing_distance(
    direction, sl_price, trailing_distance, mark_price, trailing_step, mock_oco_handler
):
    update_order_mock = AsyncMock()

    handler = TrailingHandler(
        instrument="XBTUSDTM",
        direction=direction,
        sl_order_id="sl1234567890",
        sl_order_price=sl_price,
        trailing_distance=trailing_distance,
        update_order=update_order_mock,
        trailing_step=trailing_step,
        oco_handler=mock_oco_handler,
    )

    await handler.handle(
        {"subject": "mark.index.price", "data": {"markPrice": mark_price}}
    )
    update_order_mock.assert_not_called()


@pytest.mark.asyncio
async def test_handle_done_when_oco_handler_is_done(mock_oco_handler):
    update_order_mock = AsyncMock()
    mock_oco_handler.done.is_set.return_value = True

    handler = TrailingHandler(
        instrument="XBTUSDTM",
        direction="buy",
        sl_order_id="sl1234567890",
        sl_order_price=100.0,
        trailing_distance=10.0,
        update_order=update_order_mock,
        trailing_step=1.0,
        oco_handler=mock_oco_handler,
    )
    handler.calculate_new_price = MagicMock()

    await handler.handle({"subject": "mark.index.price", "data": {"markPrice": 120.0}})
    update_order_mock.assert_not_called()
    handler.calculate_new_price.assert_not_called()
    assert handler.done.is_set() is True
