import gfl_test

import json

import gfl_test.gfl_model as gfl_model
from gfl.core.job_mgr import JobMgr
from gfl.conf.fl_config import TrainConfig
from gfl.core.strategy import OptimizerStrategy


if __name__ == "__main__":
    train_config = TrainConfig()\
        .with_model(gfl_model.Net)\
        .with_optimizer(OptimizerStrategy.OPTIM_SGD, lr=0.01)\
        .with_scheduler(gfl_model.Scheduler, mode="max", factor=0.5, patience=5)\
        .with_loss(gfl_model.Loss)

    # job = JobMgr.generate_job(gfl_model, train_config=train_config)
    # print(job.job_id)
    job = JobMgr.get_job("dc64d3ffac523f42859c7703dd4f141f")
    print(json.dumps(job.job_config.to_dict(), indent=4))
    print(json.dumps(job.train_config.to_dict(), indent=4))
    print(json.dumps(job.aggregate_config.to_dict(), indent=4))
