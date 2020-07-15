# Copyright (c) 2019 GalaxyLearning Authors. All Rights Reserved.
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
import importlib
from pfl.utils.utils import JobUtils, CyclicTimer
from pfl.utils.ethereum_utils import PFLEthereumUtils
from pfl.entity.gfl_model import Model
from pfl.exceptions.fl_expection import PFLException
from pfl.core.strategy import WorkModeStrategy, FederateStrategy

JOB_PATH = os.path.join(os.path.abspath("."), "res", "jobs_client")
BASE_MODEL_PATH = os.path.join(os.path.abspath("."), "res", "models")


class FLClient(object):
    def __init__(self):
        super(FLClient, self).__init__()
        self.job_path = JOB_PATH
        self.base_model_path = BASE_MODEL_PATH


    def get_remote_pfl_models(self, server_url=None):
        if server_url is None:
            return self._get_models_from_local()
        else:
            return self._get_models_from_remote(server_url)


    def _get_models_from_local(self):
        model_list = []
        JobUtils.get_job_from_remote(None, self.job_path)
        job_list = JobUtils.list_all_jobs(self.job_path)

        for job in job_list:
            model = self._get_model_from_job(job)
            pfl_model = Model()
            pfl_model.set_model(model)
            pfl_model.set_job_id(job.get_job_id())
            model_list.append(pfl_model)
        return model_list

    def _get_models_from_remote(self, server_url):
        model_list = []
        JobUtils.get_job_from_remote(server_url, self.job_path)
        job_list = JobUtils.list_all_jobs(self.job_path)
        for job in job_list:
            model = self._get_model_from_job(job)
            pfl_model = Model()
            pfl_model.set_model(model)
            pfl_model.set_job_id(job.get_job_id())
            model_list.append(pfl_model)
        return model_list

    def _get_model_from_job(self, job):
        job_id = job.get_job_id()
        module = importlib.import_module("res.models.models_{}.init_model_{}".format(job_id, job_id),
                                         "init_model_{}".format(job_id))
        model_class = getattr(module, job.get_train_model_class_name())
        return model_class()



class FLClientBlockchain(FLClient):
    pass



class FLModelBlockchain(FLClient):

    def __init__(self, ethereum_url=None, model_client_blockchain_address=None, model_client_blockchain_address_password=None, federate_strategy=None):
        super(FLModelBlockchain, self).__init__()
        if ethereum_url is None or model_client_blockchain_address is None or model_client_blockchain_address_password is None:
            raise PFLException("parameter error")
        self.federate_strategy = federate_strategy
        self.server_blockchain_address = model_client_blockchain_address
        self.server_blockchain_address_password = model_client_blockchain_address_password
        self.work_mode = WorkModeStrategy.WORKMODE_BLOCKCHAIN
        self.ethereum_url = ethereum_url
        self.web3 = PFLEthereumUtils.get_connection_with_ethereum(self.ethereum_url)
        self.pfl_controller_contract = PFLEthereumUtils.init_pfl_controller_contracts(web3=self.web3,
                                                                                      account=self.server_blockchain_address,
                                                                                      account_password=self.server_blockchain_address_password)
        self.cyclic_timer = CyclicTimer(60, PFLEthereumUtils.block_support_function)

    def start(self):
        self.logger.info("Work Mode: {}".format(self.work_mode))
        self.logger.info("Successfully connected to Ethereum")
        if self.federate_strategy == FederateStrategy.FED_AVG:
            raise PFLException("Blockchain mode only allowed in FED_DISTILLATION federate strategy")
        self.cyclic_timer.start()
