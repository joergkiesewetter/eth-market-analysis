import os
from datetime import datetime, timedelta
from heapq import nlargest

import config
from manage_balances import BASE_DIRECTORY
from manage_realized_market_capitalization import get_first_data_timestamp
from util import logging

STORE_DIRECTORY = '/data/final/top_token_holder_normalized/'

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)

def calculate_top_token_holder_normalized(token: dict):

    symbol = token['symbol']
    symbol_dir = STORE_DIRECTORY + symbol + '/'

    os.makedirs(symbol_dir, exist_ok=True)

    max_time = datetime.utcnow()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    top_holder_date = get_first_data_timestamp(symbol)
    date_last_processed = datetime.utcnow()
    date_last_processed = date_last_processed.replace(hour=0, minute=0, second=0, microsecond=0)
    date_last_processed -= timedelta(days=1)
    top_holder_date = max(top_holder_date, date_last_processed)

    stop_processing_date = False

    log.debug('calculate_top_token_holder_normalized for ' + symbol)

    while not stop_processing_date:

        log.debug('calculate_top_token_holder_normalized ' + top_holder_date.strftime('%Y-%m-%d'))
        
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

            if date_to_process >= max_time:
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
        return datetime.utcnow() - timedelta(days=2)

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

    date_to_process = date - timedelta(days=30)

    stop_processing = False
    token_balances = {}

    while not stop_processing:

        data = _get_data_to_process(token['symbol'], date_to_process)

        for line in data:
            value = float(line[2])
            if value > 1e20:

                if line[0] not in token_balances.keys():
                    token_balances[line[0]] = list()

                token_balances[line[0]].append(value)

        date_to_process += timedelta(days=1)

        if date_to_process >= date:
            stop_processing = True

    for holder in token_balances.keys():

        if len(token_balances[holder]) <= 0:
            token_balances[holder] = 0
            continue

        token_balances[holder] = sum(token_balances[holder]) / len(token_balances[holder])

    return nlargest(amount, token_balances, token_balances.get)


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
                    'balance': (int(datum[2]) / pow(10, 18)),
                })

                found = True
                break

        if not found:
            return_data.append({
                'holder': holder,
                'balance': 0
            })

    return return_data

