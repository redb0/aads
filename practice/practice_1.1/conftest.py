"""Локальный плагин для pytest"""


import math
import timeit
import pytest


SETUP_CODE = 'from array import array; a = array("i")'
APPEND_CODE = '''
for i in range(10_000):
    a.append(i)
'''


def pytest_collection_modifyitems(items):
    """Динамическое добавление маркера таймаута"""
    for item in items:
        if "timeout_append" in item.nodeid:
            reference_time = timeit.timeit(
                APPEND_CODE, setup=SETUP_CODE, number=10_000
            )
            print(f'\n\033[33mЭталонное время: {reference_time} сек.\033[0m')
            reference_time = math.ceil(reference_time * 2.5)
            print(f'\033[33mВремя с поправкой: {reference_time} сек.\033[0m')
            item.add_marker(pytest.mark.timeout(reference_time))
