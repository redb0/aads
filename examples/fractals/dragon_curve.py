"""Кривая дракона

Wiki:
    https://en.wikipedia.org/wiki/Dragon_curve

:Authors:
    - Voronov Vladimir
"""


import turtle


START_AXIOM = 'fx'
LEN_STEP = 10
NUMBER_STEP = 10


def dragon_curve(axiom: str) -> str:
    """Кривая дракона представленная в виде L-системы

    Wiki: https://en.wikipedia.org/wiki/L-system

    :param axiom: аксиома, состояние системы
    :type axiom: str
    :return: новое состояние системы
    :rtype: str
    """
    rules = {
        'x': 'x+yf+',
        'y': '-fx-y',
    }
    return ''.join([rules[char] if char in rules else char for char in axiom])


def main():
    """Простой пример визуализации кривой"""
    # настройки черепахи
    turtle.tracer(0, 0)
    dragon = turtle.Turtle()
    dragon.pensize(2)
    dragon.hideturtle()

    old_str = START_AXIOM
    new_str = ''

    # вычисление результирующей строки
    for _ in range(NUMBER_STEP):
        new_str = dragon_curve(old_str)
        old_str = new_str

    # рисование кривой
    for char in new_str:
        if char == 'f':
            dragon.forward(LEN_STEP)
        elif char == '+':
            dragon.right(90)
        elif char == '-':
            dragon.left(90)

    turtle.mainloop()


if __name__ == '__main__':
    main()
