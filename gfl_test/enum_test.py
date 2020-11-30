from enum import Enum


class Strategy(Enum):

    USER_DEFINED = "UserDefined"
    NONE = "None"


class AggregateStrategy(Enum):

    FED_AVG = "FedAvg"
    FED_DISTILLATION = "FedDistillation"


if __name__ == "__main__":
    s = Strategy.USER_DEFINED
    print(type(s) == Strategy)
    print(type(s) == Enum)
    print(isinstance(s, Enum))