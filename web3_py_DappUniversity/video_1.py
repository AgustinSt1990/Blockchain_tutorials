import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
infura_url =  os.environ['NODE_PROVIDER']
web3 = Web3(Web3.HTTPProvider(infura_url))

print (web3.isConnected())

print (web3.eth.blockNumber)

balance = web3.eth.get_balance("0x6701681E0B28386ea100b23405f07C9AA1209B33")
print (web3.fromWei(balance, 'ether'))