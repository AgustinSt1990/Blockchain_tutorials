import os
from dotenv import load_dotenv
from web3 import Web3
from moralis import Moralis


if __name__ == '__main__':
    
    load_dotenv()
    
    ####################################################
    # # # #            MAIN PROGRAM            # # # # # 
    ####################################################
    
    connection = Moralis('local')
    connection.are_we_connected()
    sender = os.environ['ADDRESS_1']
    reciever = os.environ['ADDRESS_2']
    signature = os.environ['PRIVATE_KEY_1']
    amount = 7.5

    connection.transfer_ETH(sender, reciever, signature, amount)
