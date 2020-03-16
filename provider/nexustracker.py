from datetime import time

import requests


class NexusTracker:

    @staticmethod
    def get_exchange_rates():
        url = 'https://nexustracker.io/nxm_price'

        response = requests.get(url)

        while response.status_code != 200:
            print(response.status_code)
            response = requests.get(url)
            time.sleep(1)

        json = response.json()

        if 'ETH' in json:
            return json['ETH']

        return None