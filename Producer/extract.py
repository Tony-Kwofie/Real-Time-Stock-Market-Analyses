import requests
from config import logger, headers, url


def connect_to_api():
    stocks = ["TESLA", "MSFT", "GOOGL"]
    json_response = []

    for stock in stocks:
        querystring = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": stock,
            "outputsize": "compact",
            "interval": "5min",
            "datatype": "json",
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()

            data = response.json()
            logger.info(f"{stock} Stock successfully loaded")

            json_response.append(data)
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error on stock {stock}: {e}")
            break

    return json_response


def extract_json(response):
    records=[]
    
    for data in response:
        symbol = data['meta data']['2. symbol']
        
        for data_str, metrics in data ['TIme series(5min)'].iterm:
            record = {
                "symbol" = symbol,
                "date" = data_str,
                "open" = metrics["1. open"],
                "close" = metrics["4. close"],
                "high" = metrics["2. high"],
                "low" = metrics["3. low"]
                
            }
            
            records.append[record] 
            
    return records             