"""Простые шифры

- шифр Виженера

Wiki:
    https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

:Authors:
    - Voronov Vladimir
"""


ALPHABET_SIZE = 26
SHIFT = 97


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


def vigenere_encryption(text: str, key: str) -> str:
    """Кодирование шифром Виженера

    :param text: шифруемый текст
    :type text: str
    :param key: ключ, должен быть равен длине текста
    :type key: str
    :return: шифр
    :rtype: str
    """
    result = ''.join(
        [chr((ord(m) + ord(key[i % len(key)]) - 2*SHIFT) % ALPHABET_SIZE+SHIFT) for i, m in enumerate(text)]
    )
    return result


def vigenere_decryption(text: str, key: str) -> str:
    """Декодирование шифра Виженера

    :param text: расшифровываемый текст
    :type text: str
    :param key: ключ
    :type key: str
    :return: исходный текст
    :rtype: str
    """
    result = ''.join(
        [chr((ord(m) - ord(key[i % len(key)]) + 26) % 26+97) for i, m in enumerate(text)]
    )
    return result


def main():
    """Пример"""
    text = 'attackatdown'
    key_word = 'lemon'

    key = create_key(text, key_word)
    print(key)
    result = vigenere_encryption(text, key)
    print(result)
    print(vigenere_decryption(result, key))


if __name__ == '__main__':
    main()
