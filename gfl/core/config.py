from typing import (
    Union,
    Type
)

from torch.nn.modules.loss import _Loss
from torch.optim import Optimizer
from torch.optim.lr_scheduler import _LRScheduler
from torch.nn import Module

from gfl.core.strategy import *


class Config(object):

    def __init__(self):
        super(Config, self).__init__()

    def _get_name(self, obj, strategy_type):
        if type(obj) == strategy_type:
            return obj, None
        if type(obj) == str:
            return strategy_type(str), None
        if strategy_type is None:
            return None, obj.__name__
        return strategy_type.USER_DEFINED, obj.__name__


class TrainConfig(Config):

    def __init__(self,
                 model: Union[str, Type],
                 epoch: int = 10,
                 batch_size: int = 32,
                 **kwargs):
        super(TrainConfig, self).__init__()
        _, self.model = self._get_name(model, None)
        self.optimizer, self.optimizer_strategy, self.optimizer_args = None, OptimizerStrategy.OPTIM_SGD, {}
        self.loss, self.loss_strategy, self.loss_args = None, LossStrategy.CROSSENTROPY_LOSS, {}
        self.scheduler, self.scheduler_strategy, self.scheduler_args = None, SchedulerStrategy.STEPLR, {}

        self.epoch = epoch
        self.batch_size = batch_size
        self.args = kwargs.copy() if kwargs is not None else {}

    def with_optimizer(self, optimizer: Union[str, OptimizerStrategy, Type], **kwargs):
        self.optimizer_strategy, self.optimizer = self._get_name(optimizer, OptimizerStrategy)
        self.optimizer_args = kwargs.copy() if kwargs is not None else {}
        return self

    def with_loss(self, loss: Union[str, LossStrategy, Type], **kwargs):
        self.loss_strategy, self.loss = self._get_name(loss, LossStrategy)
        self.loss_args = kwargs.copy() if kwargs is not None else {}
        return self

    def with_scheduler(self, scheduler: Union[str, SchedulerStrategy, Type], **kwargs):
        self.scheduler_strategy, self.scheduler = self._get_name(scheduler, SchedulerStrategy)
        self.scheduler_args = kwargs.copy() if kwargs is not None else {}
        return self

    def with_epoch(self, epoch: int):
        self.epoch = epoch
        return self

    def with_batch_size(self, batch_size: int):
        self.batch_size = batch_size
        return self

    def with_args(self, **kwargs):
        self.args = kwargs.copy() if kwargs is not None else {}

    def to_dict(self):
        ret = {
            "epoch": self.epoch,
            "batch_size": self.batch_size,
            "args": self.args,
            "model": self.model,
            "optimizer": {
               "name": self.optimizer,
               "strategy": self.optimizer_strategy.value,
               "args": self.optimizer_args
            },
            "loss": {
                "name": self.loss,
                "strategy": self.loss_strategy.value,
                "args": self.loss_args
            },
            "scheduler": {
                "name": self.scheduler,
                "strategy": self.scheduler_strategy.value,
                "args": self.scheduler_args
            }
        }
        return ret

    def from_dict(self, d):
        self.epoch = d["epoch"]
        self.batch_size = d["batch_size"]
        self.args = d["args"]
        self.model = d["model"]
        self.optimizer = d["optimizer"]["name"]
        self.optimizer_strategy = d["optimizer"]["strategy"]
        self.optimizer_args = d["optimizer"]["args"]
        self.loss = d["loss"]["name"]
        self.loss_strategy = d["loss"]["strategy"]
        self.loss_args = d["loss"]["args"]
        self.scheduler = d["scheduler"]["name"]
        self.scheduler_strategy = d["scheduler"]["strategy"]
        self.scheduler_args = d["scheduler"]["args"]
        return self


class AggregateConfig(object):

    def __init__(self):
        super(AggregateConfig, self).__init__()
        self.aggregate_strategy = None
        self.aggregate = None
