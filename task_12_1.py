import typing


def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break

    return res


def cycle(itr: typing.Iterable) -> typing.Iterable:
    class NewIterator:
        def __init__(self, iterable: typing.Iterable):
            self.__initial = iterable
            self.__cur = iter(iterable)

        def __next__(self):
            try:
                return next(self.__cur)

            except StopIteration:
                self.__cur = iter(self.__initial)
                return next(self.__cur)

        def __iter__(self):
            return self

    return NewIterator(itr)


print(take(cycle([1, 2, 3]), 10))
