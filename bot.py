from binance.client import Client
from typing import Dict, Optional
from config import logger
from binance.exceptions import BinanceAPIException, BinanceRequestException

class BasicBot:
    def __init__(self, api_key, api_secret, testnet: bool =True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        logger.info("Bot initialized on Testnet")
        
    def place_order(self,
            symbol: str, 
            side: str, 
            order_type: str, 
            quantity: int, 
            price: Optional[float]=None
        ) -> Dict:
        try:
            logger.info(f"sending {side} {order_type} order for {symbol}...")
            params = {
                'symbol': symbol,
                'quantity': quantity,
                'side': side,
                'type': order_type
            }
        
            # Add Stop limit order:
            if order_type == 'LIMIT':
                if price == None:
                    logger.error("Limit order requires a price")
                    return None
                params['price'] = price 
                params['timeInForce'] = 'GTC' # Good Till Cancelled
            
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order placed, order ID: {response['orderId']}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Order failed, reason -> {e.code}:{e.message}")
        except BinanceRequestException as e:
            logger.warning(f"Order failed, reason -> {e}")
        except Exception as e:
            logger.exception(f"Order failed, reason -> {e}")  