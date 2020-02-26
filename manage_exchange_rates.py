import os
import time
from datetime import datetime, timedelta

from manage_transactions import get_first_transaction_timestamp
from provider.coingecko import CoinGecko

BASE_DIRECTORY = 'data/exchange_rates/'

def update_exchange_rates(symbol: str):

    os.makedirs(BASE_DIRECTORY, exist_ok=True)

    coin_gecko_id = CoinGecko.get_id_by_symbol(symbol)

    max_time = datetime.now()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    path = os.path.join(BASE_DIRECTORY, symbol + '.csv')

    if not os.path.isfile(path):
        act_date = get_first_transaction_timestamp(symbol)
    else:
        act_date = _get_last_timestamp(path) + timedelta(days=1)

    with open(path, 'a') as file:
        while act_date < max_time:

            price = CoinGecko.get_exchange_rate(coin_gecko_id, act_date)

            file.write(','.join([act_date.strftime('%Y-%m-%d'), str(price)]) + '\n')
            file.flush()
            time.sleep(1)

            act_date += timedelta(days=1)


def _get_last_timestamp(path):
    with open(path, 'rt') as file:

        try:
            last_line = file.readlines()[-1]
            last_line = last_line.split(',')

            return datetime.strptime(last_line[0], '%Y-%m-%d')
        except:
            return datetime(year=2018, month=1, day=1)


def get_local_exchange_rate(symbol, timestamp):
    time_string = timestamp.strftime('%Y-%m-%d')
    path = os.path.join('data/exchange_rates', symbol + '.csv')

    with open(path) as file:

        for line in file:

            line_split = line.split(',')

            if line_split[0] == time_string:
                if line_split[1].strip() == 'None':
                    return 0
                else:
                    return float(line_split[1].strip())

    return 0


def get_first_market_price_date(symbol):

    with open('data/exchange_rates/' + symbol + '.csv') as file:

        for line in file:

            line_parts = line.split(',')

            if line_parts[1].strip() != 'None':
                return datetime.strptime(line_parts[0], '%Y-%m-%d')