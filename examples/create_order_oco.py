import asyncio
from kucoin_futures_lib import initialize_kucoinf
from kucoin_futures_lib.utils import retriable


async def main():
    kucoinf = initialize_kucoinf(
        api_key='your-api-key',
        api_secret='your-api-secret',
        api_passphrase='your-api-passphrase',
        # Optional retriable method to retry methods in the library
        retriable=retriable(retries=3, exceptions=(Exception,), backoff_base=2.0, initial_backoff=0.1),
    )
    order_id = await kucoinf.create_order(
        instrument="XBTUSDTM",
        side="buy",
        size=3,
        take_profit=75000,
        stop_loss=60000,
        leverage=10,
        enable_oco=True,
    )
    print(f"Order ID: {order_id}")


def start():
    """Start the main function."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


if __name__ == "__main__":
    start()