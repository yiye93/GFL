from gfl.conf.fl_config import TrainConfig, AggregateConfig, JobConfig


class Job(object):

    def __init__(self, job_id, job_config, train_config, aggregate_config):
        super(Job, self).__init__()
        self.job_id: str = job_id
        self.job_config: JobConfig = job_config
        self.train_config: TrainConfig = train_config
        self.aggregate_config: AggregateConfig = aggregate_config
