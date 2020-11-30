from enum import Enum

from gfl.core.strat import Strategy


class Object(object):

    def __init__(self, obj=None, **kwargs):
        super(Object, self).__init__()
        self.name, self.strategy = self.__get_name(obj)
        self.args = kwargs.copy() if kwargs is not None else {}
        self.is_instance = type(obj) != type

    def __get_name(self, obj):
        if obj is None:
            return None, None
        else:
            if type(obj) == str:
                return obj, Strategy.USER_DEFINED.value
            if isinstance(obj, Enum):
                return None, obj.value
            return obj.__name__, Strategy.USER_DEFINED.value

    def to_dict(self):
        return {
            "name": self.name,
            "strategy": self.strategy,
            "args": self.args,
            "is_instance": self.is_instance
        }

    def from_dict(self, dt: dict):
        if dt is not None:
            self.name = dt.get("name")
            self.strategy = dt.get("strategy")
            self.args = dt.get("args")
            self.is_instance = dt.get("is_instance")
        return self


class Config(object):

    def __init__(self, **kwargs):
        super(Config, self).__init__()
        self.__init_fields()
        self.args = {}
        if kwargs is not None:
            for k, v in kwargs.items():
                if k in type(self).__dict__.items():
                    setattr(self, k, v)
                else:
                    self.args[k] = v

    def __init_fields(self):
        for k, v in type(self).__dict__.items():
            if not k.startswith("_") and not k.endswith("_") and not callable(getattr(type(self), k)):
                setattr(self, k, v[0](*v[1:]))

    def to_dict(self):
        return {
            "args": self.args
        }

    def from_dict(self, dt: dict):
        self.args = dt.get("args")


class TrainConfig(Config):

    epoch = (int, 10)
    batch_size = (int, 32)
    model = (Object, None)
    optimizer = (Object, None)
    scheduler = (Object, None)
    loss = (Object, None)

    def __init__(self, **kwargs):
        super(TrainConfig, self).__init__(**kwargs)

    def with_epoch(self, epoch=10):
        self.epoch = epoch
        return self

    def with_batch_size(self, batch_size=32):
        self.batch_size = batch_size
        return self

    def with_model(self, model, **kwargs):
        self.model = Object(model, **kwargs)
        return self

    def with_optimizer(self, optimizer, **kwargs):
        self.optimizer = Object(optimizer, **kwargs)
        return self

    def with_scheduler(self, scheduler, **kwargs):
        self.scheduler = Object(scheduler, **kwargs)
        return self

    def with_loss(self, loss, **kwargs):
        self.loss = Object(loss, **kwargs)
        return self

    def to_dict(self):
        ret = super(TrainConfig, self).to_dict()
        ret.update({
            "model": self.model.to_dict(),
            "optimizer": self.optimizer.to_dict(),
            "scheduler": self.scheduler.to_dict(),
            "loss": self.loss.to_dict(),
            "epoch": self.epoch,
            "batch_size": self.batch_size
        })
        return ret

    def from_dict(self, dt: dict):
        super(TrainConfig, self).from_dict(dt)
        self.model = Object().from_dict(dt.get("model"))
        self.optimizer = Object().from_dict(dt.get("optimizer"))
        self.scheduler = Object().from_dict(dt.get("scheduler"))
        self.loss = Object().from_dict(dt.get("loss"))
        self.epoch = dt.get("epoch")
        self.batch_size = dt.get("batch_size")
        return self


class AggregateConfig(Config):

    aggregator = (Object, None)
    epoch = (int, )

    def __init__(self, **kwargs):
        super(AggregateConfig, self).__init__(**kwargs)

    def with_epoch(self, epoch):
        self.epoch = epoch
        return self

    def with_aggregator(self, aggregator, **kwargs):
        self.aggregator = Object(aggregator, **kwargs)
        return self

    def to_dict(self):
        ret = super(AggregateConfig, self).to_dict()
        ret.update({
            "epoch": self.epoch,
            "aggregator": self.aggregator.to_dict()
        })
        return ret

    def from_dict(self, dt: dict):
        super(AggregateConfig, self).from_dict(dt)
        self.epoch = dt.get("epoch")
        self.aggregator = Object().from_dict(dt.get("aggregator"))
        return self


class JobConfig(Config):

    owner = (str, )
    create_time = (int, )

    def __init__(self, **kwargs):
        super(JobConfig, self).__init__(**kwargs)

    def to_dict(self):
        ret = super(JobConfig, self).to_dict()
        ret.update({
            "owner": self.owner,
            "create_time": self.create_time
        })
        return ret

    def from_dict(self, dt: dict):
        super(JobConfig, self).from_dict(dt)
        self.owner = dt.get("owner")
        self.create_time = dt.get("create_time")


if __name__ == "__main__":
    train_config = TrainConfig()