import logging

import pytest

logger = logging.getLogger(__name__)


def test_get_open_limit_orders(test_kucoinf):
    test_order = {
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
    test_kucoinf.trade.client.get_order_list.return_value = {
        "currentPage": 1,
        "pageSize": 50,
        "totalNum": 1,
        "totalPage": 1,
        "items": [test_order],
    }
    orders = test_kucoinf.trade.get_open_limit_orders()
    assert len(orders) == 1
    assert orders[0] == test_order


def test_get_order_history(test_kucoinf):
    test_orders = [
        {
            "id": "167330565140250624",
            "symbol": "XBTUSDTM",
            "type": "market",
            "side": "buy",
            "price": "0",
            "size": 0,
            "value": "0",
            "dealValue": "0",
            "dealSize": 0,
            "stp": "",
            "stop": "up",
            "stopPriceType": "TP",
            "stopTriggered": False,
            "stopPrice": "69465.6",
            "timeInForce": "GTC",
            "postOnly": False,
            "hidden": False,
            "iceberg": False,
            "leverage": "1",
            "forceHold": False,
            "closeOrder": True,
            "visibleSize": 0,
            "clientOid": "f19e1f4af6ce11ee964aacde48001122",
            "remark": "Order Cancel:Order manually canceled.",
            "tags": "",
            "isActive": False,
            "cancelExist": True,
            "createdAt": 1712707917581,
            "updatedAt": 1712707942693,
            "endAt": 1712707942693,
            "orderTime": 1712707917581079481,
            "settleCurrency": "USDT",
            "filledSize": 0,
            "filledValue": "0",
            "status": "done",
            "reduceOnly": False,
        },
        {
            "id": "167330519980183553",
            "symbol": "XBTUSDTM",
            "type": "market",
            "side": "buy",
            "price": "0",
            "size": 0,
            "value": "0",
            "dealValue": "0",
            "dealSize": 0,
            "stp": "",
            "stop": "up",
            "stopPriceType": "TP",
            "stopTriggered": False,
            "stopPrice": "69466.6",
            "timeInForce": "GTC",
            "postOnly": False,
            "hidden": False,
            "iceberg": False,
            "leverage": "1",
            "forceHold": False,
            "closeOrder": True,
            "visibleSize": 0,
            "clientOid": "eb377da4f6ce11eea011acde48001122",
            "remark": "Order Cancel:Order manually canceled.",
            "tags": "",
            "isActive": False,
            "cancelExist": True,
            "createdAt": 1712707906813,
            "updatedAt": 1712707917240,
            "endAt": 1712707917240,
            "orderTime": 1712707906813662535,
            "settleCurrency": "USDT",
            "filledSize": 0,
            "filledValue": "0",
            "status": "done",
            "reduceOnly": False,
        },
        {
            "id": "167330248243867648",
            "symbol": "XBTUSDTM",
            "type": "market",
            "side": "buy",
            "price": "0",
            "size": 0,
            "value": "0",
            "dealValue": "0",
            "dealSize": 0,
            "stp": "",
            "stop": "up",
            "stopPriceType": "TP",
            "stopTriggered": False,
            "stopPrice": "69464.6",
            "timeInForce": "GTC",
            "postOnly": False,
            "hidden": False,
            "iceberg": False,
            "leverage": "1",
            "forceHold": False,
            "closeOrder": True,
            "visibleSize": 0,
            "clientOid": "c495bdd2f6ce11ee93ffacde48001122",
            "remark": "Order Cancel:Order manually canceled.",
            "tags": "",
            "isActive": False,
            "cancelExist": True,
            "createdAt": 1712707842026,
            "updatedAt": 1712707906508,
            "endAt": 1712707906508,
            "orderTime": 1712707842026587979,
            "settleCurrency": "USDT",
            "filledSize": 0,
            "filledValue": "0",
            "status": "done",
            "reduceOnly": False,
        },
    ]
    test_kucoinf.trade.client.get_order_list.return_value = {
        "currentPage": 1,
        "pageSize": 50,
        "totalNum": 3,
        "totalPage": 1,
        "items": test_orders,
    }
    orders = test_kucoinf.trade.get_order_history()
    assert len(orders) == 3
    assert orders == test_orders


def test_get_open_stop_orders(test_kucoinf):
    stop_order = {
        "id": "167330671801491456",
        "symbol": "XBTUSDTM",
        "type": "market",
        "side": "buy",
        "price": "0",
        "size": 0,
        "value": "0",
        "dealValue": "0",
        "dealSize": 0,
        "stp": None,
        "stop": "up",
        "stopPriceType": "TP",
        "stopTriggered": False,
        "stopPrice": "69464.6",
        "timeInForce": "GTC",
        "postOnly": False,
        "hidden": False,
        "iceberg": False,
        "leverage": "1",
        "forceHold": False,
        "closeOrder": True,
        "visibleSize": 0,
        "clientOid": "00c7e212f6cf11ee96aaacde48001122",
        "remark": None,
        "tags": "",
        "isActive": False,
        "cancelExist": False,
        "createdAt": 1712707943013,
        "updatedAt": 1712707943013,
        "endAt": None,
        "orderTime": 1712707943010737407,
        "settleCurrency": "USDT",
        "filledSize": 0,
        "filledValue": "0",
        "status": "done",
        "reduceOnly": False,
    }
    test_kucoinf.trade.client.get_open_stop_order.return_value = {
        "currentPage": 1,
        "pageSize": 50,
        "totalNum": 1,
        "totalPage": 1,
        "items": [stop_order],
    }
    orders = test_kucoinf.trade.get_open_stop_orders()
    assert len(orders) == 1


def test_create_market_order(test_kucoinf):
    test_kucoinf.trade.client.create_market_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_market_order(
        instrument="XBTUSDTM",
        side="buy",
        size=1,
        leverage=100,
    )
    test_kucoinf.trade.client.create_market_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="buy",
        size="1",
        lever="100",
    )
    assert order_id == "12345689"


