from importlib.machinery import SourceFileLoader
from time import perf_counter


def raw_load_module(ruta: str):
    # noinspection PyArgumentList
    _module = SourceFileLoader("module.name", ruta).load_module()
    # deprecated, but I don't understand how to use the new method.
    return _module


perf_counter()
module = raw_load_module('04/solutions.py')
print('\nPerformed in {} seconds'.format(perf_counter()))
