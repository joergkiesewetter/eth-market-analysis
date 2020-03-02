import os
from datetime import datetime, timedelta
from heapq import nlargest

from manage_realized_market_capitalization import BASE_DIRECTORY, get_first_data_timestamp, get_last_data_timestamp


def calculate_top_token_holder(token: dict, from_date: datetime):

    max_time = datetime.now()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    stop_processing = False

    date_to_process = get_first_data_timestamp(token['symbol'])
    date_to_process = max(date_to_process, from_date)

    token_holder = _get_top_holder(token, get_last_data_timestamp(token['symbol']), 100)

    print('--------')
    print(token['symbol'])

    print('date,' + ','.join(token_holder))
    while not stop_processing:

        data = _get_data_to_process(token['symbol'], date_to_process)

        result = _analyse_data(token['symbol'], data, date_to_process, token_holder)

        final_string = ''
        for datum in result:
            final_string += ',' + str(datum['balance'])
        print(date_to_process.strftime('%Y-%m-%d') + final_string)
        # print(date_to_process.strftime('%Y-%m-%d') + ',' + str(result['num_coins']) + ',' + str(
        #     result['not_moved_coins']) + ',' + str(result['realized_market_cap']) + ',' + str(result['coins_older_1y']))

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


def _get_top_holder(token, date, amount):

    data = _get_data_to_process(token['symbol'], date)

    token_balances = {}

    for line in data:
        if line[0] not in token['known_contracts']:
            token_balances[line[0]] = float(line[1])

    top_holder = nlargest(amount, token_balances, key=token_balances.get)

    # for account in top_holder:
    #     print(account, ":", token_balances.get(account))

    return top_holder


def _analyse_data(symbol, data, date, token_holder):

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

