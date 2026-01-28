
# Binance Futures Testnet Trading Bot (USDT-M)

A Python command-line application that places MARKET and LIMIT orders on Binance USDT-M Futures Testnet.  
The application supports both BUY and SELL sides, validates user input via CLI, logs all activity, and handles API and network errors gracefully.

---

## Overview

This project demonstrates how to interact with the Binance Futures Testnet using Python and the `python-binance` library.  
It is structured with clear separation between the command-line interface, API client logic, configuration, and logging.

The bot is intended for testing and educational purposes only and does not use real funds.

---

## Features

- Place MARKET and LIMIT orders
- Supports BUY and SELL sides
- Binance USDT-M Futures Testnet support
- Command-line interface using argparse
- Structured codebase with separate layers:
  - CLI layer
  - API client layer
  - Logging layer
- Logs API requests, responses, and errors to a log file
- Handles invalid input, API errors, and network failures

---

## Project Structure


binance_futures_bot/
│
├── cli.py
├── client.py
├── config.py
├── logger.py
├── requirements.txt
├── README.md
├── .gitignore
└── bot.log



---

## Requirements

- Python 3.9 or higher
- Binance Futures Testnet account
- Binance Futures Testnet API key and secret

---

## Installation

Install dependencies using pip:

```bash
pip install -r requirements.txt
````

---

## Configuration

Set your Binance Futures Testnet API credentials as environment variables:

```bash
export BINANCE_API_KEY=your_testnet_api_key
export BINANCE_API_SECRET=your_testnet_api_secret
```

The application uses the following base URL for Binance USDT-M Futures Testnet:

```python
BASE_URL = "https://testnet.binancefuture.com"
```

Never commit API keys or secrets to version control.

---

## Usage

### Place a Market Order (BUY)

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order (SELL)

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## Sample Output

```
=== ORDER REQUEST ===
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001

=== ORDER RESPONSE ===
Order ID     : 123456789
Status       : FILLED
Executed Qty : 0.001
Avg Price    : 59874.50

Order placed successfully
```

---

## Logging

All API requests, responses, and errors are logged to the following file:

```
bot.log
```

Example log entry:

```
2026-01-28 12:30:45 | INFO | Placing order | BTCUSDT BUY MARKET qty=0.001
```

---

## Error Handling

The application safely handles:

* Invalid command-line input
* Missing price for LIMIT orders
* Binance API exceptions
* Network or request failures
* Unexpected runtime exceptions

Errors are printed to the console and written to the log file.

---

## Notes

* This project uses Binance Futures USDT-M Testnet only
* No real funds are used
* Intended for testing, learning, and demonstration purposes

---

## License

MIT License

```
```
