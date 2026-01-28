from binance import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from config import API_KEY, SECRET_KEY, BASE_URL
from logger import log

logger = log()


class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(API_KEY, SECRET_KEY)
        self.client.FUTURES_URL = BASE_URL

    def place_order(self, symbol, side, order_type, quantity, price=None):
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        try:
            logger.info(
                f"Placing order | {symbol} {side} {order_type} "
                f"qty={quantity} price={price}"
            )

            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=Client.ORDER_TYPE_MARKET,
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders")

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=Client.ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=price,
                    timeInForce=Client.TIME_IN_FORCE_GTC
                )
            else:
                raise ValueError("Invalid order type")

            logger.info(f"Order response: {response}")

            return {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice")
            }

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Request error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