def test_create_limit_order(test_kucoinf):
    test_kucoinf.trade.client.create_limit_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_limit_order(
        instrument="XBTUSDTM",
        side="buy",
        size=1,
        price=1000.001,
        leverage=100,
    )
    test_kucoinf.trade.client.create_limit_order.assert_called_once_with(
        symbol="XBTUSDTM", side="buy", size="1", price="1000.001", lever="100"
    )
    assert order_id == "12345689"


def test_create_take_profit_limit(test_kucoinf):
    test_kucoinf.trade.client.create_limit_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_take_profit_limit(
        instrument="XBTUSDTM",
        entry_side="buy",
        tp_price=1000,
    )
    test_kucoinf.trade.client.create_limit_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        price="1000",
        timeInForce="GTC",
        closeOrder=True,
        lever=None,
        size=None,
        reduceOnly=False,
    )
    assert order_id == "12345689"


def test_create_reduce_take_profit_limit(test_kucoinf):
    test_kucoinf.trade.client.create_limit_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_take_profit_limit(
        instrument="XBTUSDTM",
        entry_side="buy",
        tp_price=1000,
        reduce_amount=1,
    )
    test_kucoinf.trade.client.create_limit_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        price="1000",
        timeInForce="GTC",
        closeOrder=False,
        reduceOnly=True,
        size="1",
        lever=None,
    )
    assert order_id == "12345689"


def test_create_take_profit_stop(test_kucoinf):
    test_kucoinf.trade.client.create_market_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_take_profit_stop(
        instrument="XBTUSDTM",
        entry_side="buy",
        tp_price=1000,
    )
    test_kucoinf.trade.client.create_market_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        stop="up",
        stopPrice="1000",
        timeInForce="GTC",
        stopPriceType="TP",
        closeOrder=True,
        lever=None,
        size=None,
        reduceOnly=False,
    )
    assert order_id == "12345689"


def test_create_reduce_take_profit_stop(test_kucoinf):
    test_kucoinf.trade.client.create_market_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_take_profit_stop(
        instrument="XBTUSDTM",
        entry_side="buy",
        tp_price=1000,
        reduce_amount=1,
    )
    test_kucoinf.trade.client.create_market_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        stop="up",
        stopPrice="1000",
        timeInForce="GTC",
        stopPriceType="TP",
        closeOrder=False,
        reduceOnly=True,
        size="1",
        lever=None,
    )
    assert order_id == "12345689"


