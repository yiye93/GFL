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

import json
from pfl.contract.contract_config import *
from pfl.exceptions.fl_expection import PFLException


class PFLStorage(object):

    def __init__(self, web3=None, account=None, password=None, pfl_storage_contract_address=None):

        if web3 is None or account is None or password is None:
            raise PFLException("__init__() missing 1 positional argument")

        self.web3 = web3
        self.password = password
        self.web3.eth.defaultAccount = self.web3.toChecksumAddress(account)
        self.web3.geth.personal.unlockAccount(web3.eth.coinbase, self.password)

        if not pfl_storage_contract_address:
            with open(PFL_STORAGE_CONTRACT_ABI, "r") as abi_f:
                abi = json.loads(abi_f.read())
            with open(PFL_STORAGE_CONTRACT_BIN, "r") as bin_f:
                bytecode = json.loads(bin_f.read())['object']
            pre_contract = self.web3.eth.contract(abi=abi, bytecode=bytecode)
            tx_hash = pre_contract.constructor().transact()
            tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
            if tx_receipt is None:
                raise PFLException("Deploy PFLStorage Contract fail!")

            self.pfl_storage_contract_address = tx_receipt.contractAddress

            self.pfl_storage_contract = self.web3.eth.contract(address=self.web3.toChecksumAddress(self.pfl_storage_contract_address), abi=abi)
        else:
            with open(PFL_STORAGE_CONTRACT_ABI, "r") as abi_f:
                abi = json.loads(abi_f.read())
            self.pfl_storage_contract_address = pfl_storage_contract_address
            self.pfl_storage_contract = self.web3.eth.contract(address=self.web3.toChecksumAddress(self.pfl_storage_contract_address), abi=abi)

    def store_client_url(self, client_url):
        tx_hash = self.pfl_storage_contract.functions.storeClientUrl(client_url).trasact(
            {'from': self.web3.eth.coinbase, 'gas': GAS_PRICE})
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def retreive_all_client_urls(self):
        client_urls = self.pfl_storage_contract.functions.retreiveAllClientsUrls().call()
        return client_urls

    def retreive_client_urls_length(self):
        client_urls_length = self.pfl_storage_contract.functions.retreiveAllClientsUrls().call()
        return client_urls_length

    def store_client_address(self, client_address):
        tx_hash = self.pfl_storage_contract.functions.storeClientAddress(client_address).trasact(
            {'from': self.web3.eth.coinbase, 'gas': GAS_PRICE})
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def retreive_client_address_length(self):
        client_address_length = self.pfl_storage_contract.functions.retreiveClientAddressLength().call()
        return client_address_length

    def store_epoch_model_file(self, epoch_num, model_ipfs_hash, file_name):
        tx_hash = self.pfl_storage_contract.functions.storeEpochModelFile(epoch_num, model_ipfs_hash, file_name).trasact(
            {'from': self.web3.eth.coinbase, 'gas': GAS_PRICE})
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt


    def retrieve_model_files(self, epoch_num):
        model_files = self.pfl_storage_contract.functions.retrieveModelFiles(epoch_num).call()
        return model_files


    def store_aggregated_model_file(self, epoch_num, model_ipfs_hash, file_name):
        tx_hash = self.pfl_storage_contract.functions.storeAggregatedModelFile(epoch_num, model_ipfs_hash,
                                                                          file_name).trasact(
            {'from': self.web3.eth.coinbase, 'gas': GAS_PRICE})
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def retrieve_aggregated_model_file(self, epoch_num):
        model_file = self.pfl_storage_contract.functions.retreiveAggregatedModelFile(epoch_num).call()
        return model_file


    def retrieve_ipfs_hash_file_name(self, ipfs_hash):

        file_name = self.pfl_storage_contract.functions.retrieveIpfsHashName(ipfs_hash).call()
        return file_name