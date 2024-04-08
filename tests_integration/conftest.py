import logging
import os
import pathlib

import pytest
from dotenv import load_dotenv

from kucoin_futures_lib.factory import initialize_kucoinf

logging.basicConfig(level=logging.INFO)


TEST_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def kucoinf_real():
    """Fixture to initialize KucoinFutures with real credentials."""
    load_dotenv(dotenv_path=TEST_DIR / ".env")
    return initialize_kucoinf(
        api_key=os.getenv("KUCOIN_API_KEY"),
        api_secret=os.getenv("KUCOIN_API_SECRET"),
        api_passphrase=os.getenv("KUCOIN_API_PASSPHRASE"),
    )
