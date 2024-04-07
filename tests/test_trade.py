import logging
from unittest.mock import patch

import pytest

logger = logging.getLogger(__name__)

module = "kucoin_futures_lib.trade"
trade = f"{module}.Trade"


@patch(f"{trade}.get_order_list")
def test_get_open_orders(mock_get_order_list, test_kucoinf):
    xbtusdtm_order = {
        "id": "162367525139533826",
        "symbol": "XBTUSDTM",
        "type": "limit",
        "side": "buy",
        "price": "69653.9",
        "size": 1,
        "value": "69.6539",
        "dealValue": "69.6539",
        "dealSize": 1,
        "stp": "",
        "stop": "",
        "stopPriceType": "",
        "stopTriggered": False,
        "stopPrice": None,
        "timeInForce": "GTC",
        "postOnly": False,
        "hidden": False,
        "iceberg": False,
        "leverage": "1",
        "forceHold": False,
        "closeOrder": True,
        "visibleSize": 0,
        "clientOid": "e73f6586ec0b11ee98480a58a9feac02",
        "remark": None,
        "tags": "",
        "isActive": False,
        "cancelExist": False,
        "createdAt": 1711524636636,
        "updatedAt": 1711529760958,
        "endAt": 1711529760958,
        "orderTime": 1711524636636773006,
        "settleCurrency": "USDT",
        "filledSize": 1,
        "filledValue": "69.6539",
        "status": "done",
        "reduceOnly": True,
    }
    xrpusdtm_order = {
        "id": "161585261925412864",
        "symbol": "XRPUSDTM",
        "type": "market",
        "side": "buy",
        "price": "0",
        "size": 1,
        "value": "6.325",
        "dealValue": "6.325",
        "dealSize": 1,
        "stp": "",
        "stop": "",
        "stopPriceType": "",
        "stopTriggered": False,
        "stopPrice": None,
        "timeInForce": "GTC",
        "postOnly": False,
        "hidden": False,
        "iceberg": False,
        "leverage": "1",
        "forceHold": False,
        "closeOrder": True,
        "visibleSize": 0,
        "clientOid": "",
        "remark": None,
        "tags": "",
        "isActive": False,
        "cancelExist": False,
        "createdAt": 1711338130551,
        "updatedAt": 1711338130559,
        "endAt": 1711338130559,
        "orderTime": 1711338130551710991,
        "settleCurrency": "USDT",
        "filledSize": 1,
        "filledValue": "6.325",
        "status": "done",
        "reduceOnly": True,
    }
    mock_get_order_list.return_value = {
        "currentPage": 1,
        "pageSize": 50,
        "totalNum": 139,
        "totalPage": 3,
        "items": [xbtusdtm_order, xrpusdtm_order],
    }
    orders = test_kucoinf.trade.get_open_orders("XBTUSDTM")
    assert len(orders) == 1
    assert orders[0] == xbtusdtm_order


@patch(f"{trade}.create_market_order")
def test_create_market_order(mock_create_market_order, test_kucoinf):
    mock_create_market_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_market_order(
        instrument="XBTUSDTM",
        side="buy",
        size=1,
        leverage=100,
    )
    mock_create_market_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="buy",
        size="1",
        lever="100",
    )
    assert order_id == "12345689"


@patch(f"{trade}.create_limit_order")
def test_create_limit_order(mock_create_limit_order, test_kucoinf):
    mock_create_limit_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_limit_order(
        instrument="XBTUSDTM",
        side="buy",
        size=1,
        price=1000.001,
        leverage=100,
    )
    mock_create_limit_order.assert_called_once_with(
        symbol="XBTUSDTM", side="buy", size="1", price="1000.001", lever="100"
    )
    assert order_id == "12345689"


@patch(f"{trade}.create_limit_order")
def test_create_take_profit_limit(mock_create_limit_order, test_kucoinf):
    mock_create_limit_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_take_profit_limit(
        instrument="XBTUSDTM",
        entry_side="buy",
        tp_price=1000,
    )
    mock_create_limit_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        price="1000",
        timeInForce="GTC",
        closeOrder=True,
        lever=None,
        size=None,
    )
    assert order_id == "12345689"


@patch(f"{trade}.create_market_order")
def test_create_take_profit_stop(mock_create_market_order, test_kucoinf):
    mock_create_market_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_take_profit_stop(
        instrument="XBTUSDTM",
        entry_side="buy",
        tp_price=1000,
    )
    mock_create_market_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        stop="up",
        stopPrice="1000",
        timeInForce="GTC",
        stopPriceType="TP",
        closeOrder=True,
        lever=None,
        size=None,
    )
    assert order_id == "12345689"


