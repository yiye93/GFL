from web3 import Web3


if __name__ == "__main__":
    w3 = Web3()
    acc = w3.eth.account.create()
    print(acc.key.hex())
    print(acc.address)
    print(acc.privateKey.hex())
