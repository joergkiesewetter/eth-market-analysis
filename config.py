import logging

LOG_LEVEL = logging.DEBUG

TOKEN = [
#     {
#         'symbol': 'ANT',
#         'address': '0x960b236a07cf122663c4303350609a66a7b288c0',
#         'init_price': 0.92,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x960b236a07cf122663c4303350609a66a7b288c0',   # ANT
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'BAT',
#         'address': '0x0d8775f648430679a709e98d2b0cb6250d2887ef',
#         'init_price': 0.04,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x0d8775f648430679a709e98d2b0cb6250d2887ef',       # BAT
#             '0x7c31560552170ce96c4a7b018e93cddc19dc61b6',       # BAT: UGP Reserve
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'FXC',
#         'address': '0x4a57e687b9126435a9b19e4a802113e266adebde',
#         'init_price': 0.00025,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x4a57e687b9126435a9b19e4a802113e266adebde',   # FXC
#             '0xd7abF0AdA97780b43d88cC37Bd9cEFdE73773510',   # probably a treasury
#         ],
#         'lending_contracts': [
#             '0x12f208476f64de6e6f933e55069ba9596d818e08',   # Flexa Capacity Staking
#         ],
#         'team_accounts': [
#             '0x30a68f8efc0c82db84d0bb0597a3cddcc329433d',   # Flexacoin: Treasury 1
#             '0x5b8515ee513cecf713ff6986da5c1f824c393032',   # Flexacoin: Treasury 2
#         ],
#     },
#     {
#         'symbol': 'HOT',
#         'address': '0x9af839687f6c94542ac5ece2e317daae355493a1',
#         'init_price': 0.08, # https://cryptorank.io/currencies/hydro-protocol/ico
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x9af839687f6c94542ac5ece2e317daae355493a1',   # FXC
#             '0x74622073a4821dbfd046e9aa2ccf691341a076e1',   # allowance proxy
#             '0xe2a0bfe759e2a4444442da5064ec549616fff101',   # HybridExchange1.1
#             '0xb15367df8a39ea06f8f81ed35d49e056ee05f3b7',   # MultiSigWalletWithLock
#             '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',   # wrapped Ether
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [ # data from coingecko
#             '0x1902f0a23142cf07b726c9c117b2500e42c39e79',   # Foundation Wallet
#             '0x3295f80c45de76fe955a9220e758bd81de7aa261',   # Founder Wallet
#             '0xf47faffc5215ace2dd3bde670de0ae25adacf076',   # Foundation and Eco-Fund
#             '0x058073b504ff054fcde9c6d27cb342b9e19055f8',   # Bounty and legal/ Early investor and advisor
#             '0xf12f30d3f20c108141252f99ed93090066320ef6',   # Bounty and legal/ Early investor and advisor
#             '0x5b2b77773d04da8c7fc17a559bc0b404ef3b210e',   # Bounty and legal/ Early investor and advisor
#             '0x6cc5f688a315f3dc28a7781717a9a798a59fda7b',   # Foundation and Eco-fund
#         ],
#     },
#     {
#         'symbol': 'HT',
#         'address': '0x6f259637dcd74c767781e37bc6133cd6a68aa161',
#         'init_price': 1.52,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x6f259637dcd74c767781e37bc6133cd6a68aa161',       # HT
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'IDEX',
#         'address': '0xb705268213d593b8fd88d3fdeff93aff5cbdcfae',
#         'init_price': 0.06,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0xb705268213d593b8fd88d3fdeff93aff5cbdcfae',       # IDEX
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'KNC',
#         'address': '0xdd974d5c2e2928dea5f71b9825b8b646686bd200',
#         'init_price': 0.46,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0xdd974d5c2e2928dea5f71b9825b8b646686bd200',       # KNC
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'LEND',
#         'address': '0x80fB784B7eD66730e8b1DBd9820aFD29931aab03',
#         'init_price': 0.0173,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x80fB784B7eD66730e8b1DBd9820aFD29931aab03',       # LEND
#             '0x24a42fD28C976A61Df5D00D0599C34c4f90748c8',       # LendingPoolAddressesProvider
#             '0x398eC7346DcD622eDc5ae82352F02bE94C62d119',       # LendingPool
#             '0x3dfd23A6c5E8BbcFc9581d2E864a68feb6a076d3',       # LendingPoolCore
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'LINK',
#         'address': '0x514910771af9ca656af840dff83e8264ecf986ca',
#         'init_price': 0.11,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x514910771af9ca656af840dff83e8264ecf986ca',   # LINK
#             '0xf5a3d443fccd7ee567000e43b23b0e98d96445ce',   # Oracle: Chainlayer
#             '0x89f70fa9f439dbd0a1bc22a09befc56ada04d9b4',   # Oracle: Chainlink
#             '0x049bd8c3adc3fe7d3fc2a44541d955a537c2a484',   # Oracle: Fiews
#             '0x240bae5a27233fd3ac5440b5a598467725f7d1cd',   # Oracle: Linkpool
#             '0xb92ec7d213a28e21b426d79ede3c9bbcf6917c09',   # Oracle: stake.fish
#             '0x8c85a06eb3854df0d502b2b00169dbfb8b603bf3',   # Oracle address 2
#             '0x0563fc575d5219c48e2dfc20368fa4179cdf320d',   # Oracle address 3
#             '0x79febf6b9f76853edbcbc913e6aae8232cfb9de9',   # ChainLink: Aggregator
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
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
#     {
#         'symbol': 'LRC',
#         'address': '0xbbbbca6a901c926f240b89eacb641d8aec7aeafd',
#         'init_price': 0.05,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0xbbbbca6a901c926f240b89eacb641d8aec7aeafd',       # LRC
#             '0x527f4fb6563d6afd30efedb9c57c7d7df2f5cdfc',       # NewLRCFoundationIceboxContract
#         ],
#         'lending_contracts': [
#             '0xf4662bb1c4831fd411a95b8050b3a5998d8a4a5b',       # LRC staking eth
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'MANA',
#         'address': '0x0f5d2fb29fb7d3cfee444a200298f468908cc942',
#         'init_price': 0.024,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x0f5d2fb29fb7d3cfee444a200298f468908cc942',  # MANA
#             # '0x7a3abf8897f31b56f09c6f69d074a393a905c1ac',  # Decentraland Vesting
#             # '0xa3a90cacfd83ea4b114d5d7a24b54b42f670af94',  # Decentraland Vesting
#             # '0x45dfe39d2f8bbf8bcdf4d3aa1e4e9d93ea605278',  # Decentraland Vesting
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [],
#     },
#     {
#         'symbol': 'MKR',
#         'address': '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2',
#         'init_price': 10.0,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2',       # MKR
#             '0x69076e44a9c70a67d5b79d95795aba299083c275',       # gempit: place to destroy token
#             '0x642ae78fafbb8032da552d619ad43f1d81e4dd7c',       # Redeemer
#         ],
#         'lending_contracts': [
#             '0x9ef05f7f6deb616fd37ac3c959a2ddd25a54e4f5',       # Maker governance contract
#         ],
#         'team_accounts': [
#
#         ],
# },
#     {
#         'symbol': 'NEST',
#         'address': '0x04abeda201850ac0124161f037efd70c74ddc74c',
#         'init_price': 0.65,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x04abeda201850ac0124161f037efd70c74ddc74c',   # NEST
#             '0x923f80828663e44e0ffd5eb499686dc1ccc78476',   # NEST mining save
#             '0x561d0d6c498a379574eaaa4a5f2532b223ffaebf',   # NEST save
#             '0x101d8b63a081dfff2b1364864345b7f071b052ac',   # NEST node save
#             '0x4f391c202a906eed9e2b63fdd387f28e952782e2',   # NEST 3 offer factory
#             '0xf67b829397dc05751a98f243dbde5db63f86e7f6',   # NEST A Bonus
#             '0x9c3c7bcf8993a58410016e29882c78b552d5c9b4',   # NEST ore pool logic
#             '0x72b07fc5753a3564cfcac50cd6f246187d2d4306',   # NEST 3 offer data
#             '0xb68f0942c7f821b4367c76597b4cf235639bb282',   # NEST 3 offer factory
#             '0x89be829d32a66b116ec8568687481101fb121751',   # NEST 3 ore pool logic
#             '0x54f701415ce1b17bd02fe4fbb6974b8f6469cd45',   # NEST 3 offer data
#             '0x5c07eb74ec8568830d57588d36ad03cef8103c11',   # ???
#             '0x350b460765dbbac2176a010f4f2c4daa628d2ba8',   # ???
#             '0xe6b9466bd33e8184d91c76d87690a156c74aaa33',   # ???
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#             '0x6756927922d2a32cb799f261e4abc47652cde54b'
#         ],
#     },
#     {
#         'symbol': 'NEXO',
#         'address': '0xb62132e35a6c13ee1ee0f84dc5d40bad8d815206',
#         'init_price': 0.10,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0xb62132e35a6c13ee1ee0f84dc5d40bad8d815206',       # NEXO
#             '0x65b0bf8ee4947edd2a500d74e50a3d757dc79de0',       # NEXO: Wallet
#             '0x00ee047a66d5cff27587a61559138c26b62f7ceb',       # Nexo 1
#             '0xffec0067f5a79cff07527f63d83dd5462ccf8ba4',       # Nexo 2
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
    {
        'symbol': 'NFTX',
        'address': '0x87d73E916D7057945c9BcD8cdd94e42A6F47f776',
        'init_price': 19.99,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x87d73E916D7057945c9BcD8cdd94e42A6F47f776',       # NFTX Token
            '0x8F217D5cCCd08fD9dCe24D6d42AbA2BB4fF4785B',       # NFTX: Deployer
            '0x5fAD0e4cc9925365b9B0bbEc9e0C3536c0B1a5C7',       # Staking Token Provider
            '0x688c3E4658B5367da06fd629E41879beaB538E37',       # Staking
            '0xe8B6820b74533c27786E4724a578Bfca28D97BD1',       # Vault template
            '0x7AE9D7Ee8489cAD7aFc84111b8b185EE594Ae090',       # Fee Distributor
            '0xBE86f647b167567525cCAAfcd6f881F1Ee558216',       # Vault Factory
            '0x4086e98Cce041d286112d021612fD894cFed94D5',       # Eligibility Manager
            '0x4333d66Ec59762D1626Ec102d7700E64610437Df',       # Proxy Controller
            '0x0b8ee2ee7d6f3bfb73c9ae2127558d1172b65fb1',       # NFTX Staking Zap
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
            '0x40D73Df4F99bae688CE3C23a01022224FE16C7b2',       # NFTX: Dao Treasury
        ],
    },
#     {
#         'symbol': 'NXM',
#         'address': '0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b',
#         'init_price': 2.4479764,
#         'source_exchange_rates': 'nexustracker',
#         'token_contracts': [
#             '0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b',       # NXM
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'REN',
#         'address': '0x408e41876cccdc0f92210600ef50372656052a38',
#         'init_price': 0.06,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x408e41876cccdc0f92210600ef50372656052a38',       # REN
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'REP',
#         'address': '0x1985365e9f78359a9B6AD760e32412f4a445E862',
#         'init_price': 0.602,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0x1985365e9f78359a9B6AD760e32412f4a445E862',       # REP
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'RPL',
#         'address': '0xb4efd85c19999d84251304bda99e90b92300bd93',
#         'init_price': 0.95795,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0xb4efd85c19999d84251304bda99e90b92300bd93',   # RPL
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
#     {
#         'symbol': 'SNX',
#         'address': '0xc011a72400e58ecd99ee497cf89e3775d4bd732f',
#         'init_price': 0.5,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0xc011a72400e58ecd99ee497cf89e3775d4bd732f',       # SNX
#             '0xb671f2210b1f6621a2607ea63e6b2dc3e2464d1f',       # SNX: Reward Escrow
#             '0x49be88f0fcc3a8393a59d3688480d7d253c37d2a',       # SNX: Foundation
#             '0x971e78e0c92392a4e39099835cf7e6ab535b2227',       # SNX: Token Sale Escrow
#             '0xa6b5e74466edc95d0b6e65c5cbfca0a676d893a4',       # SNX: Arb Rewarder
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
    {
        'symbol': 'ROBOT',
        'address': '0xfb5453340C03db5aDe474b27E68B6a9c6b2823Eb',
        'init_price': 6.31,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0xfb5453340C03db5aDe474b27E68B6a9c6b2823Eb',       # ROBOT Token
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
            '0x40D73Df4F99bae688CE3C23a01022224FE16C7b2',       # NFTX: Dao Treasury
        ],
    },
    {
        'symbol': 'WNXM',
        'address': '0x0d438F3b5175Bebc262bF23753C1E53d03432bDE',
        'init_price': 10.0,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x0d438F3b5175Bebc262bF23753C1E53d03432bDE',       # WNXM
            '0x586b9b2F8010b284A0197f392156f1A7Eb5e86e9',       # Nexus Mutual: Community Fund
            # https://api.nexusmutual.io/version-data/
            '0xcafea81b73daB8F42C5eca7d2E821A82660B6775',       # claimProofs
            '0x813174d3eC6f7C11f4364a637cEf0f1CD6176139',       # claims
            '0xdc2D359F59F6a26162972c3Bd0cFBfd8C9Ef43af',       # claimsData
            '0x15671E5710e6E8f087939F8dbB6707Bc4B5c64A9',       # claimsReward
            '0x27e6d3Ce99Fa5ec4019Ce598aF54bcB3A2FB2E5f',       # communityStakingIncentives
            '0x6752c6FbDDc24ac88f3749D8921E00c77Bffef8c',       # distributorFactory
            '0x089Ab1536D032F54DFbC194Ba47529a4351af1B5',       # gateway
            '0x4A5C681dDC32acC6ccA51ac17e9d461e6be87900',       # governance
            '0x8CEBa69a8e96a4ce71Aa65859DBdb180B489a719',       # incidents
            '0x406511caf30043f92625414E0B951a5d9c5aBF66',       # MCR
            '0x055CC48f7968FD8640EF140610dd4038e1b03926',       # MemberRoles
            '0xd7c49CEE7E9188cCa6AD8FF264C1DA2e69D4Cf3B',       # NXMToken
            '0x01BFd82675DBCc7762C84019cA518e701C0cD07e',       # NXMaster
            '0xcafea35cE5a2fc4CED4464DA4349f81A122fd12b',       # Pool
            '0xcafeaDA4d15BBC7592113D5d5af631b5dcd53Dcb',       # Pool 2
            '0x84EdfFA16bb0b9Ab1163abb0a13Ff0744c11272f',       # PooledStaking
            '0x888eA6Ab349c854936b98586CE6a17E98BF254b2',       # ProposalCategory
            '0xB365FA523d853fbfA5608E3e4c8457166287D958',       # Quotation
            '0x1776651F58a17a50098d31ba3C3cD259C1903f7A',       # QuotationData
            '0xcafea4E03B98873B842D83ed368F6F1A49F58Ee7',       # SwapOperator
            '0x5407381b6c251cFd498ccD4A1d877739CB7960B8',       # TokenController
            '0xE20B3aE826Cdb43676e418F7C3B84B75b5697a40',       # TokenData
            '0xcafea2D407F1307d1413e84b2730F0870fd72dC0',       # TokenFunctions
            '0xcafea1C9f94e077DF44D95c4A1ad5a5747a18b5C',       # TwapOracle
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
        ],
    },
#     {
#         'symbol': 'ZRX',
#         'address': '0xe41d2489571d322189246dafa5ebde1f4699f498',
#         'init_price': 0.048,
#         'source_exchange_rates': 'coin_gecko',
#         'token_contracts': [
#             '0xe41d2489571d322189246dafa5ebde1f4699f498',       # ZRX
#             '0x206376e8940e42538781cd94ef024df3c1e0fd43',       # ZRX: Ext Dev Pool
#             '0xdb63d40c033d35e79cdbb21430f0fe10e9d97303',       # ZRX: Team Vesting
#             '0x606af0bd4501855914b50e2672c5926b896737ef',       # ZRX: MultiSig 1
#             '0xba7f8b5fb1b19c1211c5d49550fcd149177a5eaf',       # ZRX: ZRX Vault
#         ],
#         'lending_contracts': [
#         ],
#         'team_accounts': [
#         ],
#     },
]



