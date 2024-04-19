Tasks:
- [ ] Handle limit orders with listener and market order with polling when waiting for fill in kucoinf.create_order
- [ ] Add propagation of all create order settings from kucoinf.create_order to kucoinf.trade methods (stopPriceType, timeInForce)
- [ ] Modify kucoinf.trade.update_stop_loss_stop to be a general update_order method 
- [ ] Decompose KucoinFuturesTrade class into TradeClient <- Risk, Poll, Orders <- KucoinFuturesTrade
