import sys
from handler.bot import BasicBot
from helpers.config import api_key, secret_key, logger
from helpers.utils import (
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
            order_type = get_valid_input("Order Type (MARKET/LIMIT/STOP_MARKET): ", ["MARKET", "LIMIT", "STOP_MARKET"])
            qty = get_valid_float(f"Enter Quantity for {symbol}: ")
            
            price = None
            if order_type == "LIMIT":
                price = get_valid_float("Enter Limit Price: ")
                bot.place_order(symbol, side, order_type, qty, price)
            elif order_type == "STOP_MARKET":
                stop_price = get_valid_float("Enter Stop Limit Price: ")
                bot.place_order(symbol, side, order_type, qty, stop_price=stop_price)
                
        except KeyboardInterrupt:
            print("\nBot stopped by the user")
            break
        except Exception as e:
            logger.exception(f"Crash in main loop due to {e}")