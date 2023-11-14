from typing import Any
from collections import namedtuple


class LRUCache:
    CacheElement = namedtuple('CacheElement', ['key', 'value'])

    # Element are stored in array by the next rules:
    # 1) Recently used element is at the top of list
    # 2) Getting element moves element to the top of the list
    # 3) Putting element inserts element to the top. And if we're out of capacity we'll remove last element
    # 4) All keys in the elements list should be unique

    def __init__(self, capacity: int = 16):
        self.__capacity = capacity
        self.__used = 0
        self.__elements: list[LRUCache.CacheElement] = []

        self.__keys: set = set([])

    def put(self, key, value):
        tmp = self.__keys
        tmp.add(key)

        if len(tmp) == len(self.__keys):
            return

        if self.__used == self.__capacity:
            self.__elements.pop(-1)
        else:
            self.__used += 1

        self.__elements.insert(0, LRUCache.CacheElement(key, value))

    def get(self, key) -> Any:
        for i in self.__elements:
            if i.key == key:
                self.__elements.remove(i)
                self.__elements.insert(0, i)
                return i.value

        return None
