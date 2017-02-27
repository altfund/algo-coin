import datetime
from .enums import Side, \
                   CurrencyType, \
                   OrderType, \
                   OrderSubType, \
                   ExchangeType, \
                   TickType
from .utils import struct


@struct
class MarketData:
    # common
    time = datetime.datetime
    volume = float
    price = float
    type = TickType
    currency = CurrencyType, CurrencyType.BTC

    # maybe specific
    remaining = float, float('nan')
    reason = str, ''
    sequence = int, -1


@struct
class TradeRequest:
    data = MarketData
    side = Side

    volume = float
    price = float
    currency = CurrencyType, CurrencyType.BTC

    order_type = OrderType, OrderType.MARKET
    order_sub_type = OrderSubType, OrderSubType.NONE
    # exchange = ExchangeType

    risk_check = bool, False
    risk_reason = str, ''


@struct
class TradeResponse:
    data = MarketData
    request = TradeRequest
    side = Side

    volume = float
    price = float
    currency = CurrencyType, CurrencyType.BTC

    slippage = float, 0.0
    transaction_cost = float, 0.0

    success = bool


@struct
class Account:
    currency = CurrencyType
    balance = float
    id = str

    def __repr__(self):
        return "<" + self.id + " - " + \
              str(self.currency) + " - " + str(self.balance) + ">"