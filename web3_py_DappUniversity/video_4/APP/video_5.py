import json
from eth_utils import to_checksum_address
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = 'http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(ganache_url))

# account
w3.eth.defaultAccount = w3.eth.accounts[0]

# location
PATH_TRUFFLE_WK = './build/contracts'
truffleFile = json.load(open(PATH_TRUFFLE_WK + '/HelloWorld.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']

## Initialize contract
HelloWorld = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = HelloWorld.constructor().transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print (tx_receipt)

### second instance
contract = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi
)

# now you can use functions
tx_hash = contract.functions.setGreeting('HEEELLLOOOO!!!').transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print(contract.functions.greet().call())