def test_create_stop_loss_limit(test_kucoinf):
    test_kucoinf.trade.client.create_limit_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_stop_loss_limit(
        instrument="XBTUSDTM",
        entry_side="buy",
        sl_price=1000,
    )
    test_kucoinf.trade.client.create_limit_order.assert_called_once_with(
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


def test_create_stop_loss_stop(test_kucoinf):
    test_kucoinf.trade.client.create_market_order.return_value = {"orderId": "12345689"}
    order_id = test_kucoinf.trade.create_stop_loss_stop(
        instrument="XBTUSDTM",
        entry_side="buy",
        sl_price=1000,
    )
    test_kucoinf.trade.client.create_market_order.assert_called_once_with(
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


@pytest.mark.asyncio
async def test_update_stop_loss_stop(test_kucoinf):
    test_kucoinf.trade.client.get_open_stop_order.return_value = {
        "currentPage": 1,
        "pageSize": 50,
        "totalNum": 1,
        "totalPage": 1,
        "items": [
            {
                "id": "12345689",
                "symbol": "XBTUSDTM",
                "side": "sell",
                "stop": "down",
                "stopPriceType": "TP",
                "timeInForce": "GTC",
                "closeOrder": True,
                "leverage": 1,
            }
        ],
    }

    await test_kucoinf.trade.update_stop_loss_stop_price(
        order_id="12345689",
        sl_price="70000",
    )

    test_kucoinf.trade.client.cancel_order.assert_called_once_with("12345689")
    test_kucoinf.trade.client.create_market_order.assert_called_once_with(
        symbol="XBTUSDTM",
        side="sell",
        stop="down",
        lever="1",
        stopPriceType="TP",
        stopPrice="70000",
        timeInForce="GTC",
        closeOrder=True,
    )


@pytest.mark.asyncio
async def test_poll_for_fill_filled(mock_trade_client, test_kucoinf):
    test_fill = {
        "symbol": "XBTUSDTM",
        "orderId": "12345689",
        "price": "68804.3",
        "size": 1,
        "side": "sell",
        "ts": 1711569300284000000,
    }
    mock_trade_client.get_recent_fills.return_value = [test_fill]
    response = await test_kucoinf.trade.poll_for_fill(order_id="12345689")
    assert response == test_fill


@pytest.mark.asyncio
async def test_poll_for_fill_multiple_attempts(mock_trade_client, test_kucoinf):
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
    mock_trade_client.get_recent_fills.side_effect = [
        [],
        [test_fill1],
        [test_fill1, test_fill2],
    ]
    response = await test_kucoinf.trade.poll_for_fill(
        order_id="12345689", interval=0.01, max_attempts=3
    )
    assert response == test_fill2


@pytest.mark.asyncio
async def test_poll_for_fill_unexpected(mock_trade_client, test_kucoinf):
    mock_trade_client.get_recent_fills.return_value = {"code": "200000", "data": []}
    with pytest.raises(
        TimeoutError, match="Order 12345689 was not filled within the timeout period"
    ):
        await test_kucoinf.trade.poll_for_fill(
            order_id="12345689", max_attempts=1, interval=0.01
        )


def test_cancel_order(mock_trade_client, test_kucoinf):
    order_id = "12345689"
    test_kucoinf.trade.cancel_order(order_id)
    mock_trade_client.cancel_order.assert_called_once_with(orderId=order_id)


@pytest.mark.asyncio
async def test_poll_for_done_with_done_status(mock_trade_client, test_kucoinf):
    mock_trade_client.get_order_details.return_value = {
        "status": "done",
        "orderId": "order1",
    }
    result = await test_kucoinf.trade.poll_for_done(order_id="order1", max_attempts=1)
    assert result["status"] == "done"


@pytest.mark.asyncio
async def test_poll_for_done_with_not_done_status(mock_trade_client, test_kucoinf):
    mock_trade_client.get_order_details.return_value = {
        "status": "not_done",
        "orderId": "order1",
    }
    with pytest.raises(TimeoutError):
        await test_kucoinf.trade.poll_for_done(
            order_id="order1", interval=0.01, max_attempts=1
        )


@pytest.mark.asyncio
async def test_poll_for_done_with_changing_status(mock_trade_client, test_kucoinf):
    mock_trade_client.get_order_details.side_effect = [
        {"status": "not_done"},
        {"status": "not_done"},
        {"status": "not_done"},
        {"status": "done"},
    ]
    result = await test_kucoinf.trade.poll_for_done(
        order_id="order1", interval=0.01, max_attempts=4
    )
    assert result["status"] == "done"
