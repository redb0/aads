"""Кривая дракона

Wiki:
    https://en.wikipedia.org/wiki/L-system#Example_7:_Fractal_plant

:Authors:
    - Electro98
"""


import turtle


START_AXIOM = 'x'
LEN_STEP = 5
NUMBER_STEP = 6
ROTATION_ANGLE = 25


def fractal_plant(axiom: str) -> str:
    """Фрактальное растение представленное с помощью L-системы

    Wiki: https://en.wikipedia.org/wiki/L-system

    :param axiom: аксиома, состояние системы
    :type axiom: str
    :return: новое состояние системы
    :rtype: str
    """
    rules = {
        'x': 'f+[[x]-x]-f[-fx]+x',
        'f': 'ff',
    }
    return ''.join([rules[char] if char in rules else char for char in axiom])


def main():
    """Простой пример визуализации кривой"""
    # настройки черепахи
    turtle.tracer(0, 0)
    turtle.pensize(1)
    turtle.hideturtle()
    turtle.setup(800, 800)
    turtle.penup()
    turtle.setposition(-400, -400)
    turtle.setheading(60)
    turtle.pendown()

    old_str = START_AXIOM
    new_str = ''

    # вычисление результирующей строки
    for _ in range(NUMBER_STEP):
        new_str = fractal_plant(old_str)
        old_str = new_str

    stack = []

    # рисование кривой
    for char in new_str:
        if char == 'f':
            turtle.forward(LEN_STEP)
        elif char == '+':
            turtle.left(ROTATION_ANGLE)
        elif char == '-':
            turtle.right(ROTATION_ANGLE)
        elif char == '[':
            turtle_state = turtle.pos(), turtle.heading()
            stack.append(turtle_state)
        elif char == ']':
            turtle_state = stack.pop()
            turtle.penup()
            turtle.goto(turtle_state[0])
            turtle.setheading(turtle_state[1])
            turtle.pendown()

    turtle.mainloop()


if __name__ == '__main__':
    main()
