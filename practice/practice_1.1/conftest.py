"""Локальный плагин для pytest"""


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
            print(f'\nЭталонное время: {reference_time = }')
            reference_time = round(reference_time * 1.125)
            print(f'Время с поправкой: {reference_time = }')
            item.add_marker(pytest.mark.timeout(reference_time))
