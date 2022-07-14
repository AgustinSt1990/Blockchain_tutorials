# Sending tx in eth

from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()
ganache_url = os.environ['NODE_PROVIDER_LOCAL']
web3 = Web3(Web3.HTTPProvider(ganache_url))


account_1 = os.environ['ACCOUNT_1']
account_2 = os.environ['ACCOUNT_2']

private_key = os.environ['PRIVATE_KEY_1']

# get nonce
nonce = web3.eth.getTransactionCount(account_1)

# build tx
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign tx
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# send tx
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# get tx hash
print (web3.toHex(tx_hash))