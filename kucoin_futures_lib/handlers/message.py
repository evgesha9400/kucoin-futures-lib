"""Handler that listens for the status of an order."""
import asyncio
import logging
from typing import Dict, List, Literal, Optional

from kucoin_futures_lib.handlers.base import HandlerABC

logger = logging.getLogger(__name__)


class MessageHandler(HandlerABC):

    def __init__(
        self,
        order_id: str,
        message_type: Optional[List[Literal["open", "match", "filled", "canceled", "update"]]] = None,
    ):
        """The handler will stop listening when any of the message_type is received.
        :param order_id: The order ID to listen for.
        :param message_type: The message type to listen for. Default is None."""

        self.order_id = order_id
        self.message_type = message_type
        self.received_message = None
        self._reached = asyncio.Event()
        self._topic = "/contractMarket/tradeOrders"

    def __repr__(self):
        return f"MessageHandler(order_id='{self.order_id}', message_type={self.message_type})"

    @property
    def topic(self) -> str:
        """Return the topic supported by the handler."""
        return f"{self._topic}"

    @property
    def private(self) -> bool:
        """Return the privacy status for the topic."""
        return True

    @property
    def done(self) -> asyncio.Event:
        """Return the done status for the handler."""
        return self._reached


    async def handle(self, msg: Dict):
        """Handle the trade order message from
        :param msg: The trade order message.
        https://www.kucoin.com/docs/websocket/futures-trading/private-channels/trade-orders
        """
        if self._reached.is_set():
            return

        trade_order = msg.get("data", {})
        trade_order_id = trade_order.get("orderId", "")
        message_type = trade_order.get("type", "")

        if trade_order_id == self.order_id and message_type in self.message_type:
            logger.info("Order %s received %s", self.order_id, message_type)
            self.received_message = message_type
            self._reached.set()
