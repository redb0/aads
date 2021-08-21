"""Monty hall paradox

Wiki:
    https://en.wikipedia.org/wiki/Monty_Hall_problem
"""

import random
from typing import Tuple


CAR, GOAT = 'car', 'goat'


def estimate_probability(number: int, num_goat: int =2) -> Tuple[float, float]:
    """Monty hall paradox

    Wiki:
        https://en.wikipedia.org/wiki/Monty_Hall_problem

    Parameters
    ----------
    :param number: number of repetitions of the experiment, n >= 1
    :type number: int
    :param num_goat: number of doors with goats, num_goat >= 1
    :type num_goat: int

    Returns
    -------
    :return: Tuple[float, float]
        The first element is the probability without changing the choice.
        The second element is probability with choice change.
    """

    DOORS = [CAR] + [GOAT] * num_goat  # pylint: disable=C0103

    p_with_change = 0
    p_without_change = 0

    for _ in range(number):
        doors = DOORS[:]
        random.shuffle(doors)
        player_choice = random.choice(doors)
        p_without_change += (player_choice == CAR)
        doors.remove(player_choice)
        while len(doors) > 1:
            doors.remove(GOAT)
        p_with_change += (doors[0] == CAR)

    return p_without_change / number, p_with_change / number


def main():
    """Демонстрация работы"""
    num_goat = 2
    for i in range(10_000, 110_000, 10_000):
        p_1, p_2 = estimate_probability(i, num_goat)
        print(f'{i: >6}: P without change {p_1:.6f}, P with change {p_2:.6f}')


if __name__ == '__main__':
    main()
