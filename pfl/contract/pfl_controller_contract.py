# Copyright (c) 2020 GalaxyLearning Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import json
from pfl.contract.contract_config import *
from pfl.exceptions.fl_expection import PFLException


class PFLController(object):

    def __init__(self, web3):

        if web3 is None:
            raise PFLException("__init__() missing 1 positional argument")

        self.web3 = web3

        with open(PFL_CONTROLLER_CONTRACT_ABI, "r") as abi_f:
            abi = json.loads(abi_f.read())
        with open(PFL_CONTROLLER_CONTRACT_BIN, "r") as bin_f:
            bytecode = json.loads(bin_f.read())['object']
        pre_contract = self.web3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = pre_contract.constructor().transact()
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        if tx_receipt is None:
            raise PFLException("Deploy PFLController Contract fail!")

        self.pfl_controller_contract_address = tx_receipt.contractAddress

        self.pfl_controller_contract = self.web3.eth.contract(address=self.pfl_controller_contract_address, abi=abi)

    def addMap(self, job_id, contract_address):
        tx_hash = self.pfl_controller_contract.functions.addMap(str(job_id), contract_address).transact({'from': self.web3.eth.coinbase, 'gas': GAS_PRICE})
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        if tx_receipt is None:
            return True
        return False



    def getContractAddress(self, job_id):
        pfl_storage_contract_address = self.pfl_controller_contract.functions.getContractAddress(str(job_id)).call()
        return pfl_storage_contract_address