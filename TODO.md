Tasks:
- [ ] Rewrite WebSocket client for graceful shutdown and disconnect
- [ ] Add remark support
- [ ] Handle limit orders with listener and market order with polling when waiting for fill in kucoinf.create_order
- [ ] Add propagation of all create order settings from kucoinf.create_order to kucoinf.trade methods (stopPriceType, timeInForce)
- [ ] Modify kucoinf.trade.update_stop_loss_stop to be a general update_order method 
- [ ] Decompose KucoinFuturesTrade class into TradeClient <- Risk, Poll, Orders <- KucoinFuturesTrade
- [ ] Global rate limiter for all requests and rate limit weight for each request method KUCOIN API
- [ ] ??? Global field store module for all fields within the repository
