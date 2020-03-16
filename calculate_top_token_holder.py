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

    token_holder_date = datetime.now()
    # token_holder_date = token_holder_date.replace(year=2020, month=3, day=1, hour=0, minute=0, second=0, microsecond=0)
    token_holder = _get_top_holder(token, token_holder_date, 100)

    print('--------')
    print(token['symbol'])

    print('accounts,' + ','.join(token_holder))
    print('category')
    while not stop_processing:

        data = _get_data_to_process(token['symbol'], date_to_process)

        result = _analyse_data(data, token_holder)

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

    max_time = datetime.now()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    date_to_process = get_first_data_timestamp(token['symbol'])

    top_holder = list()
    stop_processing = False

    while not stop_processing:

        data = _get_data_to_process(token['symbol'], date_to_process)

        token_balances = {}

        for line in data:
            value = float(line[1])
            if line[0] not in token['known_contracts'] and value > 1e20:
                token_balances[line[0]] = value

        daily_top_holder = nlargest(50, token_balances, key=token_balances.get)
        top_holder.extend(daily_top_holder)

        # for account in top_holder:
        #     print(account, ":", token_balances.get(account))

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

