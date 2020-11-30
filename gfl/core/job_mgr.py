import inspect
import json
import os
import shutil

from gfl.conf import job_dir
from gfl.conf.fl_config import *
from gfl.entity import Job
from gfl.utils import JobUtils


train_conf_filename = "train.conf"
aggregate_conf_filename = "aggregate.conf"
job_conf_filename = "job.conf"
sqlite_db_filename = "job.sqlite"


class JobMgr(object):

    def __init__(self):
        super(JobMgr, self).__init__()

    @classmethod
    def generate_job(cls, module,
                     job_config: JobConfig = JobConfig(),
                     train_config: TrainConfig = TrainConfig(),
                     aggregate_config: AggregateConfig = AggregateConfig()):
        job_id = JobUtils.generate_job_id()
        job = Job(job_id, job_config, train_config, aggregate_config)
        cls.__submit_model(job_id, module)
        cls.__write_conf(job_id, job_config, job_conf_filename)
        cls.__write_conf(job_id, train_config, train_conf_filename)
        cls.__write_conf(job_id, aggregate_config, aggregate_conf_filename)
        return job

    @classmethod
    def submit_job(cls, job_id):
        pass

    @classmethod
    def get_job(cls, job_id):
        if not os.path.exists(os.path.join(job_dir, job_id)):
            return None
        job_config = cls.__read_conf(job_id, JobConfig(), job_conf_filename)
        train_config = cls.__read_conf(job_id, TrainConfig(), train_conf_filename)
        aggregate_config = cls.__read_conf(job_id, AggregateConfig(), aggregate_conf_filename)
        return Job(job_id, job_config, train_config, aggregate_config)

    @classmethod
    def __submit_model(cls, job_id, module):
        return cls.__submit_module(job_id, module, "fl_model")

    @classmethod
    def __submit_data(cls, job_id, module):
        return cls.__submit_module(job_id, module, "fl_data")

    @classmethod
    def __submit_module(cls, job_id, module, pack):
        job_path = os.path.join(job_dir, job_id)
        os.makedirs(job_path, exist_ok=True)
        module_path = inspect.getsourcefile(module)
        if module_path.endswith("__init__.py"):
            shutil.copytree(os.path.dirname(module_path), os.path.join(job_path, pack))
        else:
            shutil.copy(module, os.path.join(job_path, pack + ".py"))

    @classmethod
    def __verify_job_api(cls, job):
        pass

    @classmethod
    def __write_conf(cls, job_id, config: Config, filename):
        conf_file = os.path.join(job_dir, job_id, filename)
        with open(conf_file, "w") as f:
            d = config.to_dict()
            f.write(json.dumps(d, indent=4))

    @classmethod
    def __read_conf(cls, job_id, config: Config, filename):
        conf_file = os.path.join(job_dir, job_id, filename)
        with open(conf_file, "r") as f:
            config.from_dict(json.loads(f.read()))
        return config
