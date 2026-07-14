import argparse
import logging

from bot.logging_config import setup_logger
from bot.validators import validate_inputs
from bot.orders import place_order


logger = logging.getLogger(__name__)


def main():

    # Initialize logger
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )


    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )


    args = parser.parse_args()


    try:

        logger.info("CLI request received")

        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )


        print("\n===== ORDER REQUEST =====")

        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")


        response = place_order(
            args.symbol,
            args.side,
            args.quantity,
            args.type,
            args.price
        )


        print("\n===== ORDER RESPONSE =====")


        print(
            "Order ID:",
            response.get("orderId")
        )


        print(
            "Status:",
            response.get("status")
        )


        print(
            "Executed Quantity:",
            response.get("executedQty")
        )


        print(
            "Average Price:",
            response.get("avgPrice")
        )


        print("\nOrder placed successfully!")

        logger.info(
            f"Order completed successfully | ID: {response.get('orderId')}"
        )


    except Exception as e:

        logger.error(
            f"CLI Error: {e}"
        )

        print(
            f"\nOrder failed: {e}"
        )


if __name__ == "__main__":
    main()