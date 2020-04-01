import os
from datetime import datetime

import config
from provider.nexustracker import NexusTracker
from util import logging

BASE_DIRECTORY = '/data/raw/exchange_rates/'

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)

def update_exchange_rates(symbol: str):

    os.makedirs(BASE_DIRECTORY, exist_ok=True)

    path = os.path.join(BASE_DIRECTORY, symbol + '.csv')

    log.debug('updating token exchange rates for ' + symbol)

    with open(path, 'w') as file:

        prices = NexusTracker.get_exchange_rates()

        for time_string in prices.keys():
            timestamp = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
            value = prices[time_string]

            file.write(','.join([time_string, str(value)]) + '\n')


