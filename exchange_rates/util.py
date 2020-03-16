import os
from datetime import datetime


def get_local_exchange_rate(symbol, requested_time):

    path = os.path.join('data/exchange_rates', symbol + '.csv')

    with open(path) as file:

        last_price = 0
        for line in file:

            line_split = line.split(',')
            line_time = _strptime(line_split[0])

            if line_time <= requested_time:
                last_price = line_split[1]
            else:
                break

        return float(last_price.strip())



def get_first_market_price_date(symbol):

    with open('data/exchange_rates/' + symbol + '.csv') as file:

        for line in file:

            line_parts = line.split(',')

            if line_parts[1].strip() == 'None':
                continue

            return _strptime(line_parts[0])


def _strptime(date_string: str):
    for fmt in ('%Y-%m-%d', '%Y-%m-%d %H:%M:%S'):
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')