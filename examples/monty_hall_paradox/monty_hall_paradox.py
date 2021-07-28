import random
from typing import Tuple


def estimate_probability(n: int, num_goat: int =2) -> Tuple[float, float]:
    """Monty hall paradox

    Wiki:
        https://en.wikipedia.org/wiki/Monty_Hall_problem

    Parameters
    ----------
    :param n: number of repetitions of the experiment, n >= 1
    :type n: int
    :param num_goat: number of doors with goats, num_goat >= 1
    :type num_goat: int

    Returns
    -------
    :return: Tuple[float, float]
        The first element is the probability without changing the choice.
        The second element is probability with choice change.
    """
    CAR, GOAT = 'car', 'goat'
    DOORS = [CAR] + [GOAT] * num_goat
    p_with_change = 0
    p_without_change = 0

    for _ in range(n):
        doors = DOORS[:]
        random.shuffle(doors)
        player_choice = random.choice(doors)
        p_without_change += (player_choice == CAR)
        doors.remove(player_choice)
        while len(doors) > 1:
            doors.remove(GOAT)
        p_with_change += (doors[0] == CAR)
    
    return p_without_change / n, p_with_change / n


def main():
    num_goat = 2
    for i in range(10_000, 110_000, 10_000):
        p_1, p_2 = estimate_probability(i, num_goat)
        print(f'{i: >6}: P without change {p_1:.6f}, P with change {p_2:.6f}')


if __name__ == '__main__':
    main()
