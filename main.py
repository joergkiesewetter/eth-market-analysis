import argparse
from datetime import datetime

import config
from calculate_realized_market_capitalization import calculate_realized_market_capitalization
from calculate_top_token_holder import calculate_top_token_holder
from exchange_rates import source_coin_gecko, source_nexustracker
from manage_transactions import update_token_transactions
from manage_realized_market_capitalization import update_realized_market_capitalization

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--etherscan-api-token',
                        dest='etherscan_api_token',
                        required=True,
                        help='the api token with which the script will query the etherscan api')

    parser.add_argument('--from-date',
                        dest='from_date',
                        required=False,
                        default=datetime.fromtimestamp(0).strftime('%Y-%m-%d'),
                        help='The date from which the data should be getting calculated in format %Y-%m-%d')
    args = parser.parse_args()

    for token in config.TOKEN:

        from_date = datetime.strptime(args.from_date, '%Y-%m-%d')

        update_token_transactions(args.etherscan_api_token, token['symbol'], token['address'])

        if token['source_exchange_rates'] == 'coin_gecko':
            source_coin_gecko.update_exchange_rates(token['symbol'])
        elif token['source_exchange_rates'] == 'nexustracker':
            source_nexustracker.update_exchange_rates(token['symbol'])


        update_realized_market_capitalization(token)

        #
        # calculation of results
        #

        # calculate_realized_market_capitalization(token['symbol'], from_date)
        calculate_top_token_holder(token, from_date)
