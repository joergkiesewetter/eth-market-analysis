import functools
import os
from datetime import datetime, timedelta
from heapq import nlargest

import config
import known_addresses
from manage_balances import BASE_DIRECTORY, get_first_data_timestamp
from util import logging

STORE_DIRECTORY = '/market-data/final/token_holder_stats/'

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)

def calculate_token_holder_stats(token: dict):

    symbol = token['symbol']
    symbol_file = STORE_DIRECTORY + symbol

    os.makedirs(STORE_DIRECTORY, exist_ok=True)

    max_time = datetime.utcnow()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    stop_processing = False

    date_to_process = get_first_data_timestamp(symbol)
    date_last_processed = _get_last_processed_date(symbol)
    date_to_process = max(date_to_process, date_last_processed + timedelta(days=1))

    log.debug('calculate_token_holder_stats for ' + symbol)

    if date_to_process >= max_time:
        return

    with open(symbol_file, 'a') as file:
        while not stop_processing:

            data = _get_data_to_process(token['symbol'], date_to_process)

            exchange_balance = 0
            token_contracts_balance = 0
            team_balance = 0
            remaining_accounts = list()

            for datum in data:
                if datum[0] in token['token_contracts'] or datum[0] in token['lending_contracts']:
                    token_contracts_balance += int(datum[1])

                elif datum[0] in token['team_accounts']:
                    team_balance += int(datum[1])

                elif datum[0] in known_addresses.exchange_addresses:
                    exchange_balance += int(datum[1])

                else:
                    remaining_accounts.append({
                        'account': datum[0],
                        'balance': int(datum[1]),
                    })


            remaining_accounts.sort(key=lambda element : element['balance'], reverse=True)

            top20 = list()
            top50 = list()
            top100 = list()
            top200 = list()
            retail = list()

            i = 0
            for account in remaining_accounts:

                if i < 20:
                    top20.append(account)
                elif i < 50:
                    top50.append(account)
                elif i < 100:
                    top100.append(account)
                elif i < 200:
                    top200.append(account)
                else:
                    retail.append(account)

                i += 1

            date_string = date_to_process.strftime('%Y-%m-%d')
            result = {
                'date': date_string,
                'token_contracts_balance': token_contracts_balance,
                'team_balance': team_balance,
                'exchanges_balance': exchange_balance,
                'top20': functools.reduce(lambda a, b : a + b['balance'], top20, 0),
                'top50': functools.reduce(lambda a, b: a + b['balance'], top50, 0),
                'top100': functools.reduce(lambda a, b: a + b['balance'], top100, 0),
                'top200': functools.reduce(lambda a, b: a + b['balance'], top200, 0),
                'retail': functools.reduce(lambda a, b: a + b['balance'], retail, 0),
            }

            file.write(result['date'] + ',' + \
                       str((result['token_contracts_balance'] / pow(10, 18))) + ',' + \
                       str((result['team_balance'] / pow(10, 18))) + ',' + \
                       str((result['exchanges_balance'] / pow(10, 18))) + ',' + \
                       str((result['top20'] / pow(10, 18))) + ',' + \
                       str((result['top50'] / pow(10, 18))) + ',' + \
                       str((result['top100'] / pow(10, 18))) + ',' + \
                       str((result['top200'] / pow(10, 18))) + ',' + \
                       str((result['retail'] / pow(10, 18))) + '\n')
            file.flush()

            log.debug('calculate_token_holder_stats for ' + date_string)

            date_to_process += timedelta(days=1)

            if date_to_process >= max_time:
                stop_processing = True


def _get_last_processed_date(symbol):
    symbol_file = STORE_DIRECTORY + symbol

    last_file_timestamp = '1970-01-01'

    if not os.path.exists(symbol_file):
        return datetime.utcfromtimestamp(0)

    with open(symbol_file, 'r') as file:

        for line in file:
            line_parts = line.split(',')

            last_file_timestamp = line_parts[0]

    return datetime.strptime(last_file_timestamp, '%Y-%m-%d')


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


def _get_top_holder(token):

    max_time = datetime.utcnow()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

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

        if date_to_process >= max_time:
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

