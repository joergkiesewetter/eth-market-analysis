import datetime
import time

from provider.coingecko import CoinGecko

if __name__ == "__main__":

    symbol = 'ANT'
    currency = 'usd'

    coingecko_id = CoinGecko.get_id_by_symbol(symbol)

    date = datetime.date(year=2017, month=8, day=13)

    yesterday = datetime.date.today()
    yesterday -= datetime.timedelta(days=1)

    while date < yesterday:

        print(date.strftime('%Y-%m-%d') + ', ' + str(CoinGecko.get_market_cap_by_date(coingecko_id, date, currency)))

        time.sleep(1)
        date += datetime.timedelta(days=1)