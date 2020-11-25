import sys


def detect(lib, msg=None):
    try:
        exec("import " + lib)
    except:
        if msg is None:
            msg = lib + " not exists."
        print(msg, file=sys.stderr)


detect("torch")
detect("torchvision")
