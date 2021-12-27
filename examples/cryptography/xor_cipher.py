"""Простые шифры

- XOR-шифрование

Wiki:
    https://en.wikipedia.org/wiki/XOR_cipher

:Authors:
    - Voronov Vladimir
"""


import itertools
from typing import Iterable


def create_key(text: str, key_word: str) -> str:
    """Создание ключа

    Циклическое повторение ключевого слова.

    :param text: шифруемый текст
    :type text: str
    :param key: ключевое слово
    :type key: str
    :return: ключ
    :rtype: str
    """
    return ''.join([key_word[i % len(key_word)] for i in range(len(text))])


def xor_cipher(string: Iterable[str], key: Iterable[str]) -> str:
    """XOR шифр

    :param string: Шифруемый/расшифровываемый текст
    :type string: Iterable[str]
    :param key: Ключ
    :type key: Iterable[str]
    :return: Текст после шифровки/дешифровки
    :rtype: str
    """
    key = itertools.cycle(key)
    result = []

    for string_char, key_char in zip(string, key):
        char = chr(ord(string_char) ^ ord(key_char))
        result.append(char)

    return "".join(result)


def xor_cipher_one_line(string: Iterable[str], key: Iterable[str]) -> str:
    """XOR шифр

    Однострочный вариант

    :param string: Шифруемый/расшифровываемый текст
    :type string: Iterable[str]
    :param key: Ключ
    :type key: Iterable[str]
    :return: Текст после шифровки/дешифровки
    :rtype: str
    """
    return "".join(chr(ord(s_c) ^ ord(k_c)) for s_c, k_c in zip(string, key))


def main():
    """Пример"""
    string = 'Wiki'
    key_word = chr(int('11110011', 2))

    print(f'String: {string!r}')
    print(f'Key word: {key_word!r}')

    key = create_key(string, key_word)
    result = xor_cipher(string, key)

    print(f'Encrypted text: {result!r}')

    result = xor_cipher(result, key)

    print(f'Decrypted text: {result!r}')


if __name__ == '__main__':
    main()
