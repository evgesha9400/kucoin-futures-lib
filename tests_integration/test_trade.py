import json
import logging

import pytest

logger = logging.getLogger(__name__)


def test_get_position_list(kucoinf_real):
    pos_list = kucoinf_real.trade.client.get_all_position()
    logger.info(f"pos_list:\n{json.dumps(pos_list, indent=4)}")
    """
    [
        {
            "id": "300000000000739530",
            "symbol": "XBTUSDTM",
            "autoDeposit": false,
            "maintMarginReq": 0.004,
            "riskLimit": 100000,
            "realLeverage": 2.0,
            "crossMode": false,
            "delevPercentage": 0.11,
            "openingTimestamp": 1712601927281,
            "currentTimestamp": 1712602528548,
            "currentQty": 1,
            "currentCost": 72.0278,
            "currentComm": 0.04321668,
            "unrealisedCost": 72.0278,
            "realisedGrossCost": 0.0,
            "realisedCost": 0.04321668,
            "isOpen": true,
            "markPrice": 71850.62,
            "markValue": 71.85062,
            "posCost": 72.0278,
            "posCross": 0,
            "posCrossMargin": 0.0,
            "posInit": 36.0139,
            "posComm": 0.06482502,
            "posCommCommon": 0.06482502,
            "posLoss": 0.0,
            "posMargin": 36.07872502,
            "posMaint": 0.3692145,
            "maintMargin": 35.90154502,
            "realisedGrossPnl": 0.0,
            "realisedPnl": -0.04321668,
            "unrealisedPnl": -0.17718,
            "unrealisedPnlPcnt": -0.0025,
            "unrealisedRoePcnt": -0.0049,
            "avgEntryPrice": 72027.8,
            "liquidationPrice": 36318.3,
            "bankruptPrice": 36013.9,
            "settleCurrency": "USDT",
            "isInverse": false,
            "maintainMargin": 0.004
        },
        {
            "id": "300000000000908252",
            "symbol": "SOLUSDTM",
            "autoDeposit": false,
            "maintMarginReq": 0.007,
            "riskLimit": 50000,
            "realLeverage": 1.99,
            "crossMode": false,
            "delevPercentage": 0.59,
            "openingTimestamp": 1712597669921,
            "currentTimestamp": 1712602528548,
            "currentQty": -1,
            "currentCost": -18.0408,
            "currentComm": 0.01082448,
            "unrealisedCost": -18.0408,
            "realisedGrossCost": 0.0,
            "realisedCost": 0.01082448,
            "isOpen": true,
            "markPrice": 180.081,
            "markValue": -18.0081,
            "posCost": -18.0408,
            "posCross": 0,
            "posCrossMargin": 0.0,
            "posInit": 9.0204,
            "posComm": 0.01623672,
            "posCommCommon": 0.01623672,
            "posLoss": 0.0,
            "posMargin": 9.03663672,
            "posMaint": 0.14252232,
            "maintMargin": 9.06933672,
            "realisedGrossPnl": 0.0,
            "realisedPnl": -0.01082448,
            "unrealisedPnl": 0.0327,
            "unrealisedPnlPcnt": 0.0018,
            "unrealisedRoePcnt": 0.0036,
            "avgEntryPrice": 180.408,
            "liquidationPrice": 269.349,
            "bankruptPrice": 270.612,
            "settleCurrency": "USDT",
            "isInverse": false,
            "maintainMargin": 0.007
        }
    ]    
    """


def test_get_order_list(kucoinf_real):
    order_list = kucoinf_real.trade.client.get_order_list(status="done")
    logger.info(f"order_list:\n{json.dumps(order_list, indent=4)}")
    """
    {
        "currentPage": 1,
        "pageSize": 50,
        "totalNum": 0,
        "totalPage": 0,
        "items": []
    }
    
    {
    "currentPage": 1,
    "pageSize": 50,
    "totalNum": 139,
    "totalPage": 3,
    "items": [
        {
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
            "stopTriggered": false,
            "stopPrice": null,
            "timeInForce": "GTC",
            "postOnly": false,
            "hidden": false,
            "iceberg": false,
            "leverage": "1",
            "forceHold": false,
            "closeOrder": true,
            "visibleSize": 0,
            "clientOid": "e73f6586ec0b11ee98480a58a9feac02",
            "remark": null,
            "tags": "",
            "isActive": false,
            "cancelExist": false,
            "createdAt": 1711524636636,
            "updatedAt": 1711529760958,
            "endAt": 1711529760958,
            "orderTime": 1711524636636773006,
            "settleCurrency": "USDT",
            "filledSize": 1,
            "filledValue": "69.6539",
            "status": "done",
            "reduceOnly": true
        },
        {
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
            "stopTriggered": false,
            "stopPrice": null,
            "timeInForce": "GTC",
            "postOnly": false,
            "hidden": false,
            "iceberg": false,
            "leverage": "1",
            "forceHold": false,
            "closeOrder": true,
            "visibleSize": 0,
            "clientOid": "",
            "remark": null,
            "tags": "",
            "isActive": false,
            "cancelExist": false,
            "createdAt": 1711338130551,
            "updatedAt": 1711338130559,
            "endAt": 1711338130559,
            "orderTime": 1711338130551710991,
            "settleCurrency": "USDT",
            "filledSize": 1,
            "filledValue": "6.325",
            "status": "done",
            "reduceOnly": true
        },
        ...
    ]
    """


def test_get_open_order_details(kucoinf_real):
    open_order_details = kucoinf_real.trade.client.get_open_order_details()
    logger.info(f"open_order_details:\n{json.dumps(open_order_details, indent=4)}")
    """
    {
        "openOrderBuySize": 0,
        "openOrderSellSize": 2,
        "openOrderBuyCost": "0",
        "openOrderSellCost": "143.9672",
        "settleCurrency": "USDT"
    }
    """


def test_get_open_stop_order(kucoinf_real):
    stop_orders = kucoinf_real.trade.client.get_open_stop_order()
    logger.info(f"stop_orders:\n{json.dumps(stop_orders, indent=4)}")


def test_cancel_order(kucoinf_real):
    order_id = "test_order_id"
    order_list = kucoinf_real.trade.client.cancel_order(orderId=order_id)
    logger.info(f"order_list:\n{json.dumps(order_list, indent=4)}")



@pytest.mark.asyncio
async def test_update_stop_loss_stop(kucoinf_real):
    order_id = await kucoinf_real.trade.update_stop_loss_stop_price(
        order_id="test_order_id",
        sl_price="69464.6",
    )
    logger.info(f"order_id: {order_id}")


def test_create_reduce_take_profit_order(kucoinf_real):
    order_id = kucoinf_real.trade.create_reduce_take_profit_order(
        symbol="XBTUSDTM",
        side="sell",
        size=1,
        price=70000,
        reduce_only=True,
    )
    logger.info(f"order_id: {order_id}")