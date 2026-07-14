import os
import logging

from dotenv import load_dotenv
from binance.client import Client


logger = logging.getLogger(__name__)


load_dotenv()


API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def get_client():
    """
    Create and return Binance Futures Testnet client.
    """

    logger.info("Initializing Binance client...")

    if not API_KEY or not API_SECRET:
        logger.error("API_KEY or API_SECRET missing from environment variables.")
        raise ValueError(
            "API_KEY or API_SECRET not found. Please check your .env file."
        )

    try:
        client = Client(
            api_key=API_KEY,
            api_secret=API_SECRET,
            testnet=True
        )

        logger.info("Binance Futures Testnet client created successfully.")

        return client

    except Exception as e:
        logger.error(f"Failed to create Binance client: {e}")
        raise