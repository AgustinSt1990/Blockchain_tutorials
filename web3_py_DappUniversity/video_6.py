import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
infura_url =  os.environ['NODE_PROVIDER']
w3 = Web3(Web3.HTTPProvider(infura_url))
print (w3.isConnected())

print (w3.eth.blockNumber)

latest = w3.eth.blockNumber
print (w3.eth.getBlock(latest))

# min 6

#for i in range(10):
#    print (w3.eth.getBlock(latest - i))

# min 8: Block Hash

hash = ''

print (w3.eth.getTransactionByBlock(hash, 2))
