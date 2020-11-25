

class TrainConfig(object):

    def __init__(self):
        super(TrainConfig, self).__init__()
        self.model = None
        self.optimizer_strategy = None
        self.optimizer_object = None
        self.loss_strategy = None
        self.loss_object = None
        self.scheduler_strategy = None
        self.scheduler_object = None

        self.distillation_alpha = None
        self.l2_dist = None
        self.epoch = None

        self.batch_size = None


class AggregateConfig(object):

    def __init__(self):
        super(AggregateConfig, self).__init__()
        self.aggregate_strategy = None
        self.aggregate_object = None