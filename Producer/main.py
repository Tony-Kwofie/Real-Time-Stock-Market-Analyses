from extract import connect_to_api, extract_json


def main():
    response = connect_to_api()

    data = extract_json(response)

    for stock in data:
        results = {
            "date": stock["date"],
            "symbol": stock["symbol"],
            "open": stock["open"],
            "high": stock["high"],
            "low": stock["low"],
            "close": stock["close"],
        }

        print(results)

    return None


if __name__ == "__main__":
    main()