@patch(f"{trade}.create_market_order")
def test_create_stop_loss_stop(mock_create_market_order, test_kucoinf):
    mock_create_market_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_stop_loss_stop(
        instrument="XBTUSDTM",
        entry_side="buy",
        sl_price=1000,
    )
    mock_create_market_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        stop="down",
        stopPriceType="TP",
        stopPrice="1000",
        timeInForce="GTC",
        closeOrder=True,
        lever=None,
    )
    assert order_id == "12345689"


@patch(f"{trade}.create_limit_order")
def test_create_stop_loss_limit(mock_create_limit_order, test_kucoinf):
    mock_create_limit_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_stop_loss_limit(
        instrument="XBTUSDTM",
        entry_side="buy",
        sl_price=1000,
    )
    mock_create_limit_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        stop="down",
        stopPriceType="TP",
        price="1000",
        stopPrice="1000",
        timeInForce="GTC",
        closeOrder=True,
        size=None,
        lever=None,
    )
    assert order_id == "12345689"


@pytest.mark.asyncio
@patch(f"{trade}.get_recent_fills")
async def test_poll_for_fill_filled(mock_get_recent_fills, test_kucoinf):
    test_fill = {
        "symbol": "XBTUSDTM",
        "orderId": "12345689",
        "price": "68804.3",
        "size": 1,
        "side": "sell",
        "ts": 1711569300284000000,
    }
    mock_get_recent_fills.return_value = [test_fill]
    response = await test_kucoinf.trade.poll_for_fill(order_id="12345689")
    assert response == test_fill


@pytest.mark.asyncio
@patch(f"{trade}.get_recent_fills")
async def test_poll_for_fill_multiple_attempts(mock_get_recent_fills, test_kucoinf):
    test_fill1 = {
        "symbol": "XBTUSDM",
        "orderId": "987654321",
        "price": "68804.3",
        "size": 1,
        "side": "sell",
        "ts": 1711569300284000000,
    }
    test_fill2 = {
        "symbol": "XBTUSDTM",
        "orderId": "12345689",
        "price": "68804.3",
        "size": 1,
        "side": "sell",
        "ts": 1711569300284000000,
    }
    mock_get_recent_fills.side_effect = [
        [],
        [test_fill1],
        [test_fill1, test_fill2],
    ]
    response = await test_kucoinf.trade.poll_for_fill(
        order_id="12345689", interval=0.01, max_attempts=3
    )
    assert response == test_fill2


@pytest.mark.asyncio
@patch(f"{trade}.get_recent_fills")
async def test_poll_for_fill_unexpected(mock_get_recent_fills, test_kucoinf):
    mock_get_recent_fills.return_value = {"code": "200000", "data": []}
    with pytest.raises(
        TimeoutError, match="Order 12345689 was not filled within the timeout period"
    ):
        await test_kucoinf.trade.poll_for_fill(
            order_id="12345689", max_attempts=1, interval=0.01
        )


@patch(f"{trade}.cancel_order")
def test_cancel_order(mock_cancel_order, test_kucoinf):
    order_id = "12345689"
    test_kucoinf.trade.cancel_order(order_id)
    mock_cancel_order.assert_called_once_with(orderId=order_id)


@pytest.mark.asyncio
@patch(f"{trade}.get_order_details")
async def test_poll_for_done_with_done_status(mock_get_order_details, test_kucoinf):
    mock_get_order_details.return_value = {"status": "done", "orderId": "order1"}
    result = await test_kucoinf.trade.poll_for_done(order_id="order1", max_attempts=1)
    assert result["status"] == "done"


@pytest.mark.asyncio
@patch(f"{trade}.get_order_details")
async def test_poll_for_done_with_not_done_status(mock_get_order_details, test_kucoinf):
    mock_get_order_details.return_value = {"status": "not_done", "orderId": "order1"}
    with pytest.raises(TimeoutError):
        await test_kucoinf.trade.poll_for_done(
            order_id="order1", interval=0.01, max_attempts=1
        )


@pytest.mark.asyncio
@patch(f"{trade}.get_order_details")
async def test_poll_for_done_with_changing_status(mock_get_order_details, test_kucoinf):
    mock_get_order_details.side_effect = [
        {"status": "not_done"},
        {"status": "not_done"},
        {"status": "not_done"},
        {"status": "done"},
    ]
    result = await test_kucoinf.trade.poll_for_done(
        order_id="order1", interval=0.01, max_attempts=4
    )
    assert result["status"] == "done"
