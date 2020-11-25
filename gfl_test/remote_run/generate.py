import gfl_test

import inspect

import gfl_test.inst as inst
from gfl_test.inst import Net


if __name__ == "__main__":
    src = inspect.getsourcefile(Net)
    print(src)
    print(type(src))