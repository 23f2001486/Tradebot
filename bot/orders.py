import logging
from bot.client import get_client


logger = logging.getLogger(__name__)


def place_order(symbol, side, quantity, order_type, price=None):
    """
    Place a MARKET or LIMIT order on Binance Futures Testnet.
    """

    logger.info(
        f"Placing {order_type.upper()} order | Symbol: {symbol}, "
        f"Side: {side}, Quantity: {quantity}, Price: {price}"
    )

    client = get_client()

    try:
        if order_type.upper() == "MARKET":

            logger.info("Creating MARKET order...")

            response = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )

            logger.info(
                f"MARKET order placed successfully | Order ID: {response.get('orderId')}"
            )

        elif order_type.upper() == "LIMIT":

            if price is None:
                logger.warning("LIMIT order attempted without price.")
                raise ValueError("Price is required for LIMIT orders.")

            logger.info("Creating LIMIT order...")

            response = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(
                f"LIMIT order placed successfully | Order ID: {response.get('orderId')}"
            )

        else:
            logger.warning(f"Invalid order type received: {order_type}")
            raise ValueError("Invalid order type. Use MARKET or LIMIT.")

        return response


    except Exception as e:
        logger.error(
            f"Error placing order | Symbol: {symbol}, "
            f"Side: {side}, Type: {order_type}, Error: {e}"
        )

        return None