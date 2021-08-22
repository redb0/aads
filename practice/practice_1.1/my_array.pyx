# cython: language_level=3
# distutils: language = c

# Указываем компилятору, что используется Python 3 и целевой формат
# языка Си (во что компилируем, поддерживается Си и C++)


# Также понадобятся функции управления памятью
from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free

# Для преоразования Python объекта float в Сишный тип и обратно
from cpython.float cimport PyFloat_FromDouble, PyFloat_AsDouble


# Так как хотим использовать массив для разных типов, указывая только
# код типа без дополнительных замарочек, то используем самописный
# дескриптор. Он будет хранить функции получения и записи значения в
# массив для нужных типов. Упрощенны аналог дескриптора из модуля array:
# https://github.com/python/cpython/blob/243b6c3b8fd3144450c477d99f01e31e7c3ebc0f/Modules/arraymodule.c#L32
cdef struct arraydescr:
    # код типа, один символ
    char* typecode
    # размер одного элемента массива
    int itemsize
    # функция получения элемента массива по индексу. Обратите внимание,
    # что она возвращает Python тип object. Вот так выглядит сигнатура на Си:
    # PyObject * (*getitem)(struct arrayobject *, Py_ssize_t)
    object (*getitem)(array, size_t)
    # функция записи элемента массива по индексу. Третий аргумент это
    # записываемое значение, оно приходит из Python. Сигнатура на Си:
    # int (*setitem)(struct arrayobject *, Py_ssize_t, PyObject *)
    int (*setitem)(array, size_t, object)


cdef object double_getitem(array a, size_t index):
    # Функция получения значения из массива для типа double.
    # Обратите внимание, что Cython сам преобразует Сишное значение типа
    # double в аналогичны объект PyObject
    return (<double *> a.data)[index]


cdef int double_setitem(array a, size_t index, object obj):
    # Функция записи значения в массив для типа double. Здесь нужно
    # самими извлеч значение из объекта PyObject.
    if not isinstance(obj, int) and not isinstance(obj, float):
        return -1
    
    # Преобразования Python объекта в Сишный
    cdef double value = PyFloat_AsDouble(obj)

    if index >= 0:
        # Не забываем преобразовывать тип, т.к. a.data имеет тип char
        (<double *> a.data)[index] = value
    return 0


# Если нужно работать с несколькими типами используем массив дескрипторов:
# https://github.com/python/cpython/blob/243b6c3b8fd3144450c477d99f01e31e7c3ebc0f/Modules/arraymodule.c#L556
cdef arraydescr[1] descriptors = [
     arraydescr("d", sizeof(double), double_getitem, double_setitem),
]


# Зачатки произвольных типов, значения - индексы дескрипторов в массиве
cdef enum TypeCode:
    DOUBLE = 0


# преобразование строкового кода в число
cdef int char_typecode_to_int(str typecode):
    if typecode == "d":
        return TypeCode.DOUBLE
    return -1


cdef class array:
    # Класс статического массива.
    # В поле length сохраняем длину массива, а в поле data будем хранить
    # данне. Обратите внимание, что для data используем тип char,
    # занимающий 1 байт. Далее мы будем выделять сразу несколько ячеек
    # этого типа для одного значения другого типа. Например, для
    # хранения одного double используем 8 ячеек для char.
    cdef public size_t length
    cdef char* data
    cdef arraydescr* descr 

    # Аналог метода __init__
    def __cinit__(self, str typecode, size_t size):
        self.length = size

        cdef int mtypecode = char_typecode_to_int(typecode)
        self.descr = &descriptors[mtypecode]

        # Выделяем память для массива
        self.data = <char*> PyMem_Malloc(size * self.descr.itemsize)
        if not self.data:
            raise MemoryError()

    # Не забываем освобаждать память. Привязываем это действие к объекту
    # Python. Это позволяет освободить память во время сборки мусора.
    def __dealloc__(self):
        PyMem_Free(self.data)

    # Пользовательски метод для примера. Инициализация массива числами
    # от 0 до length - 1. В Cython можно использовать функции из Python,
    # они преобразуются в Сишные аналоги.
    def initialize(self):
        # Объявление переменно цикла позволяет эффективнее комплировать код.
        cdef int i
        for i in range(self.length):
            self.__setitem__(i, PyFloat_FromDouble(<double> i))
    
    # Добавим возможность получать элементы по индексу.
    def __getitem__(self, size_t index):
        if 0 <= index < self.length:
            # return (<double *> self.data)[index]
            return self.descr.getitem(self, index)
        raise IndexError()

    # Запись элементов по индексу.
    def __setitem__(self, size_t index, object value):
        if 0 <= index < self.length:
            self.descr.setitem(self, index, value)
        else:
            raise IndexError()
