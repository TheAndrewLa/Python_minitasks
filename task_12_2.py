import typing


def chain(*iterables) -> typing.Iterable:
    class NewIterator:
        def __init__(self, iters: list[typing.Iterable]):
            self.__iterables = [i for i in iters]
            self.__index = 0

            self.__cur = iter(self.__iterables[0])

        def __next__(self):
            try:
                return next(self.__cur)

            except StopIteration:
                if self.__index == len(self.__iterables) - 1:
                    raise StopIteration

                else:
                    self.__index += 1
                    self.__cur = iter(self.__iterables[self.__index])
                    return next(self.__cur)

        def __iter__(self):
            return self

    return NewIterator(list(iterables))


print(list(chain([1, 2, 3], 'hello', [4, 5, 6])))
