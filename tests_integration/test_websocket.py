import asyncio
import json
import logging

import pytest
from kucoin_futures.ws_client import KucoinFuturesWsClient

logger = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_websocket_level2_market_data(kucoinf_real):
    instrument = "XBTUSDTM"
    topic = "/contractMarket/level2:" + instrument
    message_received = False

    async def log_msg(msg):
        """callback function to log the message"""
        nonlocal message_received
        logger.info(f"market_data:\n{json.dumps(msg, indent=4)}")
        message_received = True

    ws_client = await KucoinFuturesWsClient.create(
        None, kucoinf_real.websocket.token, log_msg, private=False
    )

    await ws_client.subscribe(topic)
    try:
        while not message_received:
            await asyncio.sleep(1)
    finally:
        await ws_client.unsubscribe(topic)
        await asyncio.sleep(1)


@pytest.mark.asyncio
async def test_websocket_get_ticker_v1(kucoinf_real):
    instrument = "XBTUSDTM"
    topic = "/contractMarket/ticker:" + instrument
    message_received = False

    async def log_msg(msg):
        """callback function to log the message"""
        nonlocal message_received
        logger.info(f"ticker v1:\n{json.dumps(msg, indent=4)}")
        message_received = True

    ws_client = await KucoinFuturesWsClient.create(
        None, kucoinf_real.websocket.token, log_msg, private=False
    )

    await ws_client.subscribe(topic)
    try:
        while not message_received:
            await asyncio.sleep(1)
    finally:
        await ws_client.unsubscribe(topic)
        await asyncio.sleep(1)
    """
    {
    "topic": "/contractMarket/ticker:XBTUSDTM",
    "type": "message",
    "subject": "ticker",
    "sn": 1742367095805,
    "data": {
        "symbol": "XBTUSDTM",
        "sequence": 1742367095805,
        "side": "sell",
        "size": 7,
        "price": "65658.7",
        "bestBidSize": 1,
        "bestBidPrice": "65650.2",
        "bestAskPrice": "65656.8",
        "tradeId": "1742367095805",
        "bestAskSize": 276,
        "ts": 1712168943687000000
    }
}
    """


@pytest.mark.asyncio
async def test_websocket_get_ticker_v2(kucoinf_real):
    instrument = "XBTUSDTM"
    topic = "/contractMarket/tickerV2:" + instrument
    message_received = asyncio.Event()

    async def log_msg(msg):
        """callback function to log the message"""
        nonlocal message_received
        logger.info(f"ticker v2:\n{json.dumps(msg, indent=4)}")
        message_received.set()

    ws_client = await KucoinFuturesWsClient.create(
        None, kucoinf_real.websocket.token, log_msg, private=False
    )

    await ws_client.subscribe(topic)
    try:
        await message_received.wait()
    finally:
        await ws_client.unsubscribe(topic)
    """
    {
        "topic": "/contractMarket/tickerV2:XBTUSDTM",
        "type": "message",
        "subject": "tickerV2",
        "sn": 1700700374286,
        "data": {
            "symbol": "XBTUSDTM",
            "sequence": 1700700374286,
            "bestBidSize": 1320,
            "bestBidPrice": "65941.4",
            "bestAskPrice": "65941.5",
            "bestAskSize": 275,
            "ts": 1712170829821000000
        }
    }
    """
