import os
from dotenv import load_dotenv
from web3 import Web3
from moralis import Moralis

load_dotenv()
node_provider = os.environ['NODE_PROVIDER']
w3 = Web3(Web3.HTTPProvider(node_provider))


def are_we_connected():
    print(w3.isConnected())

def latest_block():
    print (w3.eth.block_number)

def balance_of(ETH_address):
    balance = w3.eth.get_balance(ETH_address)
    balance_ETH = w3.fromWei(balance, 'ether')
    print (balance_ETH)

if __name__ == '__main__':
    Moralis('infura_url').are_we_connected()
    Moralis('infura_url').latest_block()

    #address got from etherscan
    Moralis('infura_url').balance_of('0x646dB8ffC21e7ddc2B6327448dd9Fa560Df41087')