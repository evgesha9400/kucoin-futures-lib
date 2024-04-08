import json
import logging

logger = logging.getLogger(__name__)


def test_get_order_list(kucoinf_real):
    order_list = kucoinf_real.trade.trade.get_order_list()
    logger.info(f"order_list:\n{json.dumps(order_list, indent=4)}")
    """
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


def test_cancel_order(kucoinf_real):
    order_id = "165492008100589568"
    order_list = kucoinf_real.trade.trade.cancel_order(orderId=order_id)
    logger.info(f"order_list:\n{json.dumps(order_list, indent=4)}")
