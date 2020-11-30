from enum import Enum


class Strategy(Enum):
    USER_DEFINED = "UserDefined"
    NONE = "None"


class OptimizerStrategy(Enum):
    SGD = "SGD"
    ADAM = "Adam"


class SchedulerStrategy(Enum):
    CYCLICLR = "CyclicLR"
    COSINEANNEALINGLR = "CosineAnnealingLR"
    EXPONENTIALLR = "ExponentialLR"
    LAMBDALR = "LambdaLR"
    MULTISTEPLR = "ReduceLROnPlateau"
    STEPLR = "StepLR"


class LossStrategy(Enum):
    L1 = "L1loss"
    MSE = "MSELoss"
    CROSSENTROPY = "CrossEntropyLoss"
    NLL = "NLLLoss"
    POISSIONNLL = "PoissonNLLLoss"
    KLDIV = "KLDivLoss"
    BCE = "BCELoss"
    BCEWITHLOGITS = "BCEWithLogitsLoss"
    MARGINRANKING = "MarginRankingloss"


class WorkModeStrategy(Enum):
    WORKMODE_STANDALONE = "standalone"
    WORKMODE_CLUSTER = "cluster"


class FederateStrategy(Enum):
    FED_AVG = "fed_avg"
    FED_DISTILLATION = "fed_distillation"


class AggregateStrategy(Enum):
    FED_AVG = "fed_avg"
    FED_DISTILLATION = "fed_distillation"
