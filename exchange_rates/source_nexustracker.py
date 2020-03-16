import os
from datetime import datetime

from provider.nexustracker import NexusTracker

BASE_DIRECTORY = 'data/exchange_rates/'

def update_exchange_rates(symbol: str):

    os.makedirs(BASE_DIRECTORY, exist_ok=True)

    path = os.path.join(BASE_DIRECTORY, symbol + '.csv')

    with open(path, 'w') as file:

        prices = NexusTracker.get_exchange_rates()

        for time_string in prices.keys():
            timestamp = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
            value = prices[time_string]

            file.write(','.join([time_string, str(value)]) + '\n')


