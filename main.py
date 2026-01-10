import sys
from bot import BasicBot
from config import api_key, secret_key, logger
from utils import (
    get_valid_float, 
    get_valid_input,
    format_quantity
)

if __name__=="__main__":
    if not api_key or not secret_key:
        logger.critical("Exiting due to missing keys.")
        sys.exit(1)
    while True:
        try:
            bot = BasicBot(api_key, secret_key)
            print("---ORDER WIZARD----")
            print("PRESS ctrl+C to exit")
            symbol = get_valid_input("Enter Symbol (e.g. BTCUSDT): ")
            side = get_valid_input("Enter Side (BUY/SELL): ", ["BUY", "SELL"])
            order_type = get_valid_input("Order Type (MARKET/LIMIT): ", ["MARKET", "LIMIT"])
            qty = get_valid_float(f"Enter Quantity for {symbol}: ")
            qty = format_quantity(qty)
            if qty == 0:
                print("Error: Quantity too small after formatting.\
                    Minimum is 0.001.")
                exit()

            print(f"Formatted Quantity: {qty}")
            
            price = None
            if order_type == "LIMIT":
                price = get_valid_float("Enter Limit Price: ")

            bot.place_order(symbol, side, order_type, qty, price)
        except KeyboardInterrupt:
            print("\nBot stopped by the user")
        except Exception as e:
            logger.exception(f"Crash in main loop due to {e}")