from pfl.utils.ethereum_utils import PFLEthereumUtils
import os
import json
# from pfl.contract.contract_bytecode import bytecode
import time



if __name__ == "__main__":

    web3 = PFLEthereumUtils.get_connection_with_ethereum(url="http://10.5.18.241:8545")
    # print(web3.eth.accounts)

    web3.eth.defaultAccount = web3.eth.coinbase
    web3.geth.personal.unlockAccount(web3.eth.coinbase, "abc")

    ##部署智能合约
    with open("/Users/huyifan/Documents/PFL/pfl/contract/test_contract_src/test.bin", "r") as bytecode_f:
        bytecode = json.loads(bytecode_f.read())['object']
    with open("/Users/huyifan/Documents/PFL/pfl/contract/test_contract_src/test.abi", "r") as abi_f:
        abi = json.loads(abi_f.read())
    # my_contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    # tx_hash = my_contract.constructor().transact()
    # tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    # contract_address = tx_receipt.contractAddress
    # print("new contract address: ", contract_address)

    contract_address = "0x504094c2eea131c1ccea449dfa6b8618a8d5b78b"

    # 调用部署好的智能合约
    # contract_address = '0x4031db3d1f6a25c7ef06a48735a6b547c34ccb2f'
    contract_address = web3.toChecksumAddress(contract_address)
    # print(contract_address)
    # #private_key = "05EAD4C38EF65C1F721C662435B835BE5DF3E2E822D0274200B96A055B7C9C4E"
    # #
    contract = web3.eth.contract(abi=abi, address=contract_address)
    #
    # abi_path = "/Users/huyifan/Documents/PFL/pfl/contract/PFLStorage.abi"
    # with open(abi_path, "r") as abi_f:
    #     contract_abi = abi_f.read()
    # my_contract = web3.eth.contract(address=contract_address, abi=abi)
    # print(my_contract.abi)
    # result = contract.functions.retreiveAllClientUrl().call()
    # gas = result.estimateGas()
    # contract_source_file_path = os.path.join("/Users/huyifan/Documents/PFL/pfl/contract", "PFLStorage.sol")
    # compiled_contract = compile_contract(contract_source_file_path)
    # contract_id, contract_interface = compiled_contract.popitem()
    # contract_address = deploy_contract(web3, contract_interface)


    #
    # print(contract_address)
    #
    # txn_dict = contract.functions.storeClientUrl(bytes("127.0.0.1:8080", 'utf-8')).buildTransaction({
    #     'chainId': 20,
    #     'gasPrice': 25000000000,
    #     'gas': 0x271000,
    #     'nonce': web3.eth.getTransactionCount(web3.eth.coinbase)
    # })
    # signed_txn = web3.eth.account.signTransaction(txn_dict, private_key=private_key)
    # print(signed_txn)
    # result = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    ##work
    # web3.geth.personal.unlockAccount(web3.eth.coinbase, "abc")
    # result = my_contract.functions.setName("127.0.0.1:8080").transact({'from':web3.eth.coinbase, 'gas':web3.eth.gasPrice})
    # gas = result.estimateGas()
    #
    #result = web3.eth.sendTransaction(txn_dict)
    # gas_estimate = contract.functions.storeClientUrl(bytes("127.0.0.1:8080", 'utf-8')).estimateGas()
    #
    # while True:
    #     receipt = web3.eth.getTransactionReceipt(result.hex())
    #     time.sleep(2)
    #     if receipt != None:
    #         break
    # tx_receipt = web3.eth.waitForTransactionReceipt(result)
    # print(tx_receipt)

    # print(receipt['transactionHash'].hex())
    # print(web3.eth.getCode(contract_address))
    # print(my_contract.all_functions())
    # function_to_call = my_contract.get_function_by_name('helloworld')
    # print("function_to_call:", function_to_call)
    #result2 = contract.functions.getName().call({'from':web3.eth.coinbase})
    result2 = contract.functions.helloworld().call()
    #
    # while True:
    #     receipt = web3.eth.getTransactionReceipt(result2)
    #     time.sleep(2)
    #     if receipt != None:
    #         break
    #
    print(result2)

    # name = contract.functions.getName().call()
    # print("name: ", name)
    #
    # txHash = contract.functions.setName("huyifan").transact({'from':web3.eth.coinbase, 'gas':0x2fefd8})
    # receipt = web3.eth.waitForTransactionReceipt(txHash)
    # print("setName receipt: ", receipt)
    #
    # txHash2 = contract.functions.setName("Gueyue").transact({'from':web3.eth.coinbase, 'gas':0x2fefd8})
    # receipt2 = web3.eth.waitForTransactionReceipt(txHash2)
    # print("setName receipt: ", receipt2)
    #
    # name = contract.functions.getName().call()
    # print("name: ", name)
    #
    # names = contract.functions.getNames().call()
    # print("names: ", names)
