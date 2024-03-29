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
from util import logging

log = logging.get_custom_logger(__name__, config.LOG_LEVEL)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--etherscan-api-token',
                        dest='etherscan_api_token',
                        required=True,
                        help='the api token with which the script will query the etherscan api')

    args = parser.parse_args()

    for token in config.TOKEN:

        token_contracts = []
        for address in token['token_contracts']:
            token_contracts.append(address.lower())
        token['token_contracts'] = token_contracts

        lending_contracts = []
        for address in token['lending_contracts']:
            lending_contracts.append(address.lower())
        token['lending_contracts'] = lending_contracts

        team_accounts = []
        for address in token['team_accounts']:
            team_accounts.append(address.lower())
        token['team_accounts'] = team_accounts

        log.info('start analysis for token ' + token['symbol'])
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

        calculate_realized_market_capitalization(token)
        calculate_token_holder_stats(token)

        log.debug('--------')

    # postphone calculation of top token holders to have the other data faster
    for token in config.TOKEN:
        calculate_top_token_holder(token)

        if len(token['lending_contracts']) > 0:
            calculate_top_token_holder_normalized(token)
