# Практическая работа №1 "Массивы и бинарный поиск"

Реализуйте модуль для языка программирования Python для работы с
массивами. 

Предусмотрите следующие возможности модуля:
- создание динамических массивов для чисел разных типов(целые (`long`),
числа с плавающей точкой (`double`));
- создание пустого массива;
- создание массива, заполненного заранее заданными данными;
- реализуйте следующие функции для работы с массивом:
    - добавление элемента в конец массива (`append`);
    - вставка элемента в нужную позицию (`insert`);
    - удаление первого вхождения элемента в массив (`remove`);
    - удаление первого вхождения элемента в массив с возвратом (`pop`);
    - инвертирование массива (`__reversed__` для поддержки функции `reversed`);
    - определение длины массива (поддержка функции `len`);
    - определение количества памяти, занимаемой массивом (`sys.getsizeof`, `__sizeof__`);
    - сравнение со стандартным массивом из модуля array или списком (`__eq__`);
- возможность итерирования по массиву;
- алгоритм бинарного поиска, возвращающий индекс найденного элемента
или `None` если ничего не найдено

Не забудьте предусмотреть
[функцию изменения размера](https://en.wikipedia.org/wiki/Dynamic_array),
которая будет работать "под капотом".

Для большей справки можно обратиться к
[документации](https://docs.python.org/3/library/array.html) модуля
`array` стандартной библиотеки Python.

##  Требования к реализации

Модуль `dynamic_array` необходимо реализовать как Си расширение для
Python. Это можно выполнить с помощью Cython - специальной надстройки
для Python, позволяющей вызывать функции из Си напрямую, а также
обладающей приближенным к Python синтаксисом. Документацию по Cython
см. в полезных материалах. Также можно сразу реализовать этот модуль на
языке Си и подключить его к Python с помощью Cython.

Обратите внимание, что при реализации на Cython или Си обертка на Python
вокруг массива **не нужна**. Здесь `dynamic_array` содержит обертку
только для тестов.

<!-- В Python модуле
необходимо реализовать класс `Array`, которы будет служить оберткой над
вашим модулем на Си или Cython. -->

Метод инициализации класса `Array` должен принимать два аргумента:
- код типа в виде строки, `'d'` для чисел с плавающей точкой и `'i'`
для целых чисел;
- набор инициализирующих данных, которые сразу будут занесены в массив.

Интерфейс методов и функций должен быть аналогичен методам модуля
`array` стандартной библиотеки Python.

Модуль `binary_search`, содержащий реализацию бинарного поиска
разрешается реализовать на Python. Этот модуль должен поддерживать
работу с объектами из `dynamic_array`.

```python
search(array: Iterable, item: Any=False) -> Optional[int]:
```

В файлах `dynamic_array.py` и `binary_search.py` размещены упрощенные
шаблоны классов и функций. В Файлах `test_dynamic_array.py` и
`test_binary_search.py` размещены тесты для проверки решения. Тесты
можно запустить с помощью модуля `unittest` или `pylint`.

В файле `my_array.pyx` приведен пример реализации расширения для Python
на Cython. Для компиляции этого модуля необходимо создать файл
`setup.py` пример которого можно найти в текущей директории. Затем
достаточно выполнить команду:

```bash
python setup.py build_ext --inplace
```

По завершении выполнения компиляции и при отсутствии ошибок появятся файлы:
- `my_array.c`
- `my_array.cp39-win_amd64.pyd`
- а также директория `build`

В файле `my_array.cp39-win_amd64.pyd` будет содержаться скомпилированный
модуль, его можно использовать как обычный модуль Python. Для удобства
его можно переименовать в `my_array.pyd`.

Для прохождения тестов вам понадобиться `pytest` и плагин
`pytest-timeout`. Установить их можно командами:

```bash
python -m pip install pytest
python -m pip install pytest-timeout
```

Также нужен файл `conftest.py` расположите его рядом с тестами.
Подробнее об этом файле можно узнать в
[документации](https://docs.pytest.org/en/latest/example/markers.html).

Запустить тесты можно командой:

```bash
pytest test_dynamic_array.py -s
```

## Входные и выходные данные

Пример входных данных для бинарного поиска:

Исходный список: ```[-3, 0, 2, 5, 5]```, ```0```<br>
Результат: ```1```<br>

Исходный список: ```[-3, 0, 2, 5, 5]```, ```5```<br>
Результат: ```3```<br>

Исходный список: ```[-3, 0, 2, 5, 5]```, ```10```<br>
Результат: ```None```<br>

## Методика оценивания

Оценка выставляется в соответствии со следующими требованиями:

1) Общие требования:
    - код работы проходит проверку утилитой `pylint` с конфигурационным
    файлом `.pylintrc`.
    - код работы успешно проходит тесты, если таковые имеются.
    - наличие документации к модулям, функциям, классам и методам.
    - наличие аннотации типов.
2) На оценку 3 балла:
    - реализовать методы `append`, `insert`, `remove`, `__eq__`.
3) На оценку 4 балла:
    - дополнительно реализовать методы `pop`, `reverse`.
4) На оценку 5 балла:
    - реализовать все методы, указанные в описании к работе. 

## Полезные материалы

- [Cython tutorial](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html)
- [Memory Allocation in Cython](https://cython.readthedocs.io/en/latest/src/tutorial/memory_allocation.html)
- [Использование Cython для ускорения вычислений в Python](http://www.machinelearning.ru/wiki/images/5/52/Cython_Nikolaev.pdf)
- [Cython. A Guide for Python Programmers](http://www.jyguagua.com/wp-content/uploads/2017/03/OReilly.Cython-A-Guide-for-Python-Programmers.pdf)
- [Python `__reverse__` magic method](https://stackoverflow.com/questions/27638960/python-reverse-magic-method)
- [Binary Search in Java](https://stackabuse.com/binary-search-in-java/)
<!-- - [How to implement dynamic array in Python](https://www.educative.io/edpresso/how-to-implement-dynamic-array-in-python) -->
