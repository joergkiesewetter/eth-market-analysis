import json
import os
from datetime import datetime, timedelta

import config
from exchange_rates.util import get_local_exchange_rate, get_first_market_price_date
from manage_transactions import get_first_transaction_timestamp, get_transaction_data
from util import logging

BASE_DIRECTORY = '/data/raw/realized_data/'

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)


def update_realized_market_capitalization(token):

    symbol = token['symbol']
    init_price = token.get('init_price')

    symbol_dir = BASE_DIRECTORY + symbol

    os.makedirs(symbol_dir, exist_ok=True)

    max_time = datetime.utcnow()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    stop_processing = False

    date_to_process = _get_next_time_to_process(symbol, symbol_dir)

    if date_to_process >= max_time:
        stop_processing = True

    state = _load_state(symbol_dir, date_to_process)

    log.debug('updating realized market cap for ' + symbol)

    while not stop_processing:

        transactions = get_transaction_data(symbol, date_to_process)

        log.debug('processing: ' + str(date_to_process))

        for transaction in transactions:
            block_number = transaction[0]
            timestamp = transaction[1]
            hash = transaction[2]
            nonce = transaction[3]
            block_hash = transaction[4]
            from_address = transaction[5]
            to_address = transaction[6]
            value = int(transaction[7])
            token_decimal = transaction[8]
            transaction_index = transaction[9]
            gas = transaction[10]
            gas_price = transaction[11]
            gas_used = transaction[12]
            cumulative_gas_used = transaction[13]
            input = transaction[14]
            confirmations = transaction[15]

            if int(timestamp) < get_first_market_price_date(symbol).timestamp():

                if init_price:
                    price = init_price
                else:
                    price = 0
            else:
                price = get_local_exchange_rate(symbol, datetime.utcfromtimestamp(int(timestamp)))

            if from_address in state.keys():
                from_account = state[from_address]
            else:
                from_account = None

            if to_address in state.keys():
                to_account = state[to_address]
            else:
                to_account = {
                    'balance': 0,
                    'data': [],
                }
                state[to_address] = to_account

            #
            # add transaction to the from-account
            #

            if from_account:

                remaining_value = value

                while remaining_value > 0:
                    try:
                        from_amount = from_account['data'][0][1]
                    except Exception:
                        log.debug(transaction)
                        break


                    if remaining_value < from_amount:
                        from_account['data'][0][1] -= remaining_value
                        remaining_value = 0
                        from_account['data'][0][2] = price

                    else:
                        remaining_value -= from_amount
                        from_account['data'] = from_account['data'][1:]

                from_balance = 0

                for entry in from_account['data']:
                    from_balance += int(entry[1])

                from_account['balance'] = from_balance

            #
            # add transaction to the to-account
            #

            to_account['data'].append([timestamp, value, price])

            to_balance = 0

            for entry in to_account['data']:
                to_balance += int(entry[1])

            to_account['balance'] = to_balance



        # all transactions are processed, saving state to a file
        _save_state(symbol_dir, date_to_process, state)

        date_to_process = date_to_process + timedelta(days=1)

        if date_to_process >= max_time:
            stop_processing = True


def _get_next_time_to_process(symbol, symbol_dir):
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

    if last_file_timestamp:
        return last_file_timestamp + timedelta(days=1)
    else:
        return get_first_transaction_timestamp(symbol)


def _load_state(symbol_dir, date_to_process):

    date_to_load = date_to_process - timedelta(days=1)

    path = os.path.join(symbol_dir, date_to_load.strftime('%Y-%m-%d') + '.csv')

    if not os.path.isfile(path):
        return {}

    return_data = {}

    with open(path, 'rt') as file:

        for line in file:

            line_parts = line.split(';')

            return_data[line_parts[0]] = {
                'balance': line_parts[1],
                'data': json.loads(line_parts[2])
            }

        return return_data


def _save_state(symbol_dir, date_to_process, state):

    path = os.path.join(symbol_dir, date_to_process.strftime('%Y-%m-%d') + '.csv')

    if os.path.isfile(path):
        os.remove(path)

    with open(path, 'at') as file:
        for key, value in state.items():
            if len(value['data']) > 0:
                file.write(key + ';' + str(value['balance']) + ';' + json.dumps(value['data']) + '\n')


def get_first_data_timestamp(symbol):

    symbol_dir = BASE_DIRECTORY + symbol

    last_file_timestamp = None

    files = [f for f in os.listdir(symbol_dir) if os.path.isfile(os.path.join(symbol_dir, f))]

    # get the file with the highest timestamp
    for file in files:
        filename = file.split('.')[0]

        timestamp = datetime.strptime(filename, '%Y-%m-%d')

        if not last_file_timestamp or timestamp < last_file_timestamp:
            last_file_timestamp = timestamp

    return last_file_timestamp


def get_last_data_timestamp(symbol):

    symbol_dir = BASE_DIRECTORY + symbol

    last_file_timestamp = None

    files = [f for f in os.listdir(symbol_dir) if os.path.isfile(os.path.join(symbol_dir, f))]

    # get the file with the highest timestamp
    for file in files:
        filename = file.split('.')[0]

        timestamp = datetime.strptime(filename, '%Y-%m-%d')

        if not last_file_timestamp or timestamp > last_file_timestamp:
            last_file_timestamp = timestamp

    return last_file_timestamp