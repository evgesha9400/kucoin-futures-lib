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
