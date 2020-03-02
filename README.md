# description

These scripts are meant to analyse different ERC20-Token. The scripts fetch the whole transaction history from etherscan and the give price from coingecko for the given token.

Afterwards it starts to calculate the realized market capitalization and some other usefull statistical values.

All analytical data are printed out to the console, so that you can use them however you want.

Calculated values are:
* total supply
* not moved token
* realized market capitalization
* amount coins not moved for more than 1 year

# pre-requirements
You need an etherscan api-token. You can get one by creating an account at etherscan and create a new one.

# usage

py ./main.py --etherscan-api-token=<YOUR API TOKEN>
