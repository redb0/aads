"""Тесты для модуля my_sort"""

import csv
import os
import unittest
import shutil

from external_sort import external_natural_merge_sort as my_sort  # pylint: disable=E0401

TEST_NUMBER = [
    [],
    [1],
    [1, 2, 3, 4, 5],
    [0, 0, 0, 55, 55, 60],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [8, 0, 42, 3, 4, 8, 0, 45, 50, 9999, 7],
    [-5, 0, 9, -999, 874, 35, -4, -5, 0],
    [1, 1, 1],
]

TEST_STR = [
    [],
    ["a"],
    ["a", "b", "c", "d", "e"],
    ["aa", "aa", "aa", "ab", "ac", "b"],
    ["e", "d", "c", "b", "a"],
    ["abc", "a", "foo", "bar", "booz", "baz", "spam", "love"],
    ["abc", "abc", "abc"],
    [""],
]

TEST_FLOAT = [
    [],
    [1.0],
    [1.0, 2.0, 3.0, 4.0, 5.0],
    [0.0, 0.0, 0.0, 55.0, 55.0, 60.0],
    [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 0.2, 0.1, 0.0],
    [8.0, 0.0, 42.0, 3.0, 4.0, 8.0, 0.0, 0.45, 0.50, 9999.0, 7.0],
    [-5.0, 0.0, 9.0, -999.0, 874.0, 35.0, -4.0, -5.0, 0.0],
    [0.1, 1.0, 0.1],
]

TEST_MORE_TXT = [
    [[], []],
    [[1], [-1000]],
    [[1, 2], [3, 4, 5]],
    [[0, 0, 0], [55, 55, 60]],
    [[9, 8, 7, 6, 5], [4, 3, 2, 1, 0]],
    [[8, 0, 42, 3, 4], [8, 0, 45, 50, 9999, 7]],
    [[-5, 0, 9, -999], [874, 35, -4, -5, 0]],
    [[1, 1], [1]],
]


class TestExternalSortOneFile(unittest.TestCase):
    """Тест-кейс модуля my_sort с одним файлом."""

    def setUp(self) -> None:
        """Создание файлов перед тестом."""
        self.file_name = "tests/test_sort_one_file.txt"
        self.dir_name = "tests"
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
        if not os.path.exists(self.file_name):
            open(self.file_name, "x", encoding="utf-8").close()

    def test_sort_number_increase(self) -> None:
        """Тест функции сортировки числовых данных по возрастанию и txt файла."""
        for data in TEST_NUMBER:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output="",
                    reverse=False,
                    key="",
                    type_data="i",
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(int(ptr.readline()))
                self.assertEqual(exit_lst, sorted(data))

    def test_sort_number_decrease(self) -> None:
        """Тест функции сортировки числовых данных по невозрастанию и txt файла."""
        for data in TEST_NUMBER:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output="",
                    reverse=True,
                    key="",
                    type_data="i",
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(int(ptr.readline()))
                self.assertEqual(exit_lst, sorted(data, reverse=True))

    def test_sort_str_increase(self) -> None:
        """Тест функции сортировки строковых данных по возрастанию и txt файла."""
        for data in TEST_STR:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(item + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output="",
                    reverse=False,
                    key="",
                    type_data="s",
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(ptr.readline().replace("\n", ""))
                self.assertEqual(exit_lst, sorted(data, reverse=False))

    def test_sort_str_decrease(self) -> None:
        """Тест функции сортировки строковых данных по невозрастанию и txt файла."""
        for data in TEST_STR:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output="",
                    reverse=True,
                    key="",
                    type_data="s",
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(ptr.readline().replace("\n", ""))
                self.assertEqual(exit_lst, sorted(data, reverse=True))

    def test_sort_float_increase(self) -> None:
        """Тест функции сортировки чисел с плавающей точкой по возрастанию."""
        for data in TEST_FLOAT:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output="",
                    reverse=False,
                    key="",
                    type_data="f",
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(float(ptr.readline()))
                self.assertEqual(exit_lst, sorted(data, reverse=False))

    def test_sort_float_decrease(self) -> None:
        """Тест функции сортировки чисел с плавающей точкой по невозрастанию."""
        for data in TEST_FLOAT:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output="",
                    reverse=True,
                    key="",
                    type_data="f",
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(float(ptr.readline()))
                self.assertEqual(exit_lst, sorted(data, reverse=True))


    def tearDown(self) -> None:
        """Действия после окончания теста."""
        shutil.rmtree(self.dir_name)


class TestExternalSortCSVFile(unittest.TestCase):
    """Тест-кейс модуля my_sort с csv файлами."""

    def setUp(self) -> None:
        """Создание файлов перед тестом."""
        self.file_name = "tests/test_sort_csv.csv"
        self.dir_name = "tests"
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
        if not os.path.exists(self.file_name):
            open(self.file_name, "x", encoding="utf-8").close()

    def test_sort_csv_file(self) -> None:
        """Тест функции сортировки csv файла"""
        key = "sort"
        for data in TEST_NUMBER:
            file = open(self.file_name, "w", encoding="utf-8")
            file.write("")
            file.close()
            ptr = open(self.file_name, "a", newline="", encoding="utf-8")
            writer = csv.DictWriter(ptr, fieldnames=[key])
            writer.writeheader()
            for i in data:
                writer.writerow({key: int(i)})
            ptr.close()
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output="",
                    reverse=False,
                    key=key,
                    type_data="i",
                )
                exit_file = []
                ptr = open(self.file_name, "r", encoding="utf-8")
                reader = csv.DictReader(ptr)
                for _ in range(len(data)):
                    exit_file.append(int(next(reader)[key]))
                ptr.close()
                self.assertEqual(exit_file, sorted(data))

    def tearDown(self) -> None:
        """Действия после окончания теста."""
        shutil.rmtree(self.dir_name)

