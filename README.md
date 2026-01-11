# Binance Futures Trading Bot

A modular Python application designed for algorithmic trading on the Binance Futures Testnet. This system features a service-oriented architecture with decoupled logic, utility, and presentation layers, supporting both Command Line Interface (CLI) and Web Dashboard execution.

## System Architecture

The project is organized into three distinct modules to ensure separation of concerns:

* **Handler (`handler/`)**: Encapsulates the core business logic (`BasicBot` class), API communication, and order execution strategies.
* **Service (`service/`)**: The presentation layer containing the entry points for the CLI (`main.py`) and the Streamlit Web Dashboard (`app.py`).
* **Helpers (`helpers/`)**: Shared utility functions for configuration loading, logging setup, and data formatting (e.g., precision handling).

### Project Structure

```text
.
├── README.md
├── __pycache__
│   ├── bot.cpython-312.pyc
│   ├── config.cpython-312.pyc
│   └── utils.cpython-312.pyc
├── bot.log
├── handler
│   ├── __pycache__
│   │   └── bot.cpython-312.pyc
│   └── bot.py
├── helpers
│   ├── __pycache__
│   │   ├── config.cpython-312.pyc
│   │   └── utils.cpython-312.pyc
│   ├── config.py
│   └── utils.py
└── service
    ├── __pycache__
    │   ├── app.cpython-312.pyc
    │   └── main.cpython-312.pyc
    ├── app.py
    └── main.py

8 directories, 15 files
```

## Installation

### Prerequisites

* Python 3.10 or higher
* Binance Futures Testnet Account

### Setup

1. **Clone the repository and navigate to the root directory.**
2. **Create and activate a virtual environment (optional but recommended):**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure Environment:**
Create a file named `.env` in the root directory:
```ini
BINANCE_API_KEY="your_testnet_api_key"
BINANCE_SECRET_KEY="your_testnet_secret_key"

```



## Usage

Execute all commands from the project root directory (`binance-crypto-bot`) to ensure module resolution.

### Web Dashboard

Launches a local web server with a visual interface for trading and real-time response monitoring.

```bash
python3 -m streamlit run service/app.py

```

### Command Line Interface

Launches the interactive terminal wizard for rapid order execution.

```bash
python3 -m service.main

```

## Technical Notes

* **Testnet Limitations:** The `BTCUSDT` symbol is the primary supported pair. Other symbols may not be available or liquid on the Testnet.
* **Minimum Notional Value:** The Binance Testnet requires a minimum order value of 100 USDT. Ensure order quantity is sufficient (e.g., > 0.002 BTC).
* **Precision Handling:** The `helpers/utils.py` module automatically formats floating-point values to strings to prevent API precision errors (Error -1111).