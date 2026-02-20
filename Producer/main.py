import random
import time
from producer_setup import init_producer


def generate_mock_data():
    stocks = ["TSLA", "MSFT", "GOOGL"]
    return {
        "symbol": random.choice(stocks),
        "price": round(random.uniform(100, 500), 2),
        "timestamp": time.time(),
    }


def main():
    producer = init_producer()

    while True:
        mock_record = generate_mock_data()

        print("Sending:", mock_record)
        producer.send("stock_analysis", value=mock_record)
        producer.flush()

        time.sleep(2)


if __name__ == "__main__":
    main()


# import time
# from extract import connect_to_api, extract_json
# from config import logger
# from producer_setup import topic, init_producer
#

# def run_producer():
# while True:
# try:
# logger.info("Starting new fetch cycle...")
#
# response = connect_to_api()
# records = extract_json(response)
#
# producer = init_producer()
#
#
#
# logger.info(f"Fetched {len(records)} records")
#
# Here you would send to Kafka or DB
#
# logger.info("Sleeping for 90 seconds...\n")
# time.sleep(90)  # Wait 1 minute before next request
#
# except Exception as e:
# logger.error(f"Unexpected error: {e}")
# time.sleep(30)  # Wait before retrying
#
#
# if __name__ == "__main__":
# run_producer()
#
