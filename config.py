import logging

LOG_LEVEL = logging.DEBUG

TOKEN = [
    {
        'symbol': 'MKR',
        'address': '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2',
        'init_price': 10.0,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2',       # MKR
            '0x69076e44a9c70a67d5b79d95795aba299083c275',       # gempit: place to destroy token
            '0x642ae78fafbb8032da552d619ad43f1d81e4dd7c',       # Redeemer
        ],
        'lending_contracts': [
            '0x9ef05f7f6deb616fd37ac3c959a2ddd25a54e4f5',       # Maker governance contract
        ],
        'team_accounts': [

        ],
},
    {
        'symbol': 'SNX',
        'address': '0xc011a72400e58ecd99ee497cf89e3775d4bd732f',
        'init_price': 0.5,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0xc011a72400e58ecd99ee497cf89e3775d4bd732f',       # SNX
            '0xb671f2210b1f6621a2607ea63e6b2dc3e2464d1f',       # SNX: Reward Escrow
            '0x49be88f0fcc3a8393a59d3688480d7d253c37d2a',       # SNX: Foundation
            '0x971e78e0c92392a4e39099835cf7e6ab535b2227',       # SNX: Token Sale Escrow
            '0xa6b5e74466edc95d0b6e65c5cbfca0a676d893a4',       # SNX: Arb Rewarder
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'ZRX',
        'address': '0xe41d2489571d322189246dafa5ebde1f4699f498',
        'init_price': 0.048,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0xe41d2489571d322189246dafa5ebde1f4699f498',       # ZRX
            '0x206376e8940e42538781cd94ef024df3c1e0fd43',       # ZRX: Ext Dev Pool
            '0xdb63d40c033d35e79cdbb21430f0fe10e9d97303',       # ZRX: Team Vesting
            '0x606af0bd4501855914b50e2672c5926b896737ef',       # ZRX: MultiSig 1
            '0xba7f8b5fb1b19c1211c5d49550fcd149177a5eaf',       # ZRX: ZRX Vault
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'KNC',
        'address': '0xdd974d5c2e2928dea5f71b9825b8b646686bd200',
        'init_price': 0.46,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0xdd974d5c2e2928dea5f71b9825b8b646686bd200',       # KNC
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'LEND',
        'address': '0x80fB784B7eD66730e8b1DBd9820aFD29931aab03',
        'init_price': 0.0173,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x80fB784B7eD66730e8b1DBd9820aFD29931aab03',       # LEND
            '0x24a42fD28C976A61Df5D00D0599C34c4f90748c8',       # LendingPoolAddressesProvider
            '0x398eC7346DcD622eDc5ae82352F02bE94C62d119',       # LendingPool
            '0x3dfd23A6c5E8BbcFc9581d2E864a68feb6a076d3',       # LendingPoolCore
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'REP',
        'address': '0x1985365e9f78359a9B6AD760e32412f4a445E862',
        'init_price': 0.602,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x1985365e9f78359a9B6AD760e32412f4a445E862',       # REP
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'IDEX',
        'address': '0xb705268213d593b8fd88d3fdeff93aff5cbdcfae',
        'init_price': 0.06,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0xb705268213d593b8fd88d3fdeff93aff5cbdcfae',       # IDEX
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'NXM',
        'address': '0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b',
        'init_price': 2.4479764,
        'source_exchange_rates': 'nexustracker',
        'token_contracts': [
            '0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b',       # NXM
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'LPT',
        'address': '0x58b6a8a3302369daec383334672404ee733ab239',
        'init_price': 3.0,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x58b6a8a3302369daec383334672404ee733ab239',       # LPT
        ],
        'lending_contracts': [
            '0x8573f2f5a3bd960eee3d998473e50c75cdbe6828',       # LPT staking contract
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'REN',
        'address': '0x408e41876cccdc0f92210600ef50372656052a38',
        'init_price': 0.06,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x408e41876cccdc0f92210600ef50372656052a38',       # REN
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'HT',
        'address': '0x6f259637dcd74c767781e37bc6133cd6a68aa161',
        'init_price': 1.52,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x6f259637dcd74c767781e37bc6133cd6a68aa161',       # HT
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'BAT',
        'address': '0x0d8775f648430679a709e98d2b0cb6250d2887ef',
        'init_price': 0.04,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x0d8775f648430679a709e98d2b0cb6250d2887ef',       # BAT
            '0x7c31560552170ce96c4a7b018e93cddc19dc61b6',       # BAT: UGP Reserve
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'NEXO',
        'address': '0xb62132e35a6c13ee1ee0f84dc5d40bad8d815206',
        'init_price': 0.10,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0xb62132e35a6c13ee1ee0f84dc5d40bad8d815206',       # NEXO
            '0x65b0bf8ee4947edd2a500d74e50a3d757dc79de0',       # NEXO: Wallet
            '0x00ee047a66d5cff27587a61559138c26b62f7ceb',       # Nexo 1
            '0xffec0067f5a79cff07527f63d83dd5462ccf8ba4',       # Nexo 2
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'LRC',
        'address': '0xbbbbca6a901c926f240b89eacb641d8aec7aeafd',
        'init_price': 0.05,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0xbbbbca6a901c926f240b89eacb641d8aec7aeafd',       # LRC
            '0x527f4fb6563d6afd30efedb9c57c7d7df2f5cdfc',       # NewLRCFoundationIceboxContract
        ],
        'lending_contracts': [
            '0xf4662bb1c4831fd411a95b8050b3a5998d8a4a5b',       # LRC staking eth
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'MANA',
        'address': '0x0f5d2fb29fb7d3cfee444a200298f468908cc942',
        'init_price': 0.024,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x0f5d2fb29fb7d3cfee444a200298f468908cc942',  # MANA
            # '0x7a3abf8897f31b56f09c6f69d074a393a905c1ac',  # Decentraland Vesting
            # '0xa3a90cacfd83ea4b114d5d7a24b54b42f670af94',  # Decentraland Vesting
            # '0x45dfe39d2f8bbf8bcdf4d3aa1e4e9d93ea605278',  # Decentraland Vesting
        ],
        'lending_contracts': [
        ],
        'team_accounts': [],
    },
    {
        'symbol': 'LINK',
        'address': '0x514910771af9ca656af840dff83e8264ecf986ca',
        'init_price': 0.11,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x514910771af9ca656af840dff83e8264ecf986ca',   # LINK
            '0xf5a3d443fccd7ee567000e43b23b0e98d96445ce',   # Oracle: Chainlayer
            '0x89f70fa9f439dbd0a1bc22a09befc56ada04d9b4',   # Oracle: Chainlink
            '0x049bd8c3adc3fe7d3fc2a44541d955a537c2a484',   # Oracle: Fiews
            '0x240bae5a27233fd3ac5440b5a598467725f7d1cd',   # Oracle: Linkpool
            '0xb92ec7d213a28e21b426d79ede3c9bbcf6917c09',   # Oracle: stake.fish
            '0x8c85a06eb3854df0d502b2b00169dbfb8b603bf3',   # Oracle address 2
            '0x0563fc575d5219c48e2dfc20368fa4179cdf320d',   # Oracle address 3
            '0x79febf6b9f76853edbcbc913e6aae8232cfb9de9',   # ChainLink: Aggregator
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
    {
        'symbol': 'ANT',
        'address': '0x960b236a07cf122663c4303350609a66a7b288c0',
        'init_price': 0.92,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x960b236a07cf122663c4303350609a66a7b288c0',   # ANT
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
]
