import time

import requests

import config
from util import logging

COIN_GECKO_BASE_URL = 'https://api.coingecko.com/api/v3/'

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)

class CoinGecko:

    @staticmethod
    def get_id_by_symbol(symbol):
        url = COIN_GECKO_BASE_URL + 'coins/list'

        response = requests.get(url)
        json = response.json()

        symbol_lower = symbol.lower()

        for token in json:
            if token['symbol'].lower() == symbol_lower:
                return token['id']

        return None

    @staticmethod
    def get_exchange_rate(coin_gecko_id, timestamp):

        url = COIN_GECKO_BASE_URL + 'coins/' + coin_gecko_id + '/history?date=' + timestamp.strftime('%d-%m-%Y')

        response = requests.get(url)

        while response.status_code != 200:
            log.warning(response.status_code)
            response = requests.get(url)
            time.sleep(1)


        json = response.json()

        if 'market_data' in json:
            return json['market_data']['current_price']['usd']

        return None
