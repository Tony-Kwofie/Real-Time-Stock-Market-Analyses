import time
from extract import connect_to_api, extract_json
from config import logger


def run_producer():
    while True:
        try:
            logger.info("Starting new fetch cycle...")

            response = connect_to_api()
            records = extract_json(response)

            logger.info(f"Fetched {len(records)} records")

            # Here you would send to Kafka or DB

            logger.info("Sleeping for 90 seconds...\n")
            time.sleep(90)  # Wait 1 minute before next request

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            time.sleep(30)  # Wait before retrying


if __name__ == "__main__":
    run_producer()