class TestExternalSortTwoFile(unittest.TestCase):
    """Тест-кейс модуля my_sort c двумя файлами."""

    def setUp(self) -> None:
        """Создание файлов перед тестом."""
        self.file_name_first = "tests/test_sort_more_txt_files_1.txt"
        self.file_name_second = "tests/test_sort_more_txt_files_2.txt"
        self.dir_name = "tests"
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
        if not os.path.exists(self.file_name_first):
            open(self.file_name_first, "x", encoding="utf-8").close()
        if not os.path.exists(self.file_name_second):
            open(self.file_name_second, "x", encoding="utf-8").close()

    def test_sort_more_txt_files(self) -> None:
        """Тест функции сортировки нескольких txt файлов"""
        for data in TEST_MORE_TXT:
            with open(self.file_name_first, "w", encoding="utf-8") as ptr:
                for item in data[0]:
                    ptr.write(str(item) + "\n")
            with open(self.file_name_second, "w", encoding="utf-8") as ptr:
                for item in data[1]:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                data = [sorted(data[0]), ] + [sorted(data[1]), ]
                my_sort(
                    src=[self.file_name_first, self.file_name_second],
                    output="",
                    reverse=False,
                    key="",
                    type_data="i",
                )
                exit_lst_first, exit_lst_second = [], []
                first_flag, second_flag = True, True
                with open(self.file_name_first, "r", encoding="utf-8") as ptr:
                    for i in range(len(data[0])):
                        exit_lst_first.append(int(ptr.readline()))
                        if data[0][i] != exit_lst_first[i]:
                            first_flag = False
                with open(self.file_name_second, "r", encoding="utf-8") as ptr:
                    for i in range(len(data[1])):
                        exit_lst_second.append(int(ptr.readline()))
                        if data[1][i] != exit_lst_second[i]:
                            second_flag = False
                self.assertEqual(first_flag and second_flag, True)

    def test_sort_more_files_with_output(self) -> None:
        """Тест функции сортировки нескольких txt файлов с выходным файлом"""
        output = "tests/test_sort_more_txt_files_output.txt"
        if not os.path.exists(output):
            open(output, "x", encoding="utf-8").close()
        for data in TEST_MORE_TXT:
            file = open(output, "w", encoding="utf-8")
            file.write("")
            file.close()
            with open(self.file_name_first, "w", encoding="utf-8") as ptr:
                for item in data[0]:
                    ptr.write(str(item) + "\n")
            with open(self.file_name_second, "w", encoding="utf-8") as ptr:
                for item in data[1]:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                data = sorted(data[0] + data[1])
                my_sort(
                    src=[self.file_name_first, self.file_name_second],
                    output=output,
                    reverse=False,
                    key="",
                    type_data="i",
                )
                output_file = []
                with open(output, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        output_file.append(int(ptr.readline()))
                self.assertEqual(output_file, data)

    def tearDown(self) -> None:
        """Действия после окончания теста."""
        shutil.rmtree(self.dir_name)
