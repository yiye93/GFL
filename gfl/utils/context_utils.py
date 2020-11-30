import sys


class SystemPackageContext(object):

    def __init__(self):
        super(SystemPackageContext, self).__init__()
        self.path = sys.path

    def __enter__(self):

        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class ContextUtils(object):

    pass