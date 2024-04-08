from unittest.mock import MagicMock

import pytest

module = "kucoin_futures_lib.kucoinf"
futures = f"{module}.KucoinFutures"
trade = f"{module}.KucoinFuturesTrade"
websocket = f"{module}.KucoinFuturesWebsocket"


@pytest.mark.asyncio
async def test_create_order(mock_kucoinf):
    mock_kucoinf.trade.create_order.return_value = "e12345689"

    order_ids = MagicMock(spec=f"{trade}.TpSlOrderIds")
    order_ids.tp_order_id = "tp12345689"
    order_ids.sl_order_id = "sl12345689"

    mock_kucoinf.trade.create_stop_loss_and_take_profit.return_value = order_ids

    entry_order_id = await mock_kucoinf.create_order(
        instrument="XBTUSDTM",
        side="buy",
        size=2,
        take_profit=70000,
        stop_loss=65000,
        leverage=2,
        enable_oco=True,
    )

    mock_kucoinf.trade.create_order.assert_called_once_with(
        instrument="XBTUSDTM",
        side="buy",
        size=2,
        price=None,
        leverage=2,
    )
    mock_kucoinf.trade.poll_for_fill.assert_called_once_with(order_id="e12345689")

    mock_kucoinf.trade.create_stop_loss_and_take_profit.assert_called_once_with(
        instrument="XBTUSDTM",
        side="buy",
        take_profit=70000,
        stop_loss=65000,
        take_profit_type="limit",
        stop_loss_type="stop",
    )

    mock_kucoinf.websocket.tp_sl_cancel.assert_called_once_with(
        sl_order_id="sl12345689",
        tp_order_id="tp12345689",
        instrument="XBTUSDTM",
        cancel_order=mock_kucoinf.trade.cancel_order,
    )
    assert entry_order_id == "e12345689"
