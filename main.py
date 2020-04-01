import argparse
from datetime import datetime

import config
from calculate_realized_market_capitalization import calculate_realized_market_capitalization
from calculate_token_holder_stats import calculate_token_holder_stats
from calculate_top_token_holder import calculate_top_token_holder
from calculate_top_token_holder_normalized import calculate_top_token_holder_normalized
from exchange_rates import source_coin_gecko, source_nexustracker
from manage_balances import update_balances
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

        if token['source_exchange_rates'] == 'coin_gecko':
            source_coin_gecko.update_exchange_rates(token['symbol'])
        elif token['source_exchange_rates'] == 'nexustracker':
            source_nexustracker.update_exchange_rates(token['symbol'])


        update_realized_market_capitalization(token)
        update_balances(token)

        #
        # calculation of results
        #

        calculate_realized_market_capitalization(token['symbol'])
        calculate_token_holder_stats(token)

    # postphone calculation of top token holders to have the other data faster
    for token in config.TOKEN:
        calculate_top_token_holder(token)
        calculate_top_token_holder_normalized(token)
