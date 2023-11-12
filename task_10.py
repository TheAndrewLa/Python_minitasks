import functools


class LRUCache:
    def __init__(self, capacity=16):
        self.__capacity = capacity
        self.__used = 0

        # Out element is a tuple (key, value, using_index)
        # Last used element has (capacity - 1) index
        # Oldest used element has (capacity - used) index
        self.__elements = []

        # Custom sort function (we'll sort our array after every get and put)
        # After the sorting element with the highest index (last recent) will be first
        self.__sorted = functools.partial(sorted, key=lambda x: x[2], reversed=True)

    def put(self, key, value):
        if self.__used == self.__capacity:
            # Pushing our element to head of the list
            # Remove last element (the oldest)
            self.__elements.insert(0, (key, value, self.__capacity))
            self.__elements.pop(-1)

            # Reducing the indices
            # So index of the newest will be (capacity - 1) and of the oldest - zero
            for i in self.__elements:
                i[2] -= 1

        else:
            self.__elements.insert(0, (key, value, self.__capacity))

            # Reducing the indices
            # So index of the newest will be (capacity - 1)
            for i in self.__elements:
                i[2] -= 1

            self.__used += 1

    def get(self, key, value):
        element = None

        for i in self.__elements:
            if i[0] != key:
                i[2] -= 1
            else:
                i[2] = self.__capacity - 1
                element = i

        self.__elements = self.__sorted(self.__elements)

        return element[1]
