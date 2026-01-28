import argparse
import sys

from client import BinanceFuturesClient


def validate_args(args):
    if args.side not in ("BUY", "SELL"):
        raise ValueError("side must be BUY or SELL")

    if args.type not in ("MARKET", "LIMIT"):
        raise ValueError("type must be MARKET or LIMIT")

    if args.type == "LIMIT" and args.price is None:
        raise ValueError("price is required for LIMIT orders")

    if args.quantity <= 0:
        raise ValueError("quantity must be positive")


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot (USDT-M)"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        validate_args(args)
        client = BinanceFuturesClient()

        print("\n=== ORDER REQUEST ===")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        if args.price:
            print(f"Price    : {args.price}")

        response = client.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n=== ORDER RESPONSE ===")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

        print("\nOrder placed successfully")

    except Exception as e:
        print("\nOrder failed")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
