import os
from datetime import datetime, timedelta
from heapq import nlargest

import config
from manage_balances import BASE_DIRECTORY
from manage_realized_market_capitalization import get_first_data_timestamp
from util import logging

STORE_DIRECTORY = '/data/final/top_token_holder/'

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)

def calculate_top_token_holder(token: dict):

    symbol = token['symbol']
    symbol_dir = STORE_DIRECTORY + symbol + '/'

    os.makedirs(symbol_dir, exist_ok=True)

    max_time = datetime.now()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    top_holder_date = get_first_data_timestamp(symbol)
    date_last_processed = _get_last_processed_date(symbol_dir)
    top_holder_date = max(top_holder_date, date_last_processed)

    stop_processing_date = False

    log.debug('calculate_top_token_holder for ' + symbol)

    while not stop_processing_date:

        log.debug('calculate_top_token_holder ' + top_holder_date.strftime('%Y-%m-%d'))

        stop_processing = False

        date_to_process = get_first_data_timestamp(symbol)

        token_holder = _get_top_holder(token, top_holder_date, 100)

        final_lines = []
        while not stop_processing:

            data = _get_data_to_process(token['symbol'], date_to_process)

            result = _analyse_data(data, token_holder)

            final_string = ''
            for datum in result:
                final_string += ',' + str(datum['balance'])

            final_lines.append(date_to_process.strftime('%Y-%m-%d') + final_string)

            date_to_process += timedelta(days=1)

            if date_to_process >= top_holder_date:
                stop_processing = True

        with open(symbol_dir + '/' + top_holder_date.strftime('%Y-%m-%d'), 'w') as file:
            file.write('accounts,' + ','.join(token_holder) + '\n')

            for line in final_lines:
                file.write(line + '\n')
            file.flush()

        top_holder_date += timedelta(days=1)

        if top_holder_date >= max_time:
            stop_processing_date = True


def _get_last_processed_date(symbol_dir):

    last_file_timestamp = None
    last_file = None

    files = [f for f in os.listdir(symbol_dir) if os.path.isfile(os.path.join(symbol_dir, f))]

    # get the file with the highest timestamp
    for file in files:
        filename = file.split('.')[0]

        timestamp = datetime.strptime(filename, '%Y-%m-%d')

        if not last_file_timestamp or timestamp > last_file_timestamp:
            last_file_timestamp = timestamp
            last_file = file

    # if we don't have stored data for the given symbol
    if not last_file:
        return datetime.now() - timedelta(days=2)

    return last_file_timestamp


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


def _get_top_holder(token, date, amount):

    date_to_process = get_first_data_timestamp(token['symbol'])

    top_holder = list()
    stop_processing = False

    while not stop_processing:

        data = _get_data_to_process(token['symbol'], date_to_process)

        token_balances = {}

        for line in data:
            value = float(line[1])
            if value > 1e20:
                token_balances[line[0]] = value

        daily_top_holder = nlargest(50, token_balances, key=token_balances.get)
        top_holder.extend(daily_top_holder)

        # for account in top_holder:
        #     log.debug(account, ":", token_balances.get(account))

        date_to_process += timedelta(days=1)

        if date_to_process >= date:
            stop_processing = True

    return _remove_duplicates(top_holder)


def _remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def _analyse_data(data, token_holder):

    return_data = []

    for holder in token_holder:

        found = False
        for datum in data:

            if holder == datum[0]:
                return_data.append({
                    'holder': holder,
                    'balance': (int(datum[1]) / pow(10, 18)),
                })

                found = True
                break

        if not found:
            return_data.append({
                'holder': holder,
                'balance': 0
            })

    return return_data
