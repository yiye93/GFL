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


GAS_PRICE = 0x2fefd8

PFL_CONTROLLER_CONTRACT_ABI = os.path.join(os.path.abspath("."), "pfl_controller_contract_src/PFLController.abi")
PFL_CONTROLLER_CONTRACT_BIN = os.path.join(os.path.abspath("."), "pfl_controller_contract_src/PFLController.bin")
PFL_CONTROLLER_CONTRACT_SOL = os.path.join(os.path.abspath("."), "pfl_controller_contract_src/PFLController.sol")

PFL_STORAGE_CONTRACT_ABI = os.path.join(os.path.abspath("."), "pfl_storage_contract_src/PFLStorage.abi")
PFL_STORAGE_CONTRACT_BIN = os.path.join(os.path.abspath("."), "pfl_storage_contract_src/PFLStorage.bin")
PFL_STORAGE_CONTRACT_SOL = os.path.join(os.path.abspath("."), "pfl_storage_contract_src/PFLStorage.sol")

