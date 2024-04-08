import json
import logging

logger = logging.getLogger(__name__)


def test_get_contract_detail(kucoinf_real):
    contract_detail = kucoinf_real.market.market.get_contract_detail("XBTUSDTM")
    logger.info(f"contract_detail:\n{json.dumps(contract_detail, indent=4)}")
    """
    {
        "symbol": "XBTUSDTM",
        "rootSymbol": "USDT",
        "type": "FFWCSX",
        "firstOpenDate": 1585555200000,
        "expireDate": null,
        "settleDate": null,
        "baseCurrency": "XBT",
        "quoteCurrency": "USDT",
        "settleCurrency": "USDT",
        "maxOrderQty": 1000000,
        "maxPrice": 1000000.0,
        "lotSize": 1,
        "tickSize": 0.1,
        "indexPriceTickSize": 0.01,
        "multiplier": 0.001,
        "initialMargin": 0.008,
        "maintainMargin": 0.004,
        "maxRiskLimit": 100000,
        "minRiskLimit": 100000,
        "riskStep": 50000,
        "makerFeeRate": 0.0002,
        "takerFeeRate": 0.0006,
        "takerFixFee": 0.0,
        "makerFixFee": 0.0,
        "settlementFee": null,
        "isDeleverage": true,
        "isQuanto": true,
        "isInverse": false,
        "markMethod": "FairPrice",
        "fairMethod": "FundingRate",
        "fundingBaseSymbol": ".XBTINT8H",
        "fundingQuoteSymbol": ".USDTINT8H",
        "fundingRateSymbol": ".XBTUSDTMFPI8H",
        "indexSymbol": ".KXBTUSDT",
        "settlementSymbol": "",
        "status": "Open",
        "fundingFeeRate": 0.001013,
        "predictedFundingFeeRate": 0.000885,
        "fundingRateGranularity": 28800000,
        "openInterest": "7447014",
        "turnoverOf24h": 751440499.385109,
        "volumeOf24h": 10743.466,
        "markPrice": 68744.79,
        "indexPrice": 68723.05,
        "lastTradePrice": 68747.4,
        "nextFundingRateTime": 457541,
        "maxLeverage": 125,
        "sourceExchanges": [
            "okex",
            "binance",
            "kucoin",
            "bybit",
            "bitget",
            "bitmart",
            "gateio"
        ],
        "premiumsSymbol1M": ".XBTUSDTMPI",
        "premiumsSymbol8H": ".XBTUSDTMPI8H",
        "fundingBaseSymbol1M": ".XBTINT",
        "fundingQuoteSymbol1M": ".USDTINT",
        "lowPrice": 68456.0,
        "highPrice": 71859.0,
        "priceChgPct": -0.0164,
        "priceChg": -1149.6
    }
    """


def test_get_ticker(kucoinf_real):
    ticker = kucoinf_real.market.market.get_ticker("XBTUSDTM")
    logger.info(f"ticker:\n{json.dumps(ticker, indent=4)}")
    """
    {
        "sequence": 1700524393648,
        "symbol": "XBTUSDTM",
        "side": "sell",
        "size": 11,
        "tradeId": "1741164111132",
        "price": "68804.3",
        "bestBidPrice": "68822.2",
        "bestBidSize": 388,
        "bestAskPrice": "68822.3",
        "bestAskSize": 175,
        "ts": 1711569300284000000
    }
    """
