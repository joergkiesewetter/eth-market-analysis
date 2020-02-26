import json
import os
from datetime import date, datetime, timedelta

from manage_realized_market_capitalization import BASE_DIRECTORY


def calculate_realized_market_capitalization(symbol: str):

    symbol_dir = BASE_DIRECTORY + symbol

    max_time = datetime.now()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    stop_processing = False

    date_to_process = _get_first_data_timestamp(symbol_dir)

    print('--------')
    print(symbol)

    while not stop_processing:

        data = _get_data_to_process(symbol, date_to_process)

        result = _analyse_data(symbol, data, date_to_process)

        print(date_to_process.strftime('%Y-%m-%d') + ',' +
              str(result['num_coins']) + ',' +
              str(result['not_moved_coins']) + ',' +
              str(result['realized_market_cap']) + ',' +
              str(result['coins_older_1y']))

        date_to_process += timedelta(days=1)

        if date_to_process >= max_time:
            stop_processing = True


##
# return [[<holder_address>, <balance>, <token data>], ...]
#
def _get_data_to_process(symbol, date):
    try:
        with open(os.path.join(BASE_DIRECTORY, symbol, date.strftime('%Y-%m-%d') + '.csv'), 'rt') as file:

            return_data = []

            for line in file:
                return_data.append(line.split(';'))

            return return_data
    except:
        return []


def _analyse_data(symbol, data, date_to_process) :

    return_data = {
        'num_coins': 0,
        'not_moved_coins': 0,
        'realized_market_cap': 0,
        'coins_older_1y': 0,
    }

    market_entry_date = _get_first_market_price_date(symbol)

    date_1y = _add_years(date_to_process, -1)

    for line in data:

        for coin_data in json.loads(line[2]):

            # calculate total amount of coins
            return_data['num_coins'] += coin_data[1]

            # calculate number of coins never traded after market entry
            if int(coin_data[0]) < market_entry_date.timestamp():
                return_data['not_moved_coins'] += coin_data[1]

            # calculate total realized market cap
            amount_coins = coin_data[1] / pow(10, 18)

            return_data['realized_market_cap'] += amount_coins * coin_data[2]

            # calculate number of coins not moved for more than a year
            if int(coin_data[0]) < date_1y.timestamp():
                return_data['coins_older_1y'] += coin_data[1]

    return_data['num_coins'] /= pow(10, 18)
    return_data['not_moved_coins'] /= pow(10, 18)
    return_data['coins_older_1y'] /= pow(10, 18)

    return return_data


def _add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


def _get_first_market_price_date(symbol):

    with open('data/exchange_rates/' + symbol + '.csv') as file:

        for line in file:

            line_parts = line.split(',')

            if line_parts[1].strip() != 'None':
                return datetime.strptime(line_parts[0], '%Y-%m-%d')


def _get_first_data_timestamp(symbol_dir):

    last_file_timestamp = None

    files = [f for f in os.listdir(symbol_dir) if os.path.isfile(os.path.join(symbol_dir, f))]

    # get the file with the highest timestamp
    for file in files:
        filename = file.split('.')[0]

        timestamp = datetime.strptime(filename, '%Y-%m-%d')

        if not last_file_timestamp or timestamp < last_file_timestamp:
            last_file_timestamp = timestamp

    return last_file_timestamp