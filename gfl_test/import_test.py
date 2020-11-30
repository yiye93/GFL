from gfl_test.gfl_model.model import Net
from gfl_test.gfl_model.others import Optimizer


class A(object):

    def __init__(self, p1, p2, p3):
        super(A, self).__init__()
        print(p1)
        print(p2)
        print(p3)


class B(A):

    pass


if __name__ == "__main__":
    b = B(p1="1", p2="2", p3="3")