import time
from extract import connect_to_api, extract_json
from producer_setup import init_producer
from config import logger


def main():
    producer = init_producer()

    while True:
        try:
            logger.info("Fetching stock data...")

            response = connect_to_api()
            records = extract_json(response)

            logger.info(f"Sending {len(records)} records to Kafka...")

            for record in records:
                producer.send("stock_analysis", value=record)

            producer.flush()

            logger.info("Sleeping 60 seconds...\n")
            time.sleep(60)

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            time.sleep(30)


if __name__ == "__main__":
    main()
