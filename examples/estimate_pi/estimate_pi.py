"""Оценка числа Пи

Для оценки используется только генератор случайных чисел равномерно распределенных 0 до 1.

Этот метод называется методом Монте-Карло.

Wiki: https://en.wikipedia.org/wiki/Monte_Carlo_method
"""

from random import uniform
from typing import Generator, Tuple


def generate_points(number: int) -> Generator[Tuple[float, float], None, None]:
    """Generating points in a 1x1 rectangle"""
    return ((uniform(0, 1), uniform(0, 1)) for _ in range(number))


def estimate_pi(number: int) -> float:
    """Estimating pi based on a random number generator.

    Calculations based on expression:
        (pi * R**2) / (2*R)**2 = number_points_in_circle / n
        pi = 4 * number_points_in_circle / n

    where: R - circle radius, R = 1;
           n - number of points.

    Parameters
    ----------
    :param number: number of points, n >= 1
    :type number: int

    Returns
    -------
    :return: float
        Estimating pi.
    """
    points = generate_points(number)
    points_in_circle = 0
    for x, y in points:
        points_in_circle += (x**2 + y**2 <= 1)
    return 4 * points_in_circle / number


def main():
    """Демонстрация работы"""
    for i in range(100_000, 500_000, 10_000):
        e_pi = estimate_pi(i)
        print(f'pi estimate at {i} points: {e_pi}')


if __name__ == '__main__':
    main()
