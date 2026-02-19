import os
import requests
from config import logger, url


def connect_to_api():
    stocks = ["TSLA", "MSFT", "GOOGL"]
    json_response = []

    api_key = os.getenv("API_KEY")

    if not api_key:
        logger.error("API_KEY is missing from environment variables")
        return []

    for stock in stocks:
        querystring = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": stock,
            "outputsize": "compact",
            "interval": "5min",
            "datatype": "json",
            "apikey": api_key,
        }

        try:
            response = requests.get(
                url,
                params=querystring,
                timeout=10,
            )

            response.raise_for_status()
            data = response.json()

            # 🚨 Alpha Vantage rate limit
            if "Note" in data:
                logger.warning(f"API limit reached for {stock}: {data['Note']}")
                continue

            # 🚨 Invalid API key
            if "Error Message" in data:
                logger.warning(f"Invalid API call for {stock}: {data['Error Message']}")
                continue

            # 🚨 Unexpected structure
            if "Time Series (5min)" not in data:
                logger.warning(f"No time series data returned for {stock}: {data}")
                continue

            logger.info(f"{stock} stock successfully loaded")
            json_response.append(data)

        except requests.exceptions.RequestException as e:
            logger.error(f"HTTP error for stock {stock}: {e}")
            continue

        except Exception as e:
            logger.error(f"Unexpected error for stock {stock}: {e}")
            continue

    return json_response


def extract_json(response):
    records = []

    for data in response:
        try:
            symbol = data["Meta Data"]["2. Symbol"]
            time_series = data["Time Series (5min)"]

            for date_str, metrics in time_series.items():
                record = {
                    "symbol": symbol,
                    "date": date_str,
                    "open": float(metrics["1. open"]),
                    "high": float(metrics["2. high"]),
                    "low": float(metrics["3. low"]),
                    "close": float(metrics["4. close"]),
                }

                records.append(record)

        except KeyError as e:
            logger.warning(f"Missing expected key in response: {e}")
            continue

        except Exception as e:
            logger.error(f"Error extracting JSON data: {e}")
            continue

    return records
