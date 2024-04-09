import pytest

from kucoin_futures_lib.helper import KucoinFuturesHelper


@pytest.mark.parametrize(
    "tick_size, expected_precision",
    [
        (0.1, 1),
        (0.01, 2),
        (0.001, 3),
        (0.0001, 4),
        (0.00001, 5),
    ],
)
def test_calculate_precision(tick_size, expected_precision):
    tick_size = 0.1
    precision = KucoinFuturesHelper.calculate_precision(tick_size=tick_size)
    assert precision == 1


@pytest.mark.parametrize(
    "investment_amount, current_price, lot_size, expected_lots",
    [
        (1000, 10, 0.1, 1000),  # Normal case
        (1000, 10, 0, 0),  # Lot size is zero
        (1000, 0, 0.1, 0),  # Current price is zero
        (0, 10, 0.1, 0),  # Investment amount is zero
        (1000, 10, 1, 100),  # Lot size is one
        (1000, 1, 0.1, 10000),  # Current price is one
        (1, 10, 0.1, 1),  # Investment amount is one
    ],
)
def test_calculate_lots(investment_amount, current_price, lot_size, expected_lots):
    lots = KucoinFuturesHelper.calculate_lots(
        investment_amount=investment_amount,
        current_price=current_price,
        lot_size=lot_size
    )
    assert lots == expected_lots
