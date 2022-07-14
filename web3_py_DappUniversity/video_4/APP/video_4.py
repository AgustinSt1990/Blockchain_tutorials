import json
from eth_utils import to_checksum_address
import pandas as pd
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = 'http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(ganache_url))

## TODO: Deploy the HelloWorld contract to Ganache with remix.ethereum.org

# Set a default account to sign transaction - this account is unlocked with Ganache
w3.eth.defaultAccount = w3.eth.accounts[0]

# HelloWorld contract address - convert to checksum address
address= to_checksum_address('0x124E5684f8A6E3Ba649765B0f9EE6E518FA89A5a')

# HelloWorld contract abi
#abi = json.loads(pd.read_json('HelloWorld_abi.json'))
PATH_TRUFFLE_WK = './build/contracts'
truffleFile = json.load(open(PATH_TRUFFLE_WK + '/HelloWorld.json'))
abi = truffleFile['abi']

# Initialize contract
contract = w3.eth.contract(address=address, abi=abi)

# Print the default greeting
print('HelloWorld smart contract dice: {}'.format(contract.functions.greet().call()))

# Set a new greeting
tx_hash = contract.functions.setGreeting('Hello World!').transact()

# Wait for transaction to be mined
w3.eth.waitForTransactionReceipt(tx_hash)

# Display the new greeting value
print ('updated contract greeting: {}'.format(contract.functions.greet().call()))