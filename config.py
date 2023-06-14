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
    {
        'symbol': 'INDEX',
        'address': '0x0954906da0Bf32d5479e25f46056d22f08464cab',
        'init_price': 3.55,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x0954906da0Bf32d5479e25f46056d22f08464cab',       # INDEX
            '0x26e316f5b3819264DF013Ccf47989Fb8C891b088',       # Index Coop: Community Treasury Year 1 Vesting
            '0xd89C642e52bD9c72bCC0778bCf4dE307cc48e75A',       # Index Coop: Community Treasury Year 2 Vesting
            '0x71F2b246F270c6AF49e2e514cA9F362B491Fbbe1',       # Index Coop: Community Treasury Year 3 Vesting
            '0xB93b505Ed567982E2b6756177ddD23ab5745f309,'       # Index Coop: DPI staking rewards v2 
            '0x8f06FBA4684B5E0988F215a47775Bb611Af0F986',       # Index Coop: Initial Liquidity Mining Rewards
            '0x7B15bB785167c610020B52bf4B790396D73bf8a0',       # unknown vesting contract
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
            '0x9467cfADC9DE245010dF95Ec6a585A506A8ad5FC',       # Index Coop: MultiSig
            '0xf64d061106054Fe63B0Aca68916266182E77e9bc',       # Index Coop: Set Labs Year 1 Vesting
            '0x4C11DFD35A4FE079B41D5d9729eD34C00D487712',       # Index Coop: Set Labs Year 2 Vesting
            '0x0D627ca04A97219F182DaB0Dc2a23FB4a5B02A9D',       # Index Coop: Set Labs Year 3 Vesting
            '0x5C29Aa6761803BcFDA7f683eaa0ff9bdDDA3649D',       # Index Coop: DeFi Pulse Year 1 Vesting
            '0xCe3c6312385fCF233aB0De574b0cB1A588566C3f',       # Index Coop: DeFi Pulse Year 2 Vesting
            '0x0f58793e8CF39D6b60919FFaf773A7f95A568146',       # Index Coop: DeFi Pulse Year 3 Vesting
            '0xDD111F0fc07F4D89ED6ff96DBAB19a61450b8435',       # Index Coop: Early Community Rewards
            '0x66a7d781828B03Ee1Ae678Cd3Fe2D595ba3B6000',       # Index Coop: Index Methodologist Vesting

        ],
    },
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
    {
        'symbol': 'MKR',
        'address': '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2',
        'init_price': 10.0,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x6b175474e89094c44da98b954eedeac495271d0f',       # Dai Stablecoin
            '0x39755357759ce0d7f32dc8dc45414cca409ae24e',       # Eth2Dai: Old Contract
            '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2',       # Maker Token
            '0x5ef30b9986345249bc32d8928b7ee64de9435e39',       # Maker: CDP Manager
            '0x448a5065aebb8e423f0896e6c5d525c040f59af3',       # Maker: Contract
            '0xbda109309f9fafa6dd6a9cb9f1df4085b27ee8ef',       # Maker: Contract 2
            '0x9b0f70df76165442ca6092939132bbaea77f2d7a',       # Maker: Contract 3
            '0x9b0ccf7c8994e19f39b2b4cf708e0a7df65fa8a3',       # Maker: Contract 4
            '0xf2c5369cffb8ea6284452b0326e326dbfdcb867c',       # Maker: Contract 5
            '0x315cbb88168396d12e1a255f9cb935408fe80710',       # Maker: Contract 6
            '0x79f6d0f646706e1261acf0b93dcb864f357d4680',       # Maker: Contract 7
            '0x8e2a84d6ade1e7fffee039a35ef5f19f13057152',       # Maker: Contract 8
            '0x69076e44a9c70a67d5b79d95795aba299083c275',       # Maker: Contract 9
            '0x4f26ffbe5f04ed43630fdc30a87638d53d0b0876',       # Maker: Deployer 1
            '0xdb33dfd3d61308c33c63209845dad3e6bfb2c674',       # Maker: Deployer 2
            '0x00daa9a2d88bed5a29a6ca93e0b7d860cd1d403f',       # Maker: Deployer 3
            '0xddb108893104de4e1c6d0e47c42237db4e617acc',       # Maker: Deployer 4
            '0xda0fab05039809e63c5d068c897c3e602fa97457',       # Maker: Deployer 5
            '0xa26e15c895efc0616177b7c1e7270a4c7d51c997',       # Maker: DS Proxy Factory
            '0x373238337bfe1146fb49989fc222523f83081ddb',       # Maker: DSR Manager
            '0x36a724bd100c39f0ea4d3a20f7097ee01a8ff573',       # Maker: Get CDPS
            '0x78f2c2af65126834c51822f56be0d7469d7a523e',       # Maker: MCD Cat
            '0xbaa65281c2fa2baacb2cb550ba051525a480d3f4',       # Maker: MCD Deploy
            '0xab14d3ce3f733cacb76ec2abe7d2fcb00c99f3d5',       # Maker: MCD End
            '0x0581a0abe32aae9b5f0f68defab77c6759100085',       # Maker: MCD ESM
            '0xdfe0fb1be2a52cdbf8fb962d5701d7fd0902db9f',       # Maker: MCD Flap
            '0xaa745404d55f88c108a28c86abe7b5a1e7817c07',       # Maker: MCD Flip BAT A
            '0xd8a04f5412223f513dc55f839574430f5ec15531',       # Maker: MCD Flip ETH A
            '0x5432b2f3c0dff95aa191c45e5cbd539e2820ae72',       # Maker: MCD Flip SAI
            '0xbe00fe8dfd9c079f1e5f5ad7ae9a3ad2c571fcac',       # Maker: MCD Flop
            '0x4f5f0933158569c026d617337614d00ee6589b6e',       # Maker: MCD Gov Actions
            '0x3d0b1912b66114d4096f48a8cee3a56c231772ca',       # Maker: MCD Join BAT A
            '0x9759a6ac90977b93b58547b4a71c78317f391a28',       # Maker: MCD Join DAI
            '0x2f0b23f53734252bda2277357e97e1517d6b042a',       # Maker: MCD Join ETH A
            '0xad37fd42185ba63009177058208dd1be4b136e6b',       # Maker: MCD Join SAI
            '0x19c0976f590d67707e62397c87829d896dc0f1f1',       # Maker: MCD Jug
            '0xbe286431454714f511008713973d3b053a2d38f3',       # Maker: MCD Pause
            '0xbe8e3e3618f7474f8cb1d074a26affef007e98fb',       # Maker: MCD Pause Proxy
            '0x197e90f9fad81970ba7976f33cbd77088e5d7cf7',       # Maker: MCD Pot
            '0x65c79fcb50ca1594b025960e539ed7a9a6d434a3',       # Maker: MCD Spot
            '0x35d1b3f3d7966a1dfe207aa4514c12a259a0492b',       # Maker: MCD Vat
            '0xa950524441892a31ebddf91d3ceefa04bf454466',       # Maker: MCD Vow
            '0x99041f808d598b782d5a3e498681c2452a31da08',       # Maker: Medianizer 1
            '0x729d19f657bd0614b4985cf1d82531c67569197b',       # Maker: Medianizer 2
            '0xc73e0383f3aff3215e6f04b0331d58cecf0ab849',       # Maker: Migration
            '0xe4b22d484958e582098a98229a24e8a43801b674',       # Maker: Migration Proxy Actions
            '0x5e227ad1969ea493b43f840cff78d08a6fc17796',       # Maker: Multicall
            '0x793ebbe21607e4f04788f89c7a9b97320773ec59',       # Maker: Oasis Proxy
            '0xc66ea802717bfb9833400264dd12c2bceaa34a6d',       # Maker: Old Token
            '0xb4eb54af9cc7882df0121d26c5b97e802915abe6',       # Maker: PIP BAT
            '0x81fe72b5a8d1a857d176c3e7d5bd2679a9b85763',       # Maker: PIP ETH
            '0x54003dbf6ae6cba6ddae571ccdc34d834b44ab1e',       # Maker: PIP SAI
            '0x82ecd135dce65fbc6dbdd0e4237e0af93ffd5038',       # Maker: Proxy Actions
            '0x07ee93aeea0a36fff2a9b95dd22bd6049ee54f26',       # Maker: Proxy Actions DSR
            '0x069b2fb501b6f16d1f5fe245b16f6993808f1008',       # Maker: Proxy Actions End
            '0x1b93556ab8dccef01cd7823c617a6d340f53fb58',       # Maker: Proxy Deployer
            '0x6bda13d43b7edd6cafe1f70fb98b5d40f61a1370',       # Maker: Proxy Pause Actions
            '0x4678f0a6958e4d2bc4f1baf7bc52e8f3564f3fe4',       # Maker: Proxy Registry
            '0x0a59649758aa4d66e25f08dd01271e891fe52199',       # Maker: PSM-USDC-A
            '0x190c2cfc69e68a8e8d5e2b9e2b9cc3332caff77b',       # Maker: Sai Proxy 1
            '0x526af336d614ade5cc252a407062b8861af998f5',       # Maker: Sai Proxy 2
            '0xbf72da2bd84c5170618fbe5914b0eca9638d5eb5',       # Maker: WBTC
            '0x794e6e91555438afc3ccf1c5076a74f42133d08d',       # OasisDEX
            '0x14fbca95be7e99c15cc2996c6c9d841e54b79425',       # OasisDex: Old Contract 1
            '0xb7ac09c2c0217b07d7c103029b4918a2c401eecb',       # OasisDex: Old Contract 2
            '0xf53ad2c6851052a81b42133467480961b2321c09',       # Pooled Ether
            '0x59adcf176ed2f6788a41b8ea4c4904518e62b6a4',       # ProtoSAI Token
            '0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359',       # Sai Stablecoin
            '0x642ae78fafbb8032da552d619ad43f1d81e4dd7c',       # Redeemer
        ],
        'lending_contracts': [
            '0x0a3f6849f78076aefadf113f5bed87720274ddc0',       # Maker: Governance Contract
            '0x9ef05f7f6deb616fd37ac3c959a2ddd25a54e4f5',       # Maker governance contract
        ],
        'team_accounts': [
            '0x8ee7d9235e01e6b42345120b5d270bdb763624c7',       # Maker: MultiSig
        ],
    },
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
            '0xe8B6820b74533c27786E4724a578Bfca28D97BD1',       # Vault template
            '0x7AE9D7Ee8489cAD7aFc84111b8b185EE594Ae090',       # Fee Distributor
            '0xBE86f647b167567525cCAAfcd6f881F1Ee558216',       # Vault Factory
            '0x4086e98Cce041d286112d021612fD894cFed94D5',       # Eligibility Manager
            '0x4333d66Ec59762D1626Ec102d7700E64610437Df',       # Proxy Controller
            '0x0b8ee2ee7d6f3bfb73c9ae2127558d1172b65fb1',       # NFTX Staking Zap
        ],
        'lending_contracts': [
            '0x688c3E4658B5367da06fd629E41879beaB538E37',       # Staking
        ],
        'team_accounts': [
            '0x40d73df4f99bae688ce3c23a01022224fe16c7b2',       # NFTX: Dao Treasury
        ],
    },
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
        'symbol': 'SSV',
        'address': '0x9D65fF81a3c488d585bBfb0Bfe3c7707c7917f54',
        'init_price': 20.44,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0x9D65fF81a3c488d585bBfb0Bfe3c7707c7917f54',       # SSV Token
        ],
        'lending_contracts': [
        ],
        'team_accounts': [
            '0x2bf73A478cc6a7bA4E6758A3A52AbDc8CDBa735E',       # DEX: CDT-SSV swap
            '0xb35096b074fdb9bBac63E3AdaE0Bbde512B2E6b6',       # ssv-network: DAO treasury
            '0xE16e6Bddf4a1683c029DdC7AEcb567A6095e95A6',       # Airdrop: Merkle Distributor
            '0x1806c87798b59C56fc481C2998D9D506675808e3',       # User: Bitfly
            '0x186fa67b00F0C8d777aAfB5caCD5002AAC1B8c83',       # User: Lsankar
            '0x489a727c5722d0D0CF654d169F87De1Bb5743A87',       # User: Fod
            '0xf71E9C766Cdf169eDFbE2749490943C1DC6b8A55',       # User: Preston
            '0xeCbb058Fc429941124a2b8d0984354c3132F536f',       # User: Yorick
            '0x10F5d45854e038071485AC9e402308cF80D2d2fE',       # User: Beiko
            '0x872Da650d6d727b87e56D8e46f62228a27f94B3d',       # User: Sp00ky
            '0x78D71193A507287365b968dBf7D3Bc6C49d7Eb0b',       # User: Taiga
            '0x2de670a1D8c1DE83D8727295284704bB196bA117',       # User: BenAffleck
            '0x6210477B3025BF5ea50A35D39e7D2875dC11661c',       # User: GBeast
            '0xA8baE5d3EEabd6AB13EE401b67EaEdCe06C70248',       # User: Izzy
            '0x5ba64C3A6Dfd64025F1647DaD8b23Cf48132624F',       # User: Elias
            '0x32ebAf9ea4063d911222407838E15E3a5027A638',       # User: Marko
            '0x4a24A839576695e3F10eCCAA090cedc0E7e39E73',       # User: dMarketing
        ],
    },
    {
        'symbol': 'TRIBE',
        'address': '0xc7283b66Eb1EB5FB86327f08e1B5816b0720212B',
        'init_price': 2.21,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts': [
            '0xc7283b66Eb1EB5FB86327f08e1B5816b0720212B',       # TRIBE Token
            '0xC416EEe663ECa29cEB726241caDFFe6a77D61E2D',       # PegExchangeDripper
            '0x0BEF27FEB58e857046d630B2c03dFb7bae567494',       # FEI DAO
            '0xE087F94c3081e1832dC7a22B48c6f2b5fAaE579B',       # Old FEI DAO
            '0x956F47F50A910163D8BF957Cf5846D573E7f87CA',       # FEI Token
            '0xB1410aeCe2c65fE9e107c58b5aa32e91B18f0BC7',       # Ratio PVC Controller
            '0xB783c0E21763bEf9F2d04E6499abFbe23AdB7e1F',       # ETH Bonding Curve
            '0xC0afe0E649e32528666F993ce63822c3840e941a',       # DAI Bonding Curve
            '0x25d60212D47Dd8F6Ff0469367E4c6C98Cd3411A5',       # RAI Bonding Curve
            '0xBf5721c5E1C370f6F1A3E21b3972E0AcE93A1E84',       # DPI Bonding Curve
            '0x902199755219A9f8209862d09F1891cfb34F59a3',       # DPI Sushiswap PCV Deposit
            '0x0ee81df08B20e4f9E0F534e50da437D24491c4ee',       # INDEX Snapshot Delegator PCV Deposit
            '0x15958381E9E6dc98bD49655e36f524D2203a28bD',       # EthUniswapPCVDeposit
            '0x17305f0e18318994a57b494078CAC866A857F7b6',       # EthReserveStabilizer
            '0x9e1076cC0d19F9B0b8019F384B0a29E48Ee46f7f',       # Tribal Chief
            '0x3Fe0EAD3500e767F0F8bC2d3B5AF7755B1b21A6a',       # Tribe ERC20Dripper
            '0xDee5c1662bBfF8f80f7c572D8091BF251b3B0dAB',       # Tribe AaveIncentivesController
            '0xd81Be1B9A7895C996704A8DDa794BbA4454EeB90',       # fTRIBE StakedTokenWrapper
            '0x73F16f0c0Cd1A078A54894974C5C054D8dC1A3d7',       # FeiRari RewardsDistributorDelegator
            '0x4e979E8b136Cd7BdEBB83ea50a599C3BED1e15c0',       # FeiRari RewardsDistributorAdmin
            '0x61Be49Dfbd869a601FEa076E1A1379903e61a895',       # FeiRari Tribe AutoRewardsDistributor

        ],
        'lending_contracts': [
        ],
        'team_accounts': [
            '0x8d5ED43dCa8C2F7dFB20CF7b53CC7E593635d7b9',       # DAO TRIBE Treasury
            '0xd51dbA7a94e1adEa403553A8235C302cEbF41a3c',       # FEO DAO Timelock
            '0x639572471f2f318464dc01066a56867130e45E25',       # Old FEI DAO Timelock
            '0x35ED000468f397AA943009bD60cc6d2d9a7d32fF',       # TribalChief Optimistic Multisig
            '0xbC9C084a12678ef5B516561df902fdc426d95483',       # TribalChief Optimistic Timelock
            '0xB8f482539F2d3Ae2C9ea6076894df36D1f632775',       # Guardian Multisig
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
    {
        'symbol':                'XMON',
        'address':               '0x3aaDA3e213aBf8529606924d8D1c55CbDc70Bf74',
        'init_price':            2000.0,
        'source_exchange_rates': 'coin_gecko',
        'token_contracts':       [
            '0x3aaDA3e213aBf8529606924d8D1c55CbDc70Bf74', # XMON
            '0xD06337A401B468657dE2f9d3E390cE5b21C3c1C0', # MonStaker2
            '0xA3300bfc13556Fa5146fFdE34e92a0230A1C3197', # MonStaker3
        ],
        'lending_contracts':     [
        ],
        'team_accounts':         [
            '0x4e2f98c96e2d595a83afa35888c4af58ac343e44',   # XMON Multisig
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



