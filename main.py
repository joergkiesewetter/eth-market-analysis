import argparse

import config
from calculate_realized_market_capitalization import calculate_realized_market_capitalization
from manage_exchange_rates import update_exchange_rates
from manage_transactions import update_token_transactions
from manage_realized_market_capitalization import update_realized_market_capitalization

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--etherscan-api-token',
                        dest='etherscan_api_token',
                        required=True,
                        help='the api token with which the script will query the etherscan api')

    args = parser.parse_args()

    for token in config.TOKEN:

        update_token_transactions(args.etherscan_api_token, token['symbol'], token['address'])

        update_exchange_rates(token['symbol'])

        update_realized_market_capitalization(token['symbol'], token.get('init_price'))

        calculate_realized_market_capitalization(token['symbol'])