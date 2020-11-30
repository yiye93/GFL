import gfl_test

import importlib
import json
import os

from torch.utils.data import DataLoader

import gfl
from gfl.conf import job_dir
from gfl.core.config import TrainConfig
from gfl.core.train import Trainer
from gfl.core.job_mgr import JobMgr

from gfl_test.gfl_data import MnistDataset


path = "res/job/e584462b2a673705a7d878244c5582f1"
pack = path.replace("/", ".") + ".model"


if __name__ == "__main__":
    job = JobMgr.get_job("dc64d3ffac523f42859c7703dd4f141f")
