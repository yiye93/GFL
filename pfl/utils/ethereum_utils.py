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

from web3 import Web3
from pfl.exceptions.fl_expection import PFLException



class PFLEthereumUtils:

    @staticmethod
    def get_connection_with_ethereum(url=None):

        if url is None:
            raise PFLException("get_connection_with_ethereum() missing 1 positional argument")

        try:
            web3 = Web3(Web3.HTTPProvider(url))
        except Exception:
            raise PFLException("Connect to ethereum fail!!!")
        else:
            return web3