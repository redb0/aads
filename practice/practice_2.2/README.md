# Практическая работа №7 "Лабиринты"

Реализовать консольную утилиту (или приложение с графическим
интерфейсом) для генерации и решения лабиринтов.

Предусмотреть:
1. Интерфейс командной строки (CLI) или графический интерфейс
2. Возможность указывать размеры лабиринта (изображения)
3. Генерацию лабиринта и сохранение его в виде изображения `jpg`, `png`
(выходной файл указывает пользователь)
4. Сохранение лабиринта в виде любого **текстового** формата
5. Загрузку лабиринта из текстового файла
6. Загрузку лабиринта из изображения
7. Решение лабиринта
8. Вывод пути от начальной до конечной точек
9. Покрыть тестами генерацию и решение лабиринта
10. *Генерация гифки построения и решения лабиринта

## Алгоритмы:

### Генерация

1. Алгоритм Эйлера
2. Алгоритм Краскала
3. Алгоритм двоичного дерева
4. Алгоритм Прима
5. Алгоритм «Sidewinder»
6. Рекурсивный алгоритм сегментации

### Решение

1. А*
2. Best-first search
3. Jump Point Search
4. Поиск в глубину (DFS, Depth-first search)
5. Алгоритм Дейкстры
6. Алгоритм Левита
7. Поиск в ширину (BFS, Breadth-first search)
8. Алгоритм Ли (Волновой алгоритм)

##  Требования к реализации

Реализуйте модуль ```maze.py``` с функциями генерации и решения лабиринта.

Функция генерации должна принимать размеры лабиринта, а также
дополнительные параметры алгоритма (по необходимости) и возвращать
лабиринт в любом удобном представлении, например в виде двумерного
массива или графа.

Функция решения должна принимать представление лабиринта, а также
дополнительные параметры алгоритма (по необходимости) и возвращать
его решение в любом удобном представлении, например, в виде массива
точек или графа.

Остальной функционал (чтение, запись в файл, генерация изображения и
другие) должен располагаться в соответствующих функциях.

<!-- ## Входные и выходные данные -->

## Методика оценивания

Оценка выставляется в соответствии со следующими требованиями:

1) Общие требования:
    - код работы проходит проверку утилитой `pylint` с конфигурационным файлом `.pylintrc`.
    - код работы успешно проходит тесты, если таковые имеются.
    - наличие документации к функциям, методам, классам и модулям.
2) На оценку 3 балла реализовать:
    - все вышеперечисленное;
    - пункты 1, 2, 3, 7 и 8.
3) На оценку 4 балла дополнительно реализовать:
    - все вышеперечисленное;
    - пункты 4 и 5;
4) На оценку 5 балла:
    - реализовать все требования, указанные в описании к работе, кроме 10.
5) Плюс в карму:
    - все вышеперечисленное;
    - пункт 10;

## Полезные материалы

- [Best-first search](https://en.wikipedia.org/wiki/Best-first_search)
- [Eller's Algorithm](http://www.neocomputer.org/projects/eller.html)
- [Maze Generation: Eller's Algorithm](http://weblog.jamisbuck.org/2010/12/29/maze-generation-eller-s-algorithm)
- [Как пройти через лабиринт не заблудившись](http://ega-math.narod.ru/Nquant/Maze.htm)
- [Поиск A*](https://ru.wikipedia.org/wiki/A*)
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Алгоритм Левита](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D0%B5%D0%B2%D0%B8%D1%82%D0%B0)
- [Алгоритм Ли](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9B%D0%B8)
- [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [Shortest Path](https://harablog.wordpress.com/2011/09/07/jump-point-search/)
- [Алгоритм поиска пути Jump Point Search](https://habr.com/ru/post/162915/)
- [Классические алгоритмы генерации лабиринтов. Часть 1: вступление](https://habr.com/ru/post/320140/)
- [Классические алгоритмы генерации лабиринтов. Часть 2: погружение в случайность](https://habr.com/ru/post/321210/)
- [Алгоритм Эллера для генерации лабиринтов](https://habr.com/ru/post/176671/)
- [Maze Classification](http://www.astrolog.org/labyrnth/algrithm.htm)
- [Алгоритм поиска путей в лабиринте](https://habr.com/ru/post/198266/)
- [Методы программирования. Обходы графа](https://hci.fenster.name/304y/practice/lab6/)
- [Генерация и решение лабиринта с помощью метода поиска в глубину по графу](https://habr.com/ru/post/262345/)
- [Алгоритм Эйлера на C++](https://github.com/lpestl/Maze#11-%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC)
- [Реализация и визуализация четырех алгоритмов генерации лабиринта](https://russianblogs.com/article/89641288190/)
- [Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Maze Generation: Sidewinder algorithm](http://weblog.jamisbuck.org/2011/2/3/maze-generation-sidewinder-algorithm)
- [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [Лабиринты: классификация, генерирование, поиск решений](https://habr.com/ru/post/445378/)
- [OBLIGE Level Maker](http://oblige.sourceforge.net/)
- [Bake Your Own 3D Dungeons With Procedural Recipes](https://gamedevelopment.tutsplus.com/tutorials/bake-your-own-3d-dungeons-with-procedural-recipes--gamedev-14360)
