# Парадокс Монти Холла

Парадокс Монти Холла это задача теории вероятности. Она моделирует
следующую ситуацию:

>Представьте, что вы стали участником игры, в которой вам нужно выбрать
>одну из трёх дверей. За одной из дверей находится автомобиль, за двумя
>другими дверями — козы. Вы выбираете одну из дверей, например, номер 1,
>после этого ведущий, который знает, где находится автомобиль, а
>где — козы, открывает одну из оставшихся дверей, например, номер 3,
>за которой находится коза. После этого он спрашивает вас — не желаете
>ли вы изменить свой выбор и выбрать дверь номер 2? Увеличатся ли ваши
>шансы выиграть автомобиль, если вы примете предложение ведущего и
>измените свой выбор?

Wiki: https://en.wikipedia.org/wiki/Monty_Hall_problem

## Требования к реализации

Реализуйте программу для моделирования этой задачи. Напишите функцию со
следующей сигнатурой:

```python
estimate_probability(n: int, num_goat: int =2) -> Tuple[float, float]:
```

Описание параметров:
- ```n```       : число испытаний, по которым будет определяться вероятность
- ```num_goat```: число коз, участвующих в игре, напомним, что число
                  дверей будет на 1 больше чем число коз.

Результатом работы функции должно быть два числа - вероятность победы
без изменения двери и с изменением.
