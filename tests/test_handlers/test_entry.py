from unittest.mock import AsyncMock

import pytest

from kucoin_futures_lib.handlers import EntryRangeHandler


def test_entry_range_handler_entry_validation():
    with pytest.raises(
        AssertionError, match="Entry high must be greater than entry low"
    ):
        EntryRangeHandler("XBTUSDTM", 100, 200)


@pytest.mark.asyncio
async def test_handle_entry_range_handler_in_range_with_callback():
    # Arrange
    mock_callback = AsyncMock()
    handler = EntryRangeHandler("XBTUSDTM", 200, 100, callback=mock_callback)

    # Act
    await handler.handle(
        {
            "data": {
                "bestBidPrice": "150",
                "bestAskPrice": "152",
            }
        }
    )

    # Assert
    assert handler.done.is_set() is True
    assert mock_callback.called is True


@pytest.mark.asyncio
async def test_handle_entry_range_handler_in_range_no_callback():
    # Arrange
    handler = EntryRangeHandler("XBTUSDTM", 200, 100)

    # Act
    await handler.handle(
        {
            "data": {
                "bestBidPrice": "150",
                "bestAskPrice": "152",
            }
        }
    )

    # Assert
    assert handler.done.is_set() is True


@pytest.mark.asyncio
async def test_handle_entry_range_handler_out_of_range():
    # Arrange
    handler = EntryRangeHandler("XBTUSDTM", 200, 100)

    # Act
    await handler.handle(
        {
            "data": {
                "bestBidPrice": "50",
                "bestAskPrice": "52",
            }
        }
    )

    # Assert
    assert handler.done.is_set() is False


@pytest.mark.asyncio
async def test_handle_entry_range_handler_invalid_data():
    # Arrange
    handler = EntryRangeHandler("XBTUSDTM", 200, 100)

    # Act
    await handler.handle({})

    # Assert
    assert handler.done.is_set() is False
