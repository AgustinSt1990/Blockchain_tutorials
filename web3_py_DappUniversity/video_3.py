# Sending tx in eth

from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0x6C4025A9970C32622Cb4Bc76b94d89Ffa072fb64'
account_2 = '0x5B0C7808D97897c5E27FEaDCFac478Dcb2FE57cC'

private_key = '2100213c322a5184dfca981a24722556dabfa34e60fc9f4b2828ebc640425e8d'

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