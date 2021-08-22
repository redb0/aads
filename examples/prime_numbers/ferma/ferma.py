"""Monty hall paradox

Wiki:
    https://en.wikipedia.org/wiki/Fermat_primality_test
"""

import math
import random


def ferma(number: int, k: int = 100) -> bool:
    """Тест простоты Ферма

    Wiki:
        https://en.wikipedia.org/wiki/Fermat_primality_test

    :param number: проверяемое число
    :type number: int
    :param k: количество тестов
    :type k: int, default 100
    :return: True если число псевдопростое, False если составное
    :rtype: bool
    """
    if number == 2:
        return True

    for _ in range(1, k + 1):
        random_number = (random.randint(1, number) % (number - 2)) + 2
        # проверка на взаимную простоту чисел random_number и number
        if math.gcd(random_number, number) != 1:
            return False
        # проверка условия теоремы Ферма, с использованием возведения
        # числа в степень по модулю
        if pow(random_number, number - 1, number) != 1:
            return False
    return True
