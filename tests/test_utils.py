from unittest.mock import MagicMock
from kucoin_futures_lib.utils import retriable, retry


def test_retriable():
    # Arrange
    mock_func = MagicMock(side_effect=Exception("Test exception"))
    decorated_func = retriable(retries=3, exceptions=(Exception,), backoff_base=2.0, initial_backoff=0.01)(mock_func)

    # Act
    result = decorated_func()

    # Assert
    assert result is None
    assert mock_func.call_count == 3


def test_retry():
    # Arrange
    mock_func = MagicMock(side_effect=Exception("Test exception"))

    # Act
    result = retry(func=mock_func, retries=3, exceptions=(Exception,), backoff_base=2.0, initial_backoff=0.01)

    # Assert
    assert result is None
    assert mock_func.call_count == 3