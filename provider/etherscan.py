import json

import requests

ETHERSCAN_BASE_URL = 'http://api.etherscan.io/api?'

class Etherscan:

    @staticmethod
    def get_token_trades(api_token, contract_id, start_block):
        url = ETHERSCAN_BASE_URL + \
              'module=account' + \
              '&action=tokentx' + \
              '&contractaddress=' + contract_id + \
              '&startblock=' + str(start_block) + \
              '&sort=asc' + \
              '&apikey=' + api_token

        response = requests.get(url)
        loaded_json = response.json()

        return loaded_json['result']