from torch.optim import SGD
from torch.nn.modules.loss import CrossEntropyLoss
from torch.optim.lr_scheduler import ReduceLROnPlateau


class Optimizer(SGD):
    """
    lr=0.1
    """
    pass


class Loss(CrossEntropyLoss):

    pass


class Scheduler(ReduceLROnPlateau):
    """
    optimizer,
    mode='max',
    factor=0.5,
    patience=5
    """
    pass