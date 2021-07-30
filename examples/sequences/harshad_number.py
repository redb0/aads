"""Числа Нивена, нивенморфные числа, множественные числа Нивена"""


from typing import Generator, List, Tuple


HARSHAD = 'Harshad number'
NIVENMORPHIC = 'Nivenmorphic number'


def sum_of_digits(number: int) -> int:
    """Сумма цифр"""
    return sum(map(int, list(str(number))))


def harshad_number(start: int, end: int) -> List[Tuple[int, str]]:
    """Поиск чисел Нивена и невенморфных чисел в интервале

    :param start: начало интервала, включительно
    :type start: int
    :param end: конец интервала, не включается
    :type end: int
    :return: список пар (число, метка) для найденных чисел Нивена и
             невенморфных чисел
    :rtype: List[Tuple[int, str]]
    """
    numbers = []
    for i in range(start, end):
        sum_d = sum(int(j) for j in list(str(i)))
        if not i % sum_d:
            str_dum = str(sum_d)
            if str(i)[-len(str_dum):] == str_dum:
                numbers.append((i, NIVENMORPHIC))
            else:
                numbers.append((i, HARSHAD))
    return numbers


def harshad_number_one_line(start: int, end: int):
    """Реализация поиска чисел Нивена и невенморфных чисел в одну строку

    Не стоит реализовывать такие длинные однострочники.
    """
    return [
        (i, NIVENMORPHIC) if str(i)[-len(str(b)):] == str(b) else (i, HARSHAD) for i in range(start, end) if not i % (b:=sum(int(j) for j in list(str(i))))  # pylint: disable=line-too-long
    ]


def multiple_harshad_number(number: int, *, max_iter: int=100) -> Tuple[bool, int]:
    """Множественные числа Нивена

    :param number: проверяемое число
    :type number: int
    :param max_iter: максимальное число итераций проверки
    :type max_iter: int
    :return: пара (метка, число шагов), где первый элемент равен True,
             если число является множественным числом Нивена,
             и False в противном случае
    :rtype: Tuple[bool, int]
    """
    i = 0
    while number != 1 and max_iter > 0:
        sum_digits = sum_of_digits(number)
        if not number % sum_digits:
            number = number // sum_digits
            i += 1
            max_iter -= 1
        else:
            break
    else:
        return number == 1, i
    return False, i


def multiple_harshad_range(start: int, end: int, max_iter: int=100) -> Generator[Tuple[int, bool, int], None, None]:
    """Поиск множественных чисел Нивена в виде генератора"""
    for i in range(start, end):
        flag, number_iter = multiple_harshad_number(i, max_iter=max_iter)
        yield i, flag, number_iter


def main():
    """Примеры"""
    print(f'Числа Нивена: {harshad_number(11, 30)}')
    print(f'Проверка числа 6804 на множественное число: {multiple_harshad_number(6804)}')


if __name__ == '__main__':
    main()
