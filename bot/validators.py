import logging

logger = logging.getLogger(__name__)


def validate_symbol(symbol):
    """
    Validate the trading symbol.
    """

    logger.info(f"Validating symbol: {symbol}")

    if not isinstance(symbol, str) or not symbol.strip():
        logger.warning("Invalid symbol provided.")
        raise ValueError("Symbol must be a non-empty string.")

    return True


def validate_side(side):
    """
    Validate order side.
    """

    logger.info(f"Validating order side: {side}")

    if not isinstance(side, str) or side.upper() not in ("BUY", "SELL"):
        logger.warning(f"Invalid order side: {side}")
        raise ValueError("Side must be either BUY or SELL.")

    return True


def validate_order_type(order_type):
    """
    Validate order type.
    """

    logger.info(f"Validating order type: {order_type}")

    if not isinstance(order_type, str) or order_type.upper() not in ("MARKET", "LIMIT"):
        logger.warning(f"Invalid order type: {order_type}")
        raise ValueError("Order type must be MARKET or LIMIT.")

    return True


def validate_quantity(quantity):
    """
    Validate quantity.
    """

    logger.info(f"Validating quantity: {quantity}")

    if not isinstance(quantity, (int, float)):
        logger.warning("Quantity is not numeric.")
        raise ValueError("Quantity must be a number.")

    if quantity <= 0:
        logger.warning("Quantity must be greater than zero.")
        raise ValueError("Quantity must be greater than 0.")

    return True


def validate_price(order_type, price):
    """
    Validate price only for LIMIT orders.
    """

    logger.info(
        f"Validating price: {price} for order type: {order_type}"
    )

    if order_type.upper() == "LIMIT":

        if price is None:
            logger.warning("LIMIT order missing price.")
            raise ValueError("Price is required for LIMIT orders.")

        if not isinstance(price, (int, float)):
            logger.warning("Price is not numeric.")
            raise ValueError("Price must be a number.")

        if price <= 0:
            logger.warning("Price must be greater than zero.")
            raise ValueError("Price must be greater than 0.")

    return True


def validate_inputs(symbol, side, order_type, quantity, price=None):
    """
    Validate all user inputs before placing an order.
    """

    logger.info("Starting input validation...")

    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(order_type, price)

        logger.info("All inputs validated successfully.")

        return True

    except ValueError as e:
        logger.error(f"Input validation failed: {e}")
        raise