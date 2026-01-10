import os
import logging
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()
load_dotenv()
api_key = os.getenv('BINANCE_API')
secret_key = os.getenv('BINANCE_SECRET')

if not api_key or not secret_key:
    logger.critical("API Keys missing in .env")