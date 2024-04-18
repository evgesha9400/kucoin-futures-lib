import time

from kucoin_futures_lib import initialize_kucoinf
from utils import retriable

if __name__ == "__main__":
    kucoinf = initialize_kucoinf(
        api_key='your-api-key',
        api_secret='your-api-secret',
        api_passphrase='your-api-passphrase',
        # Optional retriable method to retry methods in the library
        retriable=retriable(retries=3, exceptions=(Exception,), backoff_base=2.0, initial_backoff=0.1),
    )
    order_id = kucoinf.trade.create_order(
        instrument="XBTUSDTM",
        side="buy",
        size=3,
        leverage=10,
    )
    print(f"Order ID: {order_id}")

    time.sleep(5)

    tp_order_id, sl_order_id = kucoinf.trade.create_stop_loss_and_take_profit(
        instrument="XBTUSDTM",
        side="buy",
        take_profit=75000,
        stop_loss=60000,
    )
    print(f"Take profit order ID: {tp_order_id}")
    print(f"Stop loss order ID: {sl_order_id}")
