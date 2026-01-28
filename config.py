import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY= os.getenv("BINANCE_API_SECRET")

BASE_URL = "https://testnet.binancefuture.com"

if not API_KEY or not SECRET_KEY:
    raise RuntimeError("API key/secret not found in environment variables")
