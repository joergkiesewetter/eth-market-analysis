import os
import time
from datetime import datetime, timedelta

import config
from manage_transactions import get_first_transaction_timestamp
from provider.coingecko import CoinGecko
from util import logging

BASE_DIRECTORY = '/market-data/raw/exchange_rates/'

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)


def update_exchange_rates(symbol: str):

    os.makedirs(BASE_DIRECTORY, exist_ok=True)

    coin_gecko_id = CoinGecko.get_id_by_symbol(symbol)

    if not coin_gecko_id:
        return

    max_time = datetime.utcnow()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    path = os.path.join(BASE_DIRECTORY, symbol + '.csv')

    if not os.path.isfile(path):
        act_date = get_first_transaction_timestamp(symbol)
    else:
        act_date = _get_last_timestamp(path) + timedelta(days=1)

    log.debug('updating token exchange rates')

    with open(path, 'a') as file:
        while act_date < max_time:

            price = CoinGecko.get_exchange_rate(coin_gecko_id, act_date)

            line = ','.join([act_date.strftime('%Y-%m-%d'), str(price)])
            log.debug(line)

            file.write(line + '\n')
            file.flush()
            time.sleep(3)

            act_date += timedelta(days=1)


def _get_last_timestamp(path):
    with open(path, 'rt') as file:

        try:
            last_line = file.readlines()[-1]
            last_line = last_line.split(',')

            return datetime.strptime(last_line[0], '%Y-%m-%d')
        except:
            return datetime(year=2018, month=1, day=1)


