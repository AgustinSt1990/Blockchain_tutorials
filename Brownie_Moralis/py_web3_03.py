import os
from dotenv import load_dotenv
from web3 import Web3
import py_web3_01 as moral01
import py_web3_02 as moral02


def get_nonce(ETH_address):
    return w3.eth.get_transaction_count(ETH_address)

def transfer_ETH(sender, reciever, signature, amount_ETH):
    global global_gas, global_gasPrice
    tx_body = {
        'nonce':get_nonce(sender),
        'to': reciever,
        'value': w3.toWei(amount_ETH, 'ether'),
        'gas': global_gas,
        'gasPrice': global_gasPrice
    }
        
    signed_tx = w3.eth.account.sign_transaction(tx_body, signature)
    result = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return result



if __name__ == '__main__':

    load_dotenv()
    node_provider=os.environ['NODE_PROVIDER_LOCAL']
    w3 = Web3(Web3.HTTPProvider(node_provider))

    global_gas = 4500000
    global_gasPrice = w3.toWei(8, 'gwei')   



    ####################################################
    # # # #            MAIN PROGRAM            # # # # # 
    ####################################################

    moral01.are_we_connected()
    
    sender = os.environ['ADDRESS_2']
    reciever = os.environ['ADDRESS_1']
    signature = os.environ['PRIVATE_KEY_2']
    amount = 7.5

    print (transfer_ETH(sender, reciever, signature, amount))
