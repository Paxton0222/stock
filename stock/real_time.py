from typing import List
import twstock
import requests
import json


def stock(code: str | List[str]) -> dict:  # 盤中即時報價
    if type(code) == int:
        code = str(code)
    stock = twstock.realtime.get(code)

    def transform_data(stock: dict) -> dict:
        real_time = stock["realtime"]
        info = stock["info"]
        latest_trade_price = real_time["latest_trade_price"]  # 即時報價
        five_price = real_time["best_bid_price"]  # 五檔報價

        return {
            "code": info["code"],
            "name": info["name"],
            "time": info["time"],
            "timestamp": stock["timestamp"],
            "price": {
                "now": (
                    latest_trade_price if latest_trade_price != "-" else five_price[0]
                ),
                "open": real_time["open"],
                "high": real_time["high"],
                "low": real_time["low"],
            },
        }

    def multiple_data_to_list(stock: dict) -> dict:
        del stock["success"]
        return [stock[key] for i, key in enumerate(stock)]

    if type(code) == str:
        return [transform_data(stock)]
    else:
        return [transform_data(data) for data in multiple_data_to_list(stock)]


def index():  # 取得台股指數報價
    index_url = "https://mis.twse.com.tw/stock/data/mis_ohlc_TSE.txt"
    futures_index_url = "https://mis.twse.com.tw/stock/data/futures_side.txt"
    index_req = json.loads(requests.get(index_url).text)
    futures_index_req = json.loads(requests.get(futures_index_url).text)
    return {"index": index_req, "futures_index": futures_index_req}
