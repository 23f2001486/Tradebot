import logging


def setup_logger():
    """
    Configure and return the application logger.
    """

    logging.basicConfig(
        filename="trading_bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a"
    )

    return logging.getLogger(__name__)