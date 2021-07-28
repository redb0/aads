from typing import List


def golomb_seq(n: int=1) -> int:
    """Последовательность Голомба

    Вычисления проводятся по рекурсивной формуле.

    Wiki:
        https://en.wikipedia.org/wiki/Golomb_sequence

    :param n: номер числа, defaults to 1
    :type n: int, optional
    :return: n-е число из последовательности Голомба
    :rtype: int
    """
    if n == 1:
        return 1
    return 1 + golomb_seq(n - golomb_seq(golomb_seq(n - 1)))


def golomb_lst(n: int=1) -> List[int]:
    """Последовательность Голомба

    Вычисления проводятся по рекурсивной формуле на основе списка.

    Wiki:
        https://en.wikipedia.org/wiki/Golomb_sequence

    :param n: количество чисел, defaults to 1
    :type n: int, optional
    :return: n первых чисел последовательности Голомба
    :rtype: List[int]
    """
    g = [1]
    for i in range(1, n):
        g.append(1 + g[i - g[g[i - 1] - 1]])
    return g


def silverman_seq(*args, **kwargs):
    """Последовательность Сильвермана

    Wiki:
        https://en.wikipedia.org/wiki/Golomb_sequence
    """
    return golomb_lst(*args, **kwargs)


def golomb_cl(n: int=1) -> List[int]:
    """Кластера последовательности Голомба

    :param n: количество кластеров, defaults to 1
    :type n: int, optional
    :return: n первых кластеров последовательности Голомба
    :rtype: List[int]
    """
    g = [1, 2, 2]
    if 1 <= n <= 2:
        return g[:n + 1]
    for i in range(3, n + 1):
        g += [i] * g[i-1]
    return g


def main():
    recursive = map(str, [golomb_seq(i) for i in range(1, 11)])
    from_list = map(str, golomb_lst(10))
    clusters = map(str, golomb_cl(3))
    print(f'Recursion : {" ".join(recursive)}')
    print(f'List based: {" ".join(from_list)}')
    print(f'Clusters  : {" ".join(clusters)}')


if __name__ == '__main__':
    main()
