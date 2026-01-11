from binance.client import Client
from typing import Dict, Optional, Tuple
from helpers.config import logger
from binance.exceptions import BinanceAPIException, BinanceRequestException

class BasicBot:
    def __init__(self, api_key, api_secret, testnet: bool =True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.id_keys = ['orderId', 'algoId', 'orderListId', 'clientAlgoId']
        logger.info("Bot initialized on Testnet")
        
    def place_order(self,
            symbol: str, 
            side: str, 
            order_type: str, 
            quantity: float, 
            price: Optional[float]=None,
            stop_price: Optional[float]=None
        ) -> Tuple[Dict, Optional[int|str]]:
        try:
            logger.info(f"sending {side} {order_type} order for {symbol}...")
            params = {
                'symbol': symbol,
                'quantity': quantity,
                'side': side,
                'type': order_type
            }
        
            # Add limit order:
            if order_type == 'LIMIT':
                if price == None:
                    logger.error("Limit order requires a price")
                    return None, None
                params['price'] = format_quantity(price, precision=2) 
                params['timeInForce'] = 'GTC' # Good Till Cancelled
            elif order_type == 'STOP_MARKET':
                if stop_price == None:
                    logger.error("Stop order requires a stop price")
                    return None, None
                params['triggerprice'] = format_quantity(stop_price, precision=2)
                params['timeInForce'] = 'GTC'
            
            response = self.client.futures_create_order(**params)
            found_id = None
            for key in self.id_keys:
                if key in response and response[key]:
                    found_id = response[key]
                    logger.info(f"Order placed, {key}:{found_id}")
                    break
            if not found_id:
                logger.warning(f"No standard ID found, info dump: {response}")
            return response, found_id
        except BinanceAPIException as e:
            logger.error(f"Order failed, reason -> {e.code}:{e.message}")
            return None, None
        except BinanceRequestException as e:
            logger.warning(f"Order failed, reason -> {e}")
            return None, None
        except Exception as e:
            logger.exception(f"Order failed, reason -> {e}")
            return None, None  