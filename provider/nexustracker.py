from datetime import time

import requests

import config
from util import logging

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)

class NexusTracker:

    @staticmethod
    def get_exchange_rates():
        url = 'https://nexustracker.io/nxm_price'

        response = requests.get(url)

        while response.status_code != 200:
            log.warning(response.status_code)
            response = requests.get(url)
            time.sleep(1)

        json = response.json()

        if 'ETH' in json:
            return json['ETH']

        return None