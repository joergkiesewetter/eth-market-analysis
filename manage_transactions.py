import os
from datetime import datetime

from provider.etherscan import Etherscan

BASE_DIRECTORY = 'data/transactions/'


def update_token_transactions(etherscan_api_token: str, symbol: str, token_address: str):
    """

    fetches all transactions for the given token symbol. all data are fetched from etherscan.

    :return:
        Nothing
    """

    symbol_dir = BASE_DIRECTORY + symbol

    os.makedirs(symbol_dir, exist_ok=True)

    max_time = datetime.now()
    max_time = max_time.replace(hour=0, minute=0, second=0, microsecond=0)

    last_timestamp, last_block, last_hash = _get_last_transaction(symbol_dir)

    print('starting update from block: ' + str(last_block))
    if last_hash:
        print('with hash: ' + last_hash)
    print('with timestamp: ' + str(last_timestamp))

    transactions = Etherscan.get_token_trades(etherscan_api_token, token_address, last_block)

    max_time_exceeded = False

    file = None
    filename = None

    while not max_time_exceeded:

        _clear_incomplete_data(symbol_dir, transactions)

        for transaction in transactions:

            block_number = transaction['blockNumber']
            timestamp = datetime.fromtimestamp(int(transaction['timeStamp']))
            hash = transaction['hash']

            if timestamp > max_time:
                max_time_exceeded = True
                break


            act_filename = timestamp.strftime('%Y-%m-%d') + '.csv'
            if not file or act_filename != filename:
                filename = act_filename

                if file:
                    file.close()

                file = open(os.path.join(symbol_dir, filename), 'a')

            # {
            #     "blockNumber": "4620855",
            #     "timeStamp": "1511634257",
            #     "hash": "0x5c9b0f9c6c32d2690771169ec62dd648fef7bce3d45fe8a6505d99fdcbade27a",
            #     "nonce": "5417",
            #     "blockHash": "0xee385ac028bb7d8863d70afa02d63181894e0b2d51b99c0c525ef24538c44c24",
            #     "from": "0x731c6f8c754fa404cfcc2ed8035ef79262f65702",
            #     "contractAddress": "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2",
            #     "to": "0x642ae78fafbb8032da552d619ad43f1d81e4dd7c",
            #     "value": "1000000000000000000000000",
            #     "tokenName": "Maker",
            #     "tokenSymbol": "MKR",
            #     "tokenDecimal": "18",
            #     "transactionIndex": "55",
            #     "gas": "3000000",
            #     "gasPrice": "1000000000",
            #     "gasUsed": "1594668",
            #     "cumulativeGasUsed": "4047394",
            #     "input": "deprecated",
            #     "confirmations": "4924562"
            # }
            new_line = ','.join([transaction['blockNumber'],
                                 transaction['timeStamp'],
                                 transaction['hash'],
                                 transaction['nonce'],
                                 transaction['blockHash'],
                                 transaction['from'],
                                 transaction['to'],
                                 transaction['value'],
                                 transaction['tokenDecimal'],
                                 transaction['transactionIndex'],
                                 transaction['gas'],
                                 transaction['gasPrice'],
                                 transaction['gasUsed'],
                                 transaction['cumulativeGasUsed'],
                                 transaction['input'],
                                 transaction['confirmations']])

            file.write(new_line + '\n')

            last_timestamp = timestamp
            last_block = block_number
            last_hash = hash

        print('last block: ' + str(last_block))
        print('last timestamp: ' + str(last_timestamp))
        transactions = Etherscan.get_token_trades(etherscan_api_token, token_address, last_block)

        if file:
            file.flush()
            os.fsync(file.fileno())
            file.close()
            file = None


def _clear_incomplete_data(symbol_dir, transactions):
    last_file_timestamp = None
    last_file = None

    files = [f for f in os.listdir(symbol_dir) if os.path.isfile(os.path.join(symbol_dir, f))]

    # get the file with the highest timestamp
    for file in files:
        filename = file.split('.')[0]

        timestamp = datetime.strptime(filename, '%Y-%m-%d')

        if not last_file_timestamp or timestamp > last_file_timestamp:
            last_file_timestamp = timestamp
            last_file = file

    if not last_file:
        return


    first_transaction = transactions[0]
    print('removing incompleted block data')
    print('scanning for block number: ' + first_transaction['blockNumber'])
    removed_lines = 0

    new_lines = []
    with open(os.path.join(symbol_dir, last_file), 'rt') as file:

        for line in file:

            line_split = line.split(',')

            if str(line_split[0]) != str(first_transaction['blockNumber']):
                new_lines.append(line)
            else:
                removed_lines += 1

        file.flush()
        file.close()

    print('removing number of lines: ' + str(removed_lines))

    with open(os.path.join(symbol_dir, last_file), 'w') as file:
        for line in new_lines:
            file.write(line)
        file.flush()
        file.close()

    print('--------')


def _get_last_transaction(symbol_dir):

    last_file_timestamp = None
    last_file = None

    files = [f for f in os.listdir(symbol_dir) if os.path.isfile(os.path.join(symbol_dir, f))]

    # get the file with the highest timestamp
    for file in files:
        filename = file.split('.')[0]

        timestamp = datetime.strptime(filename, '%Y-%m-%d')

        if not last_file_timestamp or timestamp > last_file_timestamp:
            last_file_timestamp = timestamp
            last_file = file

    # if we don't have stored data for the given symbol
    if not last_file:
        return 0, 0, None

    # getting the last line of the file an extract the timestamp
    with open(os.path.join(symbol_dir, last_file), 'rt') as file:

        last_line = file.readlines()[-1]

        last_line = last_line.split(',')

        return datetime.fromtimestamp(int(last_line[1])), last_line[0], last_line[2]


def get_first_transaction_timestamp(symbol):

    last_file_timestamp = None

    dir = BASE_DIRECTORY + symbol

    files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

    # get the file with the highest timestamp
    for file in files:
        filename = file.split('.')[0]

        timestamp = datetime.strptime(filename, '%Y-%m-%d')

        if not last_file_timestamp or timestamp < last_file_timestamp:
            last_file_timestamp = timestamp

    return last_file_timestamp


def get_transaction_data(symbol, date):

    try:
        with open(os.path.join(BASE_DIRECTORY, symbol, date.strftime('%Y-%m-%d') + '.csv'), 'rt') as file:

            return_data = []


            for line in file:
                return_data.append(line.split(','))

            return return_data
    except:
        return []