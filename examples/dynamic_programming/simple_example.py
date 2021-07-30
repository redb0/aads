"""Простые примеры использования динамического программирования

:Authors:
    - Voronov Vladimir
"""

from typing import Optional, Sequence, Union


ItemType = Union[int, float]


def my_len(seq: Sequence) -> int:
    """Функция длины, использует подход динамического программирования

    :param seq: Последовательность, длину которой нужно узнать
    :type seq: Sequence
    :return: длина последовательности
    :rtype: int
    """
    if not seq:
        return 0
    return 1 + my_len(seq[1:])


def my_max(seq: Sequence[ItemType]) -> Optional[ItemType]:
    """Максимальный элемент последовательности

    Использует подход динамического программирования.

    :param seq: последовательность
    :type seq: Sequence[ItemType]
    :return: максимальный элемент последовательности
    :rtype: ItemType
    """
    if not seq:
        return None
    if len(seq) == 2:
        if seq[0] >= seq[1]:
            return seq[0]
        return seq[1]
    new_max = my_max(seq[1:])
    if new_max is not None:
        if seq[0] >= new_max:
            return seq[0]
        return new_max
    return seq[0]


def main():
    """Пример использования функций"""
    sequence_a = [1, 2, 3, 4, 5]
    sequence_b = (1, 2, 9, 4, 5, 1, 3)
    print(f'Длина последовательности a: {my_len(sequence_a)}')
    print(f'Длина последовательности b: {my_len(sequence_b)}')
    print('-' * 50)
    print(f'Максимум последовательности a: {my_max(sequence_a)}')
    print(f'Максимум последовательности b: {my_max(sequence_b)}')


if __name__ == '__main__':
    main()
