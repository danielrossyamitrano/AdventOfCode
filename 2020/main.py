from importlib import import_module
from time import perf_counter
import json


def raw_load_module(ruta: str):
    name = ruta.replace('/', '.')
    return import_module(name, ruta)


def abrir_json(ruta, encoding='utf-8'):
    with open(ruta, 'r', encoding=encoding) as file:
        return json.load(file)


perf_counter()
module = raw_load_module('2020/'+abrir_json('day.json')+'/solutions')
print('\nPerformed in {} seconds'.format(perf_counter()))
