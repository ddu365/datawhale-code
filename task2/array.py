class DynamicArray:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._array = [None] * self._capacity
        self._size = 0

    def __str__(self):
        return str([e for e in self])

    def __iter__(self):
        for i in range(self._capacity):
            yield self._array[i]

    def __len__(self):
        return self._size

    # 读
    def __getitem__(self, item):
        if not 0 <= item < self._capacity:
            raise IndexError('index out of range')
        return self._array[item]

    # 改
    def __setitem__(self, key, value):
        if not 0 <= key < self._capacity:
            raise IndexError('index out of range')
        self._array[key] = value

    # 删
    def __delitem__(self, key):
        if not 0 <= key < self._capacity:
            raise IndexError('index out of range')
        self._array[key] = None
        self._size -= 1

    # 增
    def append(self, value):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        self._array[self._size] = value
        self._size += 1

    def get_capacity(self):
        return self._capacity

    def _resize(self, capacity):
        tmp = [None] * capacity
        self._capacity = capacity
        for i in range(self._size):
            tmp[i] = self._array[i]
        self._array = tmp


# import numpy as np
# arr = np.arange(0,10)
#
# print(arr)
# print(type(arr))
#
#
# a = [a for a in range(10)]
# a.insert(3,6)
# print(a)
# a.remove(a[3])
# print(a)
# a[0] = 11
# print(a)
# del a[1]
# print(a)