"""Последовательность Голомба

Wiki:
    https://en.wikipedia.org/wiki/Golomb_sequence
"""

from typing import List


def golomb_seq(number: int=1) -> int:
    """Последовательность Голомба

    Вычисления проводятся по рекурсивной формуле.

    Wiki:
        https://en.wikipedia.org/wiki/Golomb_sequence

    :param number: номер числа, defaults to 1
    :type number: int, optional
    :return: n-е число из последовательности Голомба
    :rtype: int
    """
    if number == 1:
        return 1
    return 1 + golomb_seq(number - golomb_seq(golomb_seq(number - 1)))


def golomb_lst(number: int=1) -> List[int]:
    """Последовательность Голомба

    Вычисления проводятся по рекурсивной формуле на основе списка.

    Wiki:
        https://en.wikipedia.org/wiki/Golomb_sequence

    :param number: количество чисел, defaults to 1
    :type number: int, optional
    :return: n первых чисел последовательности Голомба
    :rtype: List[int]
    """
    sequence = [1]
    for i in range(1, number):
        sequence.append(1 + sequence[i - sequence[sequence[i - 1] - 1]])
    return sequence


def silverman_seq(*args, **kwargs):
    """Последовательность Сильвермана

    Wiki:
        https://en.wikipedia.org/wiki/Golomb_sequence
    """
    return golomb_lst(*args, **kwargs)


def golomb_cl(number: int=1) -> List[int]:
    """Кластера последовательности Голомба

    :param number: количество кластеров, defaults to 1
    :type number: int, optional
    :return: n первых кластеров последовательности Голомба
    :rtype: List[int]
    """
    sequence = [1, 2, 2]
    if 1 <= number <= 2:
        return sequence[:number + 1]
    for i in range(3, number + 1):
        sequence += [i] * sequence[i-1]
    return sequence


def main():
    """Демонстрация работы"""
    recursive = map(str, [golomb_seq(i) for i in range(1, 11)])
    from_list = map(str, golomb_lst(10))
    clusters = map(str, golomb_cl(3))
    print(f'Recursion : {" ".join(recursive)}')
    print(f'List based: {" ".join(from_list)}')
    print(f'Clusters  : {" ".join(clusters)}')


if __name__ == '__main__':
    main()
