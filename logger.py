import sys


def log(*args):
    print(args)


def error_log(*args, **kwargs):
    print(args, file=sys.stderr)
