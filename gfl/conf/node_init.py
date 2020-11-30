import json
import os

from web3 import Web3

from gfl.conf.path import key_file


w3 = Web3()


def init_node_id():
    global w3
    account = w3.eth.account.create()
    key_json = {
        "address": account.address[2:],
        "key": account.key.hex()[2:]
    }
    with open(key_file, "w") as f:
        f.write(json.dumps(key_json, indent=4))


def read_node_id():
    with open(key_file, "r") as f:
        key_dict = json.loads(f.read())
        return key_dict["address"], key_dict["key"]


if not os.path.exists(key_file):
    init_node_id()

node_id, priv_key = read_node_id()