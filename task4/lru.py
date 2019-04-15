from functools import lru_cache
import urllib


class LRUCache:

    def __init__(self, capacity: int):
        import collections
        self.capacity = capacity
        self._cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if self._cache.get(key):
            val = self._cache.pop(key)
            self._cache[key] = val
            return self._cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self._cache.get(key):
            self._cache.pop(key)
            self._cache[key] = value
        else:
            if len(self._cache) == self.capacity:
                self._cache.popitem(last=False)
            self._cache[key] = value


# python 内置lru缓存
@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'


for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
    pep = get_pep(n)
    print(n, len(pep))


print(get_pep.cache_info())


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print([fib(n) for n in range(16)])

print(fib.cache_info())
