# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that interacts with the **Binance Futures Testnet (USDT-M)** API.  
The bot allows users to place MARKET, LIMIT, and STOP-LIMIT orders with input validation, structured code architecture, and logging.

---

## Features

- Place orders on Binance Futures Testnet
- Supports:
  - MARKET orders
  - LIMIT orders
  - STOP-LIMIT orders
- Supports both:
  - BUY
  - SELL
- Command-line interface using `argparse`
- Input validation before order placement
- Structured modular architecture
- API error and exception handling
- Logging of:
  - API requests
  - API responses
  - Errors
- Secure API key handling using environment variables

---

## Project Structure

```
Tradebot/
│
├── bot/
│   ├── client.py              # Binance API client configuration
│   ├── orders.py              # Order placement logic
│   ├── validators.py          # Input validation
│   └── logging_config.py      # Logging configuration
│
├── logs/
│   └── bot.log                # Generated log file
│
├── cli.py                     # Command-line interface
├── test_connection.py         # Binance connection testing
├── requirements.txt           # Python dependencies
├── .env                       # API credentials
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/23f2001486/Tradebot.git

cd Tradebot
```

---

## 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file in the project root:

```
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret_key
```

Do not share your API credentials publicly.

---

# Binance Testnet Setup

1. Create a Binance Futures Testnet/Demo account.
2. Generate API credentials.
3. Enable Futures trading permissions.
4. Add the keys to the `.env` file.

---

# Usage

## Test Binance Connection

```bash
python test_connection.py
```

Successful output:

```
Connected to Binance Futures Testnet!
```

---

# Place Orders

## 1. MARKET Order

A market order executes immediately at the current market price.

Example:

```bash
python cli.py \
--symbol BTCUSDT \
--side BUY \
--type MARKET \
--quantity 0.01
```

---

## 2. LIMIT Order

A limit order executes only when the market reaches the specified price.

Example:

```bash
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type LIMIT \
--quantity 0.01 \
--price 106000
```

---

## 3. STOP-LIMIT Order

A stop-limit order triggers a limit order when the stop price is reached.

Example:

```bash
python cli.py \
--symbol BTCUSDT \
--side SELL \
--type STOP_LIMIT \
--quantity 0.01 \
--price 98500 \
--stop-price 99000
```

Meaning:

When BTC price reaches 99000 USDT, place a SELL LIMIT order at 98500 USDT.

---

# CLI Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `--symbol` | Trading pair | BTCUSDT |
| `--side` | Order direction | BUY / SELL |
| `--type` | Order type | MARKET / LIMIT / STOP_LIMIT |
| `--quantity` | Order quantity | 0.01 |
| `--price` | Limit price | 105000 |
| `--stop-price` | Trigger price for stop-limit | 99000 |

---

# Validation

The bot validates:

- Empty symbols
- Invalid order sides
- Invalid order types
- Invalid quantities
- Missing LIMIT prices
- Missing STOP-LIMIT trigger prices

Invalid inputs are rejected before sending requests to Binance.

---

# Logging

Logs are stored in:

```
logs/bot.log
```

Example:

```
INFO - Starting input validation
INFO - Binance client created successfully
INFO - Creating LIMIT order
INFO - Order placed successfully
ERROR - API request failed
```

---

# Error Handling

The bot handles:

- Invalid user input
- Binance API errors
- Network failures
- Authentication failures
- Invalid order parameters

---

# Technologies Used

- Python
- Binance Futures API
- python-binance
- argparse
- python-dotenv
- Logging module

---

# Security

- API keys are stored using environment variables.
- `.env` files are excluded from Git using `.gitignore`.
- Sensitive information is never logged.

---

# Future Improvements

- Interactive CLI menus
- Order history tracking
- Portfolio monitoring
- Additional strategies:
  - OCO orders
  - TWAP execution
  - Grid trading
- Web dashboard interface

---

## Author

Divya